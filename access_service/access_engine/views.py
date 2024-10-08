from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Employee, TechAccount, ItAsset, Role, Company
from .models import Right, Log, Contragent, Contract_Type

from .forms import EmployeeForm, TechAccountForm, ItAssetForm, CompanyForm
from .forms import RoleForm, RightForm, ContractTypeForm
from .forms import ContragentForm

from .utils import logsave

# Create your views here.
MAX_OBJECTS_NUMBER = 30


# Service Mixins
class FVMixin:
    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user.email
        logsave('create', object.__str__, self.request.user.username)
        object.save()
        return super().form_valid(form)


class DelMixin:
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class CUDMixin:
    template_name = 'access_engine/common/create_update.html'


# Main page
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'access_engine/homepage.html'


# функции Contract_type


class ContractMixin:
    success_url = reverse_lazy('access_engine:contract_list')


class ContractModelMixin:
    model = Contract_Type


# ready
class ContractListView(LoginRequiredMixin, ContractModelMixin, ListView):
    ordering = 'type'
    paginate_by = 30
    template_name = 'access_engine/contract/list.html'
    context_object_name = 'contracts'


# ready
class ContractCreateView(ContractModelMixin, ContractMixin, FVMixin,
                         CUDMixin, LoginRequiredMixin, CreateView):
    form_class = ContractTypeForm


# ready
class ContractUpdateView(ContractModelMixin, ContractMixin, FVMixin,
                         CUDMixin, LoginRequiredMixin, UpdateView):
    form_class = ContractTypeForm


# ready
class ContractDeleteView(ContractModelMixin, ContractMixin,
                         CUDMixin, LoginRequiredMixin, DeleteView):

    def get_context_data(self, **kwargs):
        context = super(ContractDeleteView, self).get_context_data(**kwargs)
        context['employees'] = Employee.objects.filter(
            contract_type=self.kwargs['pk'])
        return context


class ContractDetailView(ContractModelMixin, LoginRequiredMixin,
                         DetailView):
    pass


# ready
@login_required
def search_contract(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            lookup = Q(type__icontains=query)
            results = Contract_Type.objects.filter(lookup).distinct()
            context = {'contracts': results}
            return render(request, 'access_engine/contract/list.html', context)


# Функции Contragent


class ContragentMixin:
    success_url = reverse_lazy('access_engine:contragent_list')


class ContragentModelMixin:
    model = Contragent


# ready
class ContragentListView(ContragentModelMixin, LoginRequiredMixin,
                         ListView):
    ordering = 'name'
    paginate_by = 30
    template_name = 'access_engine/contragent/list.html'
    context_object_name = 'contragents'


# ready
class ContragentCreateView(ContragentModelMixin, ContragentMixin, FVMixin,
                           CUDMixin, LoginRequiredMixin, CreateView):
    form_class = ContragentForm


# ready
class ContragentUpdateView(ContragentModelMixin, ContragentMixin, FVMixin,
                           CUDMixin, LoginRequiredMixin, UpdateView):
    form_class = ContragentForm


# ready
class ContragentDeleteView(ContragentModelMixin, ContragentMixin,
                           CUDMixin, LoginRequiredMixin, DeleteView):
    def get_context_data(self, **kwargs):
        context = super(ContragentDeleteView, self).get_context_data(**kwargs)
        context['employees'] = Employee.objects.filter(
            contragent=self.kwargs['pk'])
        return context


class ContragentDetailView(ContragentModelMixin, LoginRequiredMixin,
                           DetailView):
    pass


# ready
@login_required
def search_contragent(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            results = Contragent.objects.filter(
                Q(name__icontains=query) |
                Q(person__icontains=query) |
                Q(phone_number__icontains=query) |
                Q(email__icontains=query) |
                Q(duty_employee__common_name__icontains=query)
            ).distinct()
            context = {'contragents': results}
            return render(request, 'access_engine/contragent/list.html',
                          context)


# Функции Company


class CompanyMixin:
    success_url = reverse_lazy('access_engine:company_list')


class CompanyModelMixin:
    model = Company


# ready
class CompanyListView(CompanyModelMixin, LoginRequiredMixin, ListView):
    ordering = 'name'
    paginate_by = 30
    template_name = 'access_engine/company/list.html'
    context_object_name = 'companies'


# ready
class CompanyCreateView(CompanyModelMixin, CompanyMixin, FVMixin,
                        CUDMixin, LoginRequiredMixin, CreateView):
    form_class = CompanyForm


# ready
class CompanyUpdateView(CompanyModelMixin, CompanyMixin, FVMixin,
                        CUDMixin, LoginRequiredMixin, UpdateView):
    form_class = CompanyForm


# ready (without checker)
class CompanyDeleteView(CompanyModelMixin, CompanyMixin,
                        CUDMixin, LoginRequiredMixin, DeleteView):
    def get_context_data(self, **kwargs):
        context = super(CompanyDeleteView, self).get_context_data(**kwargs)
        context['employees'] = Employee.objects.filter(
            company=self.kwargs['pk'])
        return context


# ready
@login_required
def search_company(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            lookup = Q(name__icontains=query)
            results = Company.objects.filter(lookup).distinct()
            context = {'companies': results}
            return render(request, 'access_engine/company/list.html', context)


# Функции Employee


class EmployeeMixin:
    success_url = reverse_lazy('access_engine:employee_list')


class EmployeeModelMixin:
    model = Employee


# ready
class EmployeeListView(EmployeeModelMixin, LoginRequiredMixin, ListView):
    ordering = 'common_name'
    paginate_by = 30
    template_name = 'access_engine/employee/list.html'
    context_object_name = 'employees'


# ready
class EmployeeCreateView(EmployeeModelMixin, EmployeeMixin,
                         CUDMixin, LoginRequiredMixin, CreateView):
    form_class = EmployeeForm

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user.username
        logsave('create', object.__str__, self.request.user.username)
        object.common_name = (object.surname + " " + object.name + " " +
                              object.patronym)
        object.save()
        return super().form_valid(form)


# ready
class EmployeeUpdateView(EmployeeModelMixin, EmployeeMixin, FVMixin,
                         CUDMixin, LoginRequiredMixin, UpdateView):
    form_class = EmployeeForm

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user.username
        logsave('create', object.__str__, self.request.user.username)
        object.common_name = (object.surname + " " + object.name + " " +
                              object.patronym)
        object.save()
        return super().form_valid(form)


# ready
class EmployeeDeleteView(EmployeeModelMixin, EmployeeMixin,
                         CUDMixin, LoginRequiredMixin, DeleteView):
    def get_context_data(self, **kwargs):
        context = super(EmployeeDeleteView, self).get_context_data(**kwargs)
        context['duties'] = Contragent.objects.filter(
            duty_employee=self.kwargs['pk']
        )
        context['itassets'] = ItAsset.objects.filter(
            owner=self.kwargs['pk']
        )
        context['techaccounts'] = TechAccount.objects.filter(
            owner=self.kwargs['pk']
        )
        return context


class EmployeeDetailView(EmployeeModelMixin, EmployeeMixin,
                         CUDMixin, LoginRequiredMixin, DetailView):
    pass


# ready
@login_required
def search_employee(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            results = Employee.objects.filter(
                Q(common_name__icontains=query) |
                Q(contract_type__type__icontains=query) |
                Q(contragent__name__icontains=query) |
                Q(company__name__icontains=query)
            ).distinct()
            context = {'employees': results}
            return render(request, 'access_engine/employee/list.html', context)


# Функции ItAsset


class ItAssetMixin:
    success_url = reverse_lazy('access_engine:itasset_list')


class ItAssetModelMixin:
    model = ItAsset


# ready
class ItAssetListView(ItAssetModelMixin, LoginRequiredMixin, ListView):
    ordering = 'name'
    paginate_by = 30
    template_name = 'access_engine/itasset/list.html'
    context_object_name = 'itassets'


# ready
class ItAssetCreateView(ItAssetModelMixin, ItAssetMixin, FVMixin,
                        CUDMixin, LoginRequiredMixin, CreateView):
    form_class = ItAssetForm


# ready
class ItAssetUpdateView(ItAssetModelMixin, ItAssetMixin, FVMixin,
                        CUDMixin, LoginRequiredMixin, UpdateView):
    form_class = ItAssetForm


# ready
class ItAssetDeleteView(ItAssetModelMixin, ItAssetMixin,
                        CUDMixin, LoginRequiredMixin, DeleteView):
    pass


class ItAssetDetailView(ItAssetModelMixin, LoginRequiredMixin,
                        DetailView):
    pass


# ready
@login_required
def search_itasset(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            results = ItAsset.objects.filter(
                Q(name__icontains=query) |
                Q(url_address__icontains=query) |
                Q(ip_address__icontains=query) |
                Q(owner__common_name__icontains=query)
            ).distinct()
            context = {'itassets': results}
            return render(request, 'access_engine/itasset/list.html', context)


# Функции Log


class LogListView(LoginRequiredMixin, ListView):
    model = Log
    ordering = 'id'
    paginate_by = 30
    template_name = 'access_engine/log/list.html'
    context_object_name = 'logs'


# Функции Role


class RoleMixin:
    success_url = reverse_lazy('access_engine:role_list')


class RoleModelMixin:
    model = Role
    template_name = 'access_engine/common/create_update.html'


# ready
class RoleListView(RoleModelMixin, LoginRequiredMixin, ListView):
    ordering = 'name'
    paginate_by = 30
    template_name = 'access_engine/role/list.html'
    context_object_name = 'roles'


# ready
class RoleCreateView(RoleModelMixin, RoleMixin,
                     CUDMixin, LoginRequiredMixin, CreateView):
    form_class = RoleForm

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user.username
        object.name = object.itasset.name + " - " + object.name
        logsave('create', object.__str__, self.request.user.username)
        object.save()
        return super().form_valid(form)


# ready
class RoleUpdateView(RoleModelMixin, RoleMixin, FVMixin,
                     CUDMixin, LoginRequiredMixin, UpdateView):
    form_class = RoleForm


# ready
class RoleDeleteView(RoleModelMixin, RoleMixin,
                     CUDMixin, LoginRequiredMixin, DeleteView):
    pass


class RoleDetailView(RoleModelMixin, LoginRequiredMixin, DetailView):
    pass


# ready
@login_required
def search_role(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            results = Role.objects.filter(
                Q(name__icontains=query) |
                Q(itasset__name__icontains=query)
            ).distinct()
            context = {'roles': results}
            return render(request, 'access_engine/role/list.html', context)


# Функции Right


class RightMixin:
    success_url = reverse_lazy('access_engine:right_list')


class RightModelMixin:
    model = Right


# ready
class RightListView(RightModelMixin, LoginRequiredMixin, ListView):
    ordering = 'id'
    paginate_by = 30
    template_name = 'access_engine/right/list.html'
    context_object_name = 'rights'


# ready
class RightCreateView(RightModelMixin, RightMixin, FVMixin,
                      CUDMixin, LoginRequiredMixin, CreateView):
    form_class = RightForm


# ready
class RightUpdateView(RightModelMixin, RightMixin, FVMixin,
                      CUDMixin, LoginRequiredMixin, UpdateView):
    form_class = RightForm


# ready
class RightDeleteView(RightModelMixin, RightMixin, CUDMixin,
                      LoginRequiredMixin, DeleteView):
    pass


class RightDetailView(RightModelMixin, LoginRequiredMixin,
                      DetailView):
    pass


# ready
@login_required
def search_right(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            results = Right.objects.filter(
                Q(role__name__icontains=query) |
                Q(employee__common_name__icontains=query) |
                Q(techaccount__name__icontains=query) |
                Q(role__itasset__name__icontains=query)
            ).distinct()
            context = {'rights': results}
            return render(request, 'access_engine/right/list.html', context)


# Функции TechAccount


class TechAccountMixin:
    success_url = reverse_lazy('access_engine:techaccount_list')


class TechAccountModelMixin:
    model = TechAccount


# ready
class TechAccountListView(TechAccountModelMixin, LoginRequiredMixin,
                          ListView):
    ordering = 'name'
    paginate_by = 30
    template_name = 'access_engine/techaccount/list.html'
    context_object_name = 'techaccounts'


# ready
class TechAccountCreateView(TechAccountModelMixin, TechAccountMixin,
                            CUDMixin, FVMixin, LoginRequiredMixin,
                            CreateView):
    form_class = TechAccountForm


# ready
class TechAccountUpdateView(TechAccountModelMixin, TechAccountMixin,
                            CUDMixin, FVMixin, LoginRequiredMixin,
                            UpdateView):
    form_class = TechAccountForm


# ready
class TechAccountDeleteView(TechAccountModelMixin, TechAccountMixin,
                            FVMixin, LoginRequiredMixin, DeleteView):
    pass


class TechAccountDetailView(TechAccountModelMixin, LoginRequiredMixin,
                            DetailView):
    pass


# ready
@login_required
def search_techaccount(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            results = TechAccount.objects.filter(
                Q(name__icontains=query) |
                Q(owner__common_name__icontains=query) |
                Q(itasset__name__icontains=query)
            ).distinct()
            context = {'techaccounts': results}
            return render(request, 'access_engine/techaccount/list.html',
                          context)


def ajax_load_roles(request):
    itasset_id = request.GET.get('itasset')
    roles = Role.objects.filter(itasset_id=itasset_id).order_by('name')
    print(roles)
    context = {'roles': roles}
    return render(request, 'access_engine/common/ajax_roles.html', context)


# def view_employees_list(request):
#    page = "access_engine/employees_list.html"
#    employees = Employee.objects.order_by('surname')[:MAX_OBJECTS_NUMBER]
#    context = {'employees_list': employees}
#    return render(request, page, context)

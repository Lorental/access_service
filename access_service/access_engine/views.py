from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

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
        object.created_by = self.request.user.username
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
    ordering = 'id'
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
    pass


class ContractDetailView(ContractModelMixin, LoginRequiredMixin,
                         DetailView):
    pass


# Функции Contragent


class ContragentMixin:
    success_url = reverse_lazy('access_engine:contragent_list')


class ContragentModelMixin:
    model = Contragent


# ready
class ContragentListView(ContragentModelMixin, LoginRequiredMixin,
                         ListView):
    ordering = 'id'
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
    pass


class ContragentDetailView(ContragentModelMixin, LoginRequiredMixin,
                           DetailView):
    pass


# Функции Company


class CompanyMixin:
    success_url = reverse_lazy('access_engine:company_list')


class CompanyModelMixin:
    model = Company


# ready
class CompanyListView(CompanyModelMixin, LoginRequiredMixin, ListView):
    ordering = 'id'
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
    pass


# Функции Employee


class EmployeeMixin:
    success_url = reverse_lazy('access_engine:employee_list')


class EmployeeModelMixin:
    model = Employee


# ready
class EmployeeListView(EmployeeModelMixin, LoginRequiredMixin, ListView):
    ordering = 'id'
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
        object.common_name = object.surname + " " + object.name + " " + object.patronym
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
        object.common_name = object.surname + " " + object.name + " " + object.patronym
        object.save()
        return super().form_valid(form)


# ready
class EmployeeDeleteView(EmployeeModelMixin, EmployeeMixin,
                         CUDMixin, LoginRequiredMixin, DeleteView):
    pass


class EmployeeDetailView(EmployeeModelMixin, EmployeeMixin,
                         CUDMixin, LoginRequiredMixin, DetailView):
    pass


# Функции ItAsset


class ItAssetMixin:
    success_url = reverse_lazy('access_engine:itasset_list')


class ItAssetModelMixin:
    model = ItAsset


# ready
class ItAssetListView(ItAssetModelMixin, LoginRequiredMixin, ListView):
    ordering = 'id'
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
    ordering = 'id'
    paginate_by = 30
    template_name = 'access_engine/role/list.html'
    context_object_name = 'roles'


# ready
class RoleCreateView(RoleModelMixin, RoleMixin, FVMixin,
                     CUDMixin, LoginRequiredMixin, CreateView):
    form_class = RoleForm


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


# Функции TechAccount


class TechAccountMixin:
    success_url = reverse_lazy('access_engine:techaccount_list')


class TechAccountModelMixin:
    model = TechAccount


# ready
class TechAccountListView(TechAccountModelMixin, LoginRequiredMixin,
                          ListView):
    ordering = 'id'
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


# def view_employees_list(request):
#    page = "access_engine/employees_list.html"
#    employees = Employee.objects.order_by('surname')[:MAX_OBJECTS_NUMBER]
#    context = {'employees_list': employees}
#    return render(request, page, context)

from django import forms
from django.contrib.auth import get_user_model

from .models import Contract_Type, Contragent, Company, Employee
from .models import ItAsset, Role, Right, TechAccount, Log


User = get_user_model()


class ContractTypeForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=Contract_Type.objects.order_by(
        'type'))

    class Meta:
        model = Contract_Type
        fields = (
            'type',
        )


class ContragentForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Contragent.objects.order_by('name'))

    class Meta:
        model = Contragent
        fields = (
            'name',
            'person',
            'phone_number',
            'email',
            'duty_employee',
        )


class CompanyForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Company.objects.order_by('name'))

    class Meta:
        model = Company
        fields = (
            'name',
        )


# Asset class forms


class EmployeeForm(forms.ModelForm):
    contract_type = forms.ModelChoiceField(
        queryset=Contract_Type.objects.order_by('type'))
    contragent = forms.ModelChoiceField(queryset=Contragent.objects.order_by(
        'name'))
    company = forms.ModelChoiceField(queryset=Company.objects.order_by(
        'name'))

    class Meta:
        model = Employee
        fields = (
            'surname',
            'name',
            'patronym',
            'contract_type',
            'is_active',
            'is_contragent',
            'contragent',
            'company',
            'end_time',
        )


class ItAssetForm(forms.ModelForm):
    owner = forms.ModelChoiceField(queryset=Employee.objects.filter(
        is_contragent=False).order_by('common_name'))

    class Meta:
        model = ItAsset
        fields = (
            'name',
            'url_address',
            'ip_address',
            'owner',
            'comment',
        )


class LogForm(forms.ModelForm):

    class Meta:
        model = Log
        fields = '__all__'


# Employees right forms


class RoleForm(forms.ModelForm):
    itasset = forms.ModelChoiceField(queryset=ItAsset.objects.order_by('name'))

    class Meta:
        model = Role
        fields = (
            'name',
            'itasset',
        )


class RightForm(forms.ModelForm):
    role = forms.ModelChoiceField(queryset=Role.objects.order_by(
        'name'))
    employee = forms.ModelChoiceField(queryset=Employee.objects.order_by(
        'common_name'))
    techaccount = forms.ModelChoiceField(queryset=TechAccount.objects.order_by(
        'name'))

    class Meta:
        model = Right
        fields = (
            'is_tech',
            'role',
            'employee',
            'techaccount',
        )


# Composite asset forms


class TechAccountForm(forms.ModelForm):
    owner = forms.ModelChoiceField(Employee.objects.order_by(
        'common_name'))
    itasset = forms.ModelChoiceField(ItAsset.objects.order_by(
        'name'))

    class Meta:
        model = TechAccount
        fields = (
            'name',
            'is_active',
            'owner',
            'itasset',
        )

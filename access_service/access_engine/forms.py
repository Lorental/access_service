from django import forms
from django.contrib.auth import get_user_model

from .models import Contract_Type, Contragent, Company, Employee
from .models import ItAsset, Role, Right, TechAccount, Log


User = get_user_model()


class ContractTypeForm(forms.ModelForm):

    class Meta:
        model = Contract_Type
        fields = (
            'type',
        )


class ContragentForm(forms.ModelForm):

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

    class Meta:
        model = Company
        fields = (
            'name',
        )


# Asset class forms


class EmployeeForm(forms.ModelForm):

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

    class Meta:
        model = Role
        fields = (
            'name',
            'itasset',
        )


class RightForm(forms.ModelForm):

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

    class Meta:
        model = TechAccount
        fields = (
            'name',
            'is_active',
            'owner',
            'itasset',
            'role',
        )

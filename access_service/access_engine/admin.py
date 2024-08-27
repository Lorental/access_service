from django.contrib import admin
from access_engine.models import ItAsset, Log, Contract_Type, Contragent, Company
from access_engine.models import Employee, Role, TechAccount, Right, AbsUser
# Register your models here.

@admin.register(ItAsset, Log, Contract_Type, Contragent, Employee, Role, Right, TechAccount, AbsUser, Company)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

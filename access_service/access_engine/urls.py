from django.urls import path, include

from .import views

app_name = 'access_engine'

urlpatterns = [
    # main page
    path('', views.HomePage.as_view(), name='homepage'),
    # authorization pages
    path('auth/', include('django.contrib.auth.urls')),
    # contract types urls
    path(
        'contract/list/',
        views.ContractListView.as_view(),
        name='contract_list'
        ),

    path(
        'contract/create/',
        views.ContractCreateView.as_view(),
        name='contract_create'
        ),

    path(
        'contract/update/<int:pk>',
        views.ContractUpdateView.as_view(),
        name='contract_update'
        ),
    path(
        'contract/delete/<int:pk>',
        views.ContractDeleteView.as_view(),
        name='contract_delete'
        ),
    path(
        'contract/<int:pk>',
        views.ContractDetailView.as_view(),
        name='contract_detail'
        ),
    # contragents urls
    path(
        'contragent/list/',
        views.ContragentListView.as_view(),
        name='contragent_list'
        ),
    path(
        'contragent/create/',
        views.ContragentCreateView.as_view(),
        name='contragent_create'
        ),
    path(
        'contragent/update/<int:pk>',
        views.ContragentUpdateView.as_view(),
        name='contragent_update'
        ),
    path(
        'contragent/delete/<int:pk>',
        views.ContragentDeleteView.as_view(),
        name='contragent_delete'
        ),
    path(
        'contragent/<int:pk>/',
        views.ContragentDetailView.as_view(),
        name='contragent_detail'
        ),
    # company urls
    path(
        'company/list/',
        views.CompanyListView.as_view(),
        name='company_list'
        ),
    path(
        'company/create/',
        views.CompanyCreateView.as_view(),
        name='company_create'
        ),
    path(
        'company/update/<int:pk>',
        views.CompanyUpdateView.as_view(),
        name='company_update'
        ),
    path(
        'company/delete/<int:pk>',
        views.CompanyDeleteView.as_view(),
        name='company_delete'
        ),
    # log urls
    path(
        'log/list',
        views.LogListView.as_view(),
        name='log_list'
    ),
    # employee urls
    path(
        'employee/list/',
        views.EmployeeListView.as_view(),
        name='employee_list'
        ),
    path(
        'employee/create/',
        views.EmployeeCreateView.as_view(),
        name='employee_create'
        ),
    path(
        'employee/update/<int:pk>',
        views.EmployeeUpdateView.as_view(),
        name='employee_update'
        ),
    path(
        'employee/delete/<int:pk>',
        views.EmployeeDeleteView.as_view(),
        name='employee_delete'
        ),
    path(
        'employee/<int:pk>/',
        views.EmployeeDetailView.as_view(),
        name='employee_detail'
        ),
    # it asset urls
    path(
        'itasset/list/',
        views.ItAssetListView.as_view(),
        name='itasset_list'
        ),
    path(
        'itasset/create/',
        views.ItAssetCreateView.as_view(),
        name='itasset_create'
        ),
    path(
        'itasset/update/<int:pk>',
        views.ItAssetUpdateView.as_view(),
        name='itasset_update'
        ),
    path(
        'itasset/delete/<int:pk>',
        views.ItAssetDeleteView.as_view(),
        name='itasset_delete'
        ),
    path(
        'itasset/<int:pk>/',
        views.ItAssetDetailView.as_view(),
        name='itasset_detail'
        ),
    # role urls
    path(
        'role/list/',
        views.RoleListView.as_view(),
        name='role_list'
        ),
    path(
        'role/create/',
        views.RoleCreateView.as_view(),
        name='role_create'
        ),
    path(
        'role/update/<int:pk>',
        views.RoleUpdateView.as_view(),
        name='role_update'
        ),
    path(
        'role/delete/<int:pk>',
        views.RoleDeleteView.as_view(),
        name='role_delete'
        ),
    path(
        'role/<int:pk>/',
        views.RoleDetailView.as_view(),
        name='role_detail'
        ),
    # right urls
    path(
        'right/list/',
        views.RightListView.as_view(),
        name='right_list'
        ),
    path(
        'right/create/',
        views.RightCreateView.as_view(),
        name='right_create'
        ),
    path(
        'right/update/<int:pk>',
        views.RightUpdateView.as_view(),
        name='right_update'
        ),
    path(
        'right/delete/<int:pk>',
        views.RightDeleteView.as_view(),
        name='right_delete'
        ),
    path(
        'right/<int:pk>/',
        views.RightDetailView.as_view(),
        name='right_detail'
        ),
    # tech account urls
    path(
        'techaccount/list/',
        views.TechAccountListView.as_view(),
        name='techaccount_list'
        ),
    path(
        'techaccount/create/',
        views.TechAccountCreateView.as_view(),
        name='techaccount_create'
        ),
    path(
        'techaccount/update/<int:pk>',
        views.TechAccountUpdateView.as_view(),
        name='techaccount_update'
        ),
    path(
        'techaccount/delete/<int:pk>',
        views.TechAccountDeleteView.as_view(),
        name='techaccount_delete'
        ),
    path(
        'techaccount/<int:pk>/',
        views.TechAccountDetailView.as_view(),
        name='techaccount_detail'
        )
]

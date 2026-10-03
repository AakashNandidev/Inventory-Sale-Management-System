"""
URL configuration for inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory_sale import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("inventory/", views.inventory, name="inventory"),
    path('stock-history/', views.stock_history, name='stock_history'),
    path("inventory/add/", views.add_product, name="add_product"),
    path("sales/", views.sales, name="sales"),
    path("sales/new/", views.new_sale, name="new_sale"),
    path("invoices/", views.invoices, name="invoices"),
    path("invoices/<int:sale_id>/", views.invoice_detail, name="invoice_detail"),
    path("customers/", views.customers, name="customers"),
    path("customers/add/", views.add_customer, name="add_customer"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("suppliers/add/", views.add_supplier, name="add_suppliers"),
    path("suppliers/edit/<int:supplier_id>/", views.edit_supplier, name="edit_supplier"),
    path("suppliers/delete/<int:supplier_id>/", views.delete_supplier, name="delete_supplier"),
    path("customers/edit/<int:customer_id>/",views.edit_customer,name="edit_customer"),
    path("customers/delete/<int:customer_id>/",views.delete_customer,name="delete_customer"),

    path("reports/", views.reports, name="reports"),
    path("reports/sales/", views.sales_report, name="sales_report"),
    path(
    'reports/sales/export/',
    views.export_sales_excel,
    name='export_sales_excel'
    ),
    path(
            'reports/inventory/export/',
            views.export_inventory_excel,
            name='export_inventory_excel'
            ),
    path(
            'reports/customer/export/',
            views.export_customer_excel,
            name='export_customer_excel'
            ),
    path(
    'reports/suppliers/export/',
    views.export_supplier_excel,
    name='export_supplier_excel'
),

path(
    'reports/revenue/export/',
    views.export_revenue_excel,
    name='export_revenue_excel'
),

path(
    'reports/pending_payments/export/',
    views.export_pending_payments_excel,
    name='export_pending_payments_excel'
),
    path("reports/inventory/", views.inventory_report, name="inventory_report"),
    path("reports/customers/", views.customer_report, name="customer_report"),
    path("reports/suppliers/", views.supplier_report, name="supplier_report"),
    path("reports/revenue/", views.revenue_report, name="revenue_report"),
    path("reports/pending_payments/", views.pending_payments_report, name="pending_payments_report"),
    path(
    "settings/",
    views.settings_view,
    name="settings"
),

path(
    "settings/profile/",
    views.update_profile,
    name="update_profile"
),

path(
    "settings/password/",
    views.change_password,
    name="change_password"
),
    
    path("inventory/edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("inventory/delete/<int:product_id>/", views.delete_product, name="delete_product"),
    
]

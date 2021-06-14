from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('product/', views.product, name="product"),
    path('supplier/', views.supplier, name="supplier"),
    path('customer/', views.customer, name="customer"),
    path('sales/', views.sales, name="sales"),
    path('purchase/', views.purchase, name="purchase"),
]

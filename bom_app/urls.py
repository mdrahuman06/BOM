from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('calculate/', views.calculate_selected, name='calculate_selected'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-product/', views.add_product, name='add_product'),
    path('product/<int:pk>/add-bom-item/', views.add_bom_item, name='add_bom_item'),
]

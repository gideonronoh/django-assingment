from django.urls import path
from .views import product_list, product_create, product_update, product_delete, export_to_csv, import_from_csv

urlpatterns = [
    path('', product_list, name='product_list'),
    path('create/', product_create, name='product_create'),
    path('update/<int:pk>/', product_update, name='product_update'),
    path('delete/<int:pk>/', product_delete, name='product_delete'),
    path('export/', export_to_csv, name='export_to_csv'),
    path('import/', import_from_csv, name='import_from_csv'),
]

from django.urls import path
from .views import *

urlpatterns = [
    # URL'S for API endpoints
    path('api/products/', product_list_api, name='product_list_api'),
    path('api/products/<int:pk>/', product_detail_api, name='product_detail_api'),
    
    # URL's for Template views
    path('', product_list, name='product_list'),
    path('create/', product_create, name='product_create'),
    path('update/<int:pk>/', product_update, name='product_update'),
    path('delete/<int:pk>/', product_delete, name='product_delete'),
] 
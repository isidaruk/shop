from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shop.api import views


urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<int:pk>/', views.category_detail),
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

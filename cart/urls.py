from django.urls import path
from .views import cart_detail_view, cart_add_view, cart_remove_view

app_name = 'cart'

urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/', cart_add_view, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove_view, name='cart_remove'),
]

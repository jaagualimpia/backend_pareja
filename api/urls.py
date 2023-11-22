from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.products, name='product'),
    path('products/<int:product_id>', views.product, name='product'),
    path('orders/', views.orders, name='order'),
    path('orders/<int:order_id>', views.order, name='order')
]
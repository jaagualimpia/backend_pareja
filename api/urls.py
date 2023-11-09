from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.products, name='product'),
    path('product/<int:product_id>', views.product, name='product'),
    path('order/', views.orders, name='order'),
    path('order/<int:order_id>', views.order, name='order')
]
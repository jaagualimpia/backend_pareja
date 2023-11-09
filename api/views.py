from django.http import HttpResponse, JsonResponse
from .services.orderService import getAllOrdersService, createOrderService, getOrderByIdService, updateOrderService, deleteOrderByIdService
from .services.productService import getAllProductsService, createProductService, getProductByIdService, updateProductService, deleteProductByIdService
from .forms import OrderForm, ProductForm
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def orders(request):
    if request.method == 'POST':
        form = OrderForm(json.loads(request.body))

        if form.is_valid():
            return createOrderService(form.cleaned_data)
        else:
            return HttpResponse("Something really bad happened in your request", status=400)

    return getAllOrdersService()

@csrf_exempt
def order(request, order_id=0):
    if request.method == 'GET':
        return getOrderByIdService(order_id)

    if request.method == 'PUT':
        return updateOrderService(order_id, json.loads(request.body))

    if request.method == 'DELETE':
        return deleteOrderByIdService(order_id)


@csrf_exempt
def products(request):
    if request.method == 'POST':
        form = ProductForm(json.loads(request.body))

        if form.is_valid():
            return createProductService(form.cleaned_data)
        else:
            return HttpResponse("Something really happened bad in your request", status=400)

    return getAllProductsService()


def product(request, product_id=0):
    if request.method == 'GET':
        return getProductByIdService(product_id)

    if request.method == 'PUT':
        return updateProductService(product_id, json.loads(request.body))

    if request.method == 'DELETE':
        return deleteProductByIdService(product_id)

from django.http import HttpResponse, JsonResponse
from .services.orderService import getAllOrdersService, createOrderService, getOrderByIdService, updateOrderService, deleteOrderByIdService
from .services.productService import addProductToOrderService, getAllProductsService, createProductService, getProductByIdService, updateProductService, deleteProductByIdService
from .forms import OrderForm, OrderToProductForm, ProductForm
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def orders(request):
    request
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        form = OrderForm(body)
  
        if form.is_valid():
            return JsonResponse(createOrderService(form.cleaned_data), status=201, safe=False)
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
        body = json.loads(request.body.decode('utf-8'))
                  
        for product in body["products"]:
            quantity_form = OrderToProductForm(product)
            product_form = ProductForm(product["product"])
            
            if product_form.is_valid() and quantity_form.is_valid():
                addProductToOrderService(product_form.cleaned_data, quantity_form.cleaned_data, body["OwnerId"])
            return JsonResponse({"state": True}, status=201, safe=False)
        else:
            return HttpResponse("Something really bad happened in your request", status=400)

    return getAllProductsService()


def product(request, product_id=0):
    if request.method == 'GET':
        return getProductByIdService(product_id)

    if request.method == 'PUT':
        return updateProductService(product_id, json.loads(request.body))

    if request.method == 'DELETE':
        return deleteProductByIdService(product_id)

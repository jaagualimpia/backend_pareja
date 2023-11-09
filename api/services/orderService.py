from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from ..repositories.orderRepository import getAllOrders, getOrderById, createOrder, updateOrder, deleteOrderById
from django.forms.models import model_to_dict

def getAllOrdersService():
    try:
        return JsonResponse(list(getAllOrders()), safe=False)
    except Exception as e:
        return HttpResponseServerError(e)
    
def getOrderByIdService(id):
    try:
        order = model_to_dict(getOrderById(id))
        return JsonResponse(order, safe=False)
    
    except Exception:
        return HttpResponse(f"Order with id: {id} cant be found", status=404)
    
def createOrderService(order):
    try:
        createOrder(order)
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponseServerError(e)
    
def updateOrderService(order):
    try:
        order = getOrderById(order.id)
        updateOrder(order)

        return HttpResponse(status=200)
    
    except Exception:
        return HttpResponse(f"Order with id: {id} cant be found", status=404)
    
def deleteOrderByIdService(id):
    try:
        getOrderById(id)
        deleteOrderById(id)

        return HttpResponse(status=200)
    
    except Exception:
        return HttpResponse(f"Order with id: {id} cant be found", status=404)
    

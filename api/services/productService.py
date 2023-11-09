from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from ..repositories.productRepository import getAllProducts, getProductById, createProduct, updateProduct, deleteProductById
from django.forms.models import model_to_dict


def getAllProductsService():
    try:
        return JsonResponse(list(getAllProducts()), safe=False)
    except Exception as e:
        return HttpResponseServerError(e)
    
def getProductByIdService(id):
    try:
        product = model_to_dict(getProductById(id))
        return JsonResponse(product, safe=False)
    
    except Exception:
        return HttpResponse(f"Product with id: {id} cant be found", status=404)
    
def createProductService(product):
    try:
        createProduct(product)
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponseServerError(e)
    
def updateProductService(product):
    try:
        product = getProductById(product.id)
        updateProduct(product)

        return HttpResponse(status=200)
    
    except Exception:
        return HttpResponse(f"Product with id: {id} cant be found", status=404)

def deleteProductByIdService(id):
    try:
        getProductById(id)
        deleteProductById(id)

        return HttpResponse(status=200)
    
    except Exception:
        return HttpResponse(f"Product with id: {id} cant be found", status=404)
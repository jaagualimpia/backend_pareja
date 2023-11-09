from api.models import Product


def getAllProducts():
    product = Product.objects.all().values()
    return product

def getProductById(id):
    product = Product.objects.get(id=id)
    return product

def createProduct(product):
    try:
        product = Product.objects.create(
            name=product['name'],
            price=product['price'],
            description=product['description']
        ).save()
    except Exception as e:
        raise e
    
def updateProduct(product):
    try:
        product = Product.objects.get(id=product['id'])
        product.name = product['name']
        product.price = product['price']
        product.description = product['description']
        product.save()
        
    except Exception as e:
        raise e
    
def deleteProductById(id):
    try:
        Product.objects.get(id=id).delete()
    except Exception as e:
        raise e
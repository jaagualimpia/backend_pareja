from api.models import Order, OrderToProduct, Product


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
        )
        product.save()
        return product
    except Exception as e:
        raise e
    
def addProductToOrder(order_id, product, quantity):
    try:
        print(order_id)
        print(product)
        print(quantity)

        order = Order.objects.get(id=order_id)
        product = Product.objects.filter(name=product['name'], price=product['price'], description=product['description'])[0]        
        orderToProduct = OrderToProduct.objects.create(
            order=order,
            product=product,
            quantity=int(quantity)
        )
        orderToProduct.save()
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
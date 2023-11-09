from api.models import Order

def getAllOrders():
    return Order.objects.all().values()

def getOrderById(id):
    return Order.objects.get(id=id)

def createOrder(order):
    try:
        order = Order.objects.create(
            date=order['date'],
            total=order['total'],
            status=order['status'],
            address=order['address']
        ).save()

    except Exception as e:
        raise e

def updateOrder(order):
    try:
        order = Order.objects.get( id= order['id'])
       
        order.date=order['date'],
        order.total=order['total'],
        order.status=order['status'],
        order.address=order['address']
        order.save()
        
    except Exception as e:
        raise e

def deleteOrderById(id):
    try:
        Order.objects.get(id=id).delete()
    except Exception as e:
        raise e
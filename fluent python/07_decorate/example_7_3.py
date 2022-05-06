
promos = []

def promotions(promo_func):
    promos.append(promo_func)
    return promo_func


@promotions
def fidelity(order):
    '''为积分为1000或以上的顾客提供5%的折扣'''
    return order.total * 0.05 if order.customer.fidelity >= 1000 else 0 

@promotions
def bulk_item(order):
    '''单个商品为20个或以上提供10%的折扣'''
    discount = 0
    for item in order.cart: 
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount 

@promotions
def large_order(order):
    '''订单中的不同商品达到10个或者以上提供7%的折扣'''
    distince_items = {item.produce for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0

def best_promo(order):
    '''选择可用的最佳折扣'''
    return max(promo(order) for promo in promos)

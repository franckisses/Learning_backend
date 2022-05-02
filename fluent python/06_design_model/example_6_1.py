
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity

class Order: # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
   
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
            return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

class Promotion(ABC): # 策略:抽象基类
    @abstractmethod
    def discount(self, order):
        """返回折扣金额(正值)"""

class FidelityPromo(Promotion): # 第一个具体策略
    """为积分为1000或以上的顾客提供5%折扣""" 
    def discount(self, order):

        return order.total() * .05 if order.customer.fidelity >= 1000 else 0 
        
class BulkItemPromo(Promotion): # 第二个具体策略
    """单个商品为20个或以上时提供10%折扣"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
            return discount

class LargeOrderPromo(Promotion): # 第三个具体策略 """订单中的不同商品达到10个或以上时提供7%折扣"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0



Long_text = """
>>> from order_1 import *
>>> joe = Customer('John Doe', 0)
>>> ann = Customer('Ann Smith', 1100)
>>> cart = [LineItem('banana',4,0.5),
... LineItem('apple',10,1.5),
... LineItem('watermelon',5,5)]
>>> Order(joe,cart,FidelityPromo())
<Order total: 42.00 due: 42.00>
>>> Order(ann, cart, FidelityPromo())
<Order total: 42.00 due: 39.90>
>>> banana_cart = [LineItem('banan',30,5),
... LineItem('apple',10,1.5)]
>>> Order(ann,banana_cart,BulkItemPromo())
<Order total: 165.00 due: 150.00>
>>> long_order = [LineItem(str(item_code),1,1.0)
... for item_code in range(10)]
>>> long_order
[<order_1.LineItem object at 0x7f9c77ac7da0>, <order_1.LineItem object at 0x7f9c77ad4080>, <order_1.LineItem object at 0x7f9c77ad4198>, <order_1.LineItem object at 0x7f9c77ad4208>, <order_1.LineItem object at 0x7f9c77ad4278>, <order_1.LineItem object at 0x7f9c77ad42e8>, <order_1.LineItem object at 0x7f9c77ad4358>, <order_1.LineItem object at 0x7f9c77ad43c8>, <order_1.LineItem object at 0x7f9c77ad4438>, <order_1.LineItem object at 0x7f9c77ad44a8>]
>>> Order(joe,long_order,LargeOrderPromo())
<Order total: 10.00 due: 9.30>
>>> 
"""
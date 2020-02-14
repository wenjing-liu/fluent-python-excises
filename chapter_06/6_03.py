from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
  def __init__(self, product, quantity, price):
    self.product = product
    self.quantity = quantity
    self.price = price
  
  def total(self):
    return self.price * self.quantity

class Order:
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
      discount = self.promotion(self)
    return self.total - discount
  
  def __repr__(self):
    fmt = '<Order total: {:.2f} due: {:.2f}>'
    return fmt.format(self.total(), self.due())

def fidelity_promo(order):
  """为积分为1000或以上的顾客提供5%折扣"""
  if order.customer.fidelity >= 1000:
      return order.total() * .05
  else:
    return 0

def bulk_item_promo(order):
  """单个商品为20个或以上时提供10%折扣"""
  discount = 0
  for item in order.cart:
    if item.quantity >= 20:
      discount += item.total() * .1
  return discount

def large_order_promo(order):
  """订单中的不同商品达到10个或以上时提供7%折扣"""
  distinct_items = {item.product for item in order.cart}
  if len(distinct_items) >= 10:
    return order.total() * .07
  return 0

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

joe_order = Order(joe, cart, fidelity_promo)
print(joe_order)
ann_order = Order(ann, cart, fidelity_promo)
print(ann_order)
banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]
joe_banana_order = Order(joe, banana_cart, bulk_item_promo)
print(joe_banana_order)
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
joe_long_order = Order(joe, long_order, large_order_promo)
print(long_order)
print(Order(joe, cart, large_order_promo))

promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order):
  return max(promo(order) for promo in promos)

print(Order(joe, long_order, best_promo))
print(Order(joe, banana_cart, best_promo))
print(Order(ann, cart, best_promo))

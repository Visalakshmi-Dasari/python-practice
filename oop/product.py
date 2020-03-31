class Product():
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, items):
        if items < 10:
            return self.price * items
        elif items >= 10 and items <= 99:
            return (self.price * items) - ((self.price * items) * .1)
        elif items >= 100:
            return (self.price * items) - ((self.price * items) * .2)

    def make_purchase(self, items):
        self.amount = self.amount - items

    def __str__(self):
        return 'name: '+ self.name +'   '+'amount: '+str(self.amount)+'   '+'total value: '+str(self.price*self.amount)


p=Product('car',100,200000)
print p.get_price(20)
p.make_purchase(20)
print str(p)
print p.get_price(20)
p.make_purchase(20)
print str(p)


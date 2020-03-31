class Investment():
    def __init__(self,principal,interest):
        self.principal=principal
        self.interest=interest

    def value_after(self, years):
        return self.principal*((1+(self.interest/100))**years)

    def __str__(self):
        return 'Principal - ' + str(self.principal) +'    '+  'Interest rate  - ' + str(self.interest)

x=Investment(1000,5.12)
print x.interest
print x.principal
print x.value_after(2)
print str(x)


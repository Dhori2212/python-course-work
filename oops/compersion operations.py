class Money:
    def __init__(self, amount):
        self.amount = amount
    def add(self, other):
        return (self.amount + other.amount)
    def equals (self, other):
        return self.amount == other.amount
    



m1=Money(100)
m2=Money(150)
m3=m1.add(m2)

print(m1.amount)
print(m2.equals(m1))




'''class Money:
    def __init__(self,amount):
        self.amount=amount
    def __add__ (self,other):
        return Money(self.amount + other.amount)
    def __eq__'''
        




        
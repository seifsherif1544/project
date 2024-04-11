# OOP (Object Oriented Programming)

# ERP 
class calc():
    def add(self, n1:int, n2:int)->int:
        return n1 + n2

    def subtract(self, n1, n2):
        pass

    def multipy(self, n1, n2):
        n1 * n2

    def divide(self, n1, n2):
        pass

    def square(self, x):
        pass


x = int(0)
firstName = str("Ahmed")
print(x, firstName)

c = calc() # object vs class 
c.add(4, 7)
c1 = calc()



# cascading, camel case, snake case
# CalcTotal, calcTotal, calc_total
# calcTotal(price, qty) => price * qty

class saleInvoice():
    def __init__(self) -> None: # constructore
        # data
        self.price = 1
        self.qty = 1
        # self.total = self.price * self.qty 
        self.customerName = ''

    # def calcTotal(self, price:float, qty:int ) -> float: # method
    def total(self) -> float: # parameterless method
        return self.price * self.qty
    
    
        
si = saleInvoice()
print(si.total())
si.price = 450 # set
print(si.total())
# x = si.price # get print(si.price)
si.qty = 5
total = si.total()
print(total)






class puchaseInvoice():
    pass

class report():
    pass
    

class customer():
    pass

def discount():
    pass


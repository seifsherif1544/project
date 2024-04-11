class invoice(): # parent, base, super
    def __init__(self) -> None:
        # self.__price = 0 # public -> private (access modifiers)
        # self.__qty = 0 # public -> private
        self.__price = 0 # public -> protect (access modifiers)
        self._qty = 0 # public -> protect
    
    # def getPrice(self):
    @property
    def price(self):
        return self.__price
    
    # def setPrice(self, newPrice):
    @price.setter
    def price(self, newPrice):
        if (type(newPrice) == int or type(newPrice) == float) and newPrice >= 0: # 2 + 3 * 4
            self.__price = newPrice
        else:
            raise ValueError("Invalide data")
                
    # def getQty(self):
    @property
    def qty(self):
        return self._qty

    @qty.setter
    # def setQty(self, newQty):
    def qty(self, newQty):
        if (type(newQty) == int or type(newQty) == float) and newQty >= 0:
            self._qty = newQty
        else:
            raise ValueError("Invalide data")    
    
    def total(self):
        return self.__price * self._qty        
    
class saleInvocie(invoice): # public, protected not private
    def __init__(self) -> None:
        super().__init__()

    def printData(self):
        pass
        # print(self.__price)

sInv1 = saleInvocie()
sInv1.printData()

# print(sInv1.__price) # 
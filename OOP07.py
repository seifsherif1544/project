from OOP06 import invoice
from m_reading import readInteger

inv1 = invoice()

try:  
    inv1.price = readInteger("Please, enter price: ", start=0)
    inv1.qty = readInteger("Please, enter quantity: ", start=0)
    print(inv1.total())
except:
    print("error")

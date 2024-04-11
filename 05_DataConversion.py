# Data conversion = casting

price = float( input("Please, enter price: ") ) # '25' -> 25 / 'Hi' -> Hi
qty = int( input("Please, enter quantity: ") ) # '100' -> 100
total = int(price * qty)

# "Total is: " + "2500.0" + " $."
print("Total is: " + str(total) + " $.") # 2500.0 -> '2500.0' -> Total is: 2500.0 $.

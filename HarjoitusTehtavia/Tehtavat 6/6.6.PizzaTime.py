import math

def PizzaPrice(diameter, price):
    diameterInMeters = diameter*0.01
    pizzaSize = (math.pi/4) * diameterInMeters**2
    return pizzaSize * price

diameter = float(input("Anna pizzan halkaisija senttimetreinä: "))
price = float(input("Anna pizzan hinta: "))

pizza1Price = PizzaPrice(diameter,price)

diameter = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
price = float(input("Anna toisen pizzan hinta: "))

pizza2Price = PizzaPrice(diameter,price)

if pizza1Price < pizza2Price:
    print("Ensimmäisellä pizzalla on alhaisempi yksikköhinta kuin toisella pizzalla.")
    print(f"Ensimmäisin pizzan yksikköhinta: {pizza1Price} vs toisen pizzan yksikköhinta:{pizza2Price}.")
else:
    print("Toisella pizzalla on alhaisempi yksikköhinta kuin ensimmäisellä pizzalla.")
    print(f"Ensimmäisin pizzan yksikköhinta: {pizza1Price} vs toisen pizzan yksikköhinta:{pizza2Price}.")
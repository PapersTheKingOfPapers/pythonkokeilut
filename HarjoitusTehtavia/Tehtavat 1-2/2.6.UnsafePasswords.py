from random import *

print("Tässä on kaksi erittäin epäturvallista salasanaa. \nÄlä käytä näitä oikeasti, koska en ole vastussa.")

def random3():
    return randint(0,9)

def random4():
    return randint(1,6)

print(f"3 number code: {random3()}{random3()}{random3()}")
print(f"4 number code: {random4()}{random4()}{random4()}{random4()}")
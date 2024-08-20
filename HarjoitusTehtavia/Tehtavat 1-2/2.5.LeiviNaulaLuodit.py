from decimal import *
from math import *

leivit = float(input("Anna Leiviskät:"))
naulat = float(input("Anna Naulat:"))
luodit = float(input("Anna Luodit:"))

grammat = float(0)
grammat += float(luodit*13.3)
grammat += float(naulat*(32*13.3))
grammat += float(leivit*(20*32*13.3))
kilograms = int(grammat/1000)
grammat -= float(kilograms*1000)

print("Massa nykymittojen mukaan:")
print(f"{kilograms} kilogrammaa ja {round(grammat,2)} grammaa.")
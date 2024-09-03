import random

nopat = int(input("Montako noppaa heitetään: "))

summa = 0
for i in range(nopat):
    summa += random.randint(1,6)
    print(summa)

print(f"Noppien summa: {summa}")
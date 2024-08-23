import random

kokomaara = int(input("Anna pisteiden kokomäärä: "))

i = 0
pisteitaYmpyrassa = 0
likiarvo: float = 0

while i<kokomaara:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    print(f"{round(i/kokomaara*100,2)}%, {i}, {x}, {y}")
    if x**2+y**2<1:
        pisteitaYmpyrassa += 1
    i += 1
likiarvo = 4*pisteitaYmpyrassa/kokomaara

print(likiarvo)
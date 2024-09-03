import random
def noppa(koko):
    return random.randint(1,koko)

suurinKoko = int(input("Anna nopan maksimi koko: "))

heitto = 0
while heitto != suurinKoko:
    heitto = noppa(suurinKoko)
    print(f"Noppa heitti {heitto}")
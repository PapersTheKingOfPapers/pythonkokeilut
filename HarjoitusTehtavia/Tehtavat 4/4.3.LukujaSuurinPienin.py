suurin = 1
pienin = 0

numero = input("Anna ensimmäinen numero tai lopeta painamalla Enter: ")
if(int(numero) >= suurin):
    suurin = int(numero)
    pienin = suurin

while numero!="":
    if(int(numero) >= suurin): suurin = int(numero)
    elif(int(numero) <= pienin): pienin = int(numero)
    numero = input("Anna seuraava numero tai lopeta painamalla Enter: ")
print(f"Suurin numero: {suurin}, pienin numero: {pienin}")
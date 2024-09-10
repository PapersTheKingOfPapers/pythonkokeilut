nimet = set()

while True:
    syotto = input("Kerro minulle nimi, tyhjä vastaus lopettaa:  ")
    if syotto == "":
        break
    if syotto in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
    nimet.add(syotto)

for i in nimet:
    print(i)
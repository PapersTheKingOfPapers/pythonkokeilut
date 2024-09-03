arvo = 0
numberslist = []
while True:
    syotto = input("Anna numero: ")
    if syotto == "":
        break
    arvo = float(syotto)
    numberslist.append(arvo)

numberslist.sort(reverse=True)
print(numberslist[:5])
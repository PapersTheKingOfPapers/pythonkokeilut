kaudet = ("Kevät", "Kesä", "Syksy", "Talvi")

kuukausi = int(input("Anna kuukausi numerona (1-12): "))

if kuukausi in range(3,6):
    print(kaudet[0])
elif kuukausi in range(6,9):
    print(kaudet[1])
elif kuukausi in range(9,12):
    print(kaudet[2])
elif kuukausi in [1,2,12]:
    print(kaudet[3])
else:
    print("Ei ole kuukausi.")
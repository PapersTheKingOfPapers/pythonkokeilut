luku = int(input("Anna Luku: "))

if luku == 0 or luku == 1:
    print(f"Luku {luku} ei ole alkuluku.")
elif luku > 1:
    for i in range(2,luku):
        if luku % i == 0:
            print(f"Luku {luku} ei ole alkuluku.")
            print(f"{i} kertaa {luku//i} on {luku}.")
            break
    else:
        print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")
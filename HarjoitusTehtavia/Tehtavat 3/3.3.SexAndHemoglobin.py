sex = input("Mikä on sinun biologinen sukupuoli? (F/M): ")
hemo = int(input("Mikä on sinun hemoglobiiniarvo? : "))

if(sex == "M"):
    if(hemo < 134):
        print("Sinulla on, MATALA, Hemoglobiiniarvo.")
    elif(hemo >=134 and hemo <= 195):
        print("Sinulla on, NORMAALI, Hemoglobiiniarvo.")
    else:
        print("Sinulla on, KORKEA, Hemoglobiiniarvo.")
elif(sex == "F"):
    if(hemo < 117):
        print("Sinulla on, MATALA, Hemoglobiiniarvo.")
    elif(hemo >=117 and hemo <= 175):
        print("Sinulla on, NORMAALI, Hemoglobiiniarvo.")
    else:
        print("Sinulla on, KORKEA, Hemoglobiiniarvo.")
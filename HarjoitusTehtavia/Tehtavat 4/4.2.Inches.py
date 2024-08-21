komento = float(input ("Anna tuuma, negatiivinen lopettaa: "))
while komento >= 0:
    print (f"{komento} tuumaa on {round(komento*2.54,2)} senttimetriä ")
    komento = float(input ("Anna tuuma, negatiivinen lopettaa: "))
print ("Toiminnot lopetettu.")
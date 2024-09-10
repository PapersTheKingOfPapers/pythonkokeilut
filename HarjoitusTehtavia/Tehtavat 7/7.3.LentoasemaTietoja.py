lentoasemat = {"ABCD":"test airport", "EFGH":"test airport2"}

def uusiAsema():
    icao = input("Syötä uuden lentoaseman ICAO koodi: ")
    nimi = input("Syötä uuden lentoaseman nimi: ")
    lentoasemat[icao] = nimi
    return
def haeAsema():
    icao = input("Syötä lentoaseman ICAO koodi: ")
    print(f"{icao}, {lentoasemat[icao]}")
    return

while True:
    valinta = int(input("Haluatko syöttää uuden lentoaseman tiedot (1), \n"
                        "hakea syötetyn lentoaseman tiedot (2), \n"
                        "vai lopettaa (0)? "))
    if valinta == 1:
        uusiAsema()
    elif valinta == 2:
        haeAsema()
    else:
        break
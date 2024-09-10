import SQLconnector
import geopy.distance

def hae_lentoasema_icao_koodilla(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao}'"
    print(sql)
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    if cursor.rowcount > 0:
        for rivi in tulos:
            return (rivi[0], rivi[1])

yhteys = SQLconnector.sqlConnector()

syotto = input("Syötä lentoaseman ICAO koodi: ")
port1 = hae_lentoasema_icao_koodilla(syotto)
syotto = input("Syötä toisen lentoaseman ICAO koodi: ")
port2 = hae_lentoasema_icao_koodilla(syotto)

print(port1)
print(port2)

print(f"{geopy.distance.distance(port1,port2)}")
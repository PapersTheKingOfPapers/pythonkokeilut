import SQLconnector

def hae_lentoasema_icao_koodilla(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
    print(sql)
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    if cursor.rowcount > 0:
        for rivi in tulos:
            print(f"{rivi[0]}, {rivi[1]}")
    return

yhteys = SQLconnector.sqlConnector()

syotto = input("Syötä lentoaseman ICAO koodi: ")
hae_lentoasema_icao_koodilla(syotto)
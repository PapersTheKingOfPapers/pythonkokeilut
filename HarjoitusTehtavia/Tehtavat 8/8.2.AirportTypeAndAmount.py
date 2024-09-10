import SQLconnector

def hae_lentoasema_maa_koodilla(maa):
    sql = f"SELECT type, count(*) FROM airport WHERE iso_country='{maa}' GROUP BY type ORDER BY count(*) DESC;"
    print(sql)
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    if cursor.rowcount > 0:
        for rivi in tulos:
            print(f"{rivi[0]}, {rivi[1]}")
    return

yhteys = SQLconnector.sqlConnector()

syotto = input("Syötä lentoaseman maa koodi: ")
hae_lentoasema_maa_koodilla(syotto)
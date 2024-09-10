import mysql.connector

def sqlConnector():
    yhteys = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='pythonscript',
        password='p47h0n',
        autocommit=True
    )
    return yhteys
from flask import Flask
from flask import request
from database import Database

app = Flask(__name__)
@app.route('/kentta/<ICAO>')
def kentta(ICAO):
    db = Database()
    icao_code = ICAO # http://127.0.0.1:3000/kentta/ICAO
    data = db.get_airport(icao_code)
    airport_name = data['name']
    airport_municipality = data['municipality']

    response = {
        "ICAO": icao_code,
        "Name": airport_name,
        "Municipality": airport_municipality
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000) #'localhost' == 127.0.0.1
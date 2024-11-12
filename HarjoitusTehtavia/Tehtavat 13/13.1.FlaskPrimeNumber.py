from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/primeNumber/<testnumber>')
def primeNumber(testnumber):
    luku = int(testnumber) # http://127.0.0.1:3000/primeNumber/31
    isprime = False

    if luku == 0 or luku == 1:
        isprime = False
    elif luku > 1:
        for i in range(2, luku):
            if luku % i == 0:
                isprime = False
                break
        else:
            isprime = True
    else:
        isprime = False

    response = {
        "Number": luku,
        "isPrime": isprime
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000) #'localhost' == 127.0.0.1
import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')

def Funcao_Fibo():
    anterior = 0
    proximo = 0
    fibo = ""
    contfibo = 1

    while(contfibo < 50):
        proximo = proximo + anterior
        anterior = proximo - anterior
        fibo = fibo + str(proximo) + "<br>"
        contfibo = contfibo + 1
        if(proximo == 0):
            proximo = proximo + 1

    return fibo

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
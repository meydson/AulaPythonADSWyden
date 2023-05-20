from flask import Flask

app = Flask(__name__)

@app.route('/ola')
def ola_mundo():
    return "Olá,mundo"

@app.route('/ola')
def ola_mundo2(nome="mundo2"):
    return "Olá, " + nome

if __name__ == '__main__':
    app.run()
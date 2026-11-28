from flask import Flask

app = Flask(__name__)


def addition(a, b):
    return a + b


def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b


@app.route("/")
def accueil():
    return "Bonjour depuis ma pipeline automatisée !"


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return {"resultat": addition(a, b)}


@app.route("/version")
def version():
    return {"version": "2.0"}


if __name__ == "__main__":  # pragma: no cover
    app.run(port=8080)


def fonction_test(x):
    return x * 2

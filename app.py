from flask import Flask

app = Flask(__name__)


def addition(a, b):
    return a + b


@app.route("/")
def accueil():
    return "Bonjour depuis la pipeline Jenkins + Docker !"


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return {"resultat": addition(a, b)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


@app.route("/version")
def version():
    return {"version": "2.0"}


def fonction_non_testee(x):
    return x * 2

from app import app, addition


def test_addition():
    assert addition(2, 3) == 5


def test_accueil():
    client = app.test_client()
    assert client.get("/").status_code == 200


def test_route_add():
    client = app.test_client()
    assert client.get("/add/4/6").get_json() == {"resultat": 10}

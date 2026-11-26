import pytest
from app import app, addition, division


def test_addition():
    assert addition(2, 3) == 5


def test_division():
    assert division(10, 2) == 5


def test_division_par_zero():
    with pytest.raises(ValueError):
        division(1, 0)


def test_accueil():
    client = app.test_client()
    assert client.get("/").status_code == 200


def test_route_add():
    client = app.test_client()
    assert client.get("/add/4/6").get_json() == {"resultat": 10}


def test_route_version():
    client = app.test_client()
    assert client.get("/version").get_json() == {"version": "2.0"}

import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_hello(client):
    res = client.get("/hello")
    assert res.status_code == 200
    assert res.json["msg"] == "Hello Flask CI/CD!"

def test_add(client):
    res = client.get("/add/2/3")
    assert res.status_code == 200
    assert res.json["result"] == 5

def test_workflow(client):
    res1 = client.get("/hello")
    assert res1.status_code == 200
    res2 = client.get("/add/10/20")
    assert res2.status_code == 200
    assert res2.json["result"] == 30
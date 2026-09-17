from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["service"] == "sre-incident-simulator"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_orders():
    response = client.get("/api/orders")

    assert response.status_code == 200
    assert "orders" in response.json()


def test_metrics():
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "api_requests_total" in response.text
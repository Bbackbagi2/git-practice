# tests/test_api.py — HTTP 요청 없이 TestClient로 API 동작 확인
import pytest
from fastapi.testclient import TestClient

from orderlab.api import create_app


@pytest.fixture
def client():
    # 테스트마다 새 앱 생성 → 주문 상태가 서로 섞이지 않음
    with TestClient(create_app()) as test_client:
        yield test_client


def test_create_and_get(client):
    # 주문 생성 201과 조회 200, 양쪽 JSON 본문 확인
    response = client.post("/orders", json={"price": 10000, "quantity": 2})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "subtotal": 20000}
    response = client.get("/orders/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "subtotal": 20000}


def test_invalid_quantity(client):
    # 수량 0은 입력 규칙 위반이므로 422
    response = client.post("/orders", json={"price": 100, "quantity": 0})
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "quantity"]


def test_invalid_price(client):
    # 음수 가격도 입력 검증 실패
    response = client.post("/orders", json={"price": -1, "quantity": 1})
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "price"]


def test_not_found(client):
    # 없는 주문은 404와 오류 JSON을 반환
    response = client.get("/orders/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found"}


def test_each_client_starts_empty(client):
    # 다른 테스트에서 생성한 주문이 현재 앱에 남지 않음
    assert client.get("/orders/1").status_code == 404

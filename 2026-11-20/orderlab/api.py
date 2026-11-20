# orderlab/api.py — 주문 입력 규칙과 FastAPI 앱 팩토리
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from orderlab.pricing import subtotal


class OrderIn(BaseModel):
    # 가격은 0 이상, 수량은 0보다 커야 함
    price: int = Field(ge=0)
    quantity: int = Field(gt=0)


def create_app() -> FastAPI:
    # 호출할 때마다 새 앱과 주문 저장소 생성 → 테스트 간 상태 분리
    app = FastAPI()
    store: dict[int, int] = {}

    @app.post("/orders", status_code=201)
    def create_order(data: OrderIn):
        # 주문 번호를 만들고 가격 × 수량을 저장
        order_id = len(store) + 1
        store[order_id] = subtotal(data.price, data.quantity)
        return {"id": order_id, "subtotal": store[order_id]}

    @app.get("/orders/{order_id}")
    def get_order(order_id: int):
        # 없는 주문은 404로 응답
        if order_id not in store:
            raise HTTPException(status_code=404, detail="Not found")
        return {"id": order_id, "subtotal": store[order_id]}

    return app

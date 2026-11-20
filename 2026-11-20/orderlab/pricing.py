# orderlab/pricing.py — 상품 금액과 최종 주문 금액 계산


def subtotal(unit_price: int, quantity: int) -> int:
    # 가격과 수량은 0을 허용하고 음수는 거부
    if unit_price < 0 or quantity < 0:
        raise ValueError("negative input")
    # 단가 × 수량을 정수 금액으로 반환
    return unit_price * quantity


def final_total(price: int, qty: int, discount: int) -> int:
    # 할인율은 0~100%만 허용
    if not 0 <= discount <= 100:
        raise ValueError("invalid discount")

    # 상품 금액을 계산하고 할인액을 정수로 구해 차감
    amount = subtotal(price, qty)
    amount -= amount * discount // 100

    # 할인 후 금액이 0원 초과 50,000원 미만이면 배송비 3,000원
    shipping = 3_000 if 0 < amount < 50_000 else 0
    return amount + shipping

import pytest

from orderlab.pricing import subtotal


def test_subtotal_normal():
    # T1 · 준비: 가격 10,000원과 수량 2개 설정
    price = 10_000
    quantity = 2

    # 실행: subtotal을 호출하고 반환값을 result에 저장
    result = subtotal(price, quantity)

    # 검증: 반환값이 기대값 20,000원과 같으면 통과
    assert result == 20_000


def test_subtotal_zero():
    # T2: 가격 0원과 수량 3개로 subtotal 호출
    # 반환값이 기대값 0과 같으면 테스트 통과
    assert subtotal(0, 3) == 0


def test_subtotal_negative():
    # T3: 아래 코드에서 ValueError가 발생해야 테스트 통과
    with pytest.raises(ValueError):
        # 음수 가격 -100원과 수량 2개로 subtotal 호출
        subtotal(-100, 2)

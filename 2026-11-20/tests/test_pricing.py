# tests/test_pricing.py — 정상·경계·예외 테스트
import pytest

from orderlab.pricing import final_total, subtotal


def test_subtotal_normal():
    # T1 · Arrange(준비): 가격 10,000원과 수량 2개 설정
    price = 10_000
    quantity = 2

    # Act(실행): subtotal을 호출하고 반환값을 result에 저장
    result = subtotal(price, quantity)

    # Assert(검증): 반환값이 기대값 20,000원과 같으면 통과
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


# parametrize: 같은 검증을 다섯 입력과 기대값으로 각각 실행
@pytest.mark.parametrize(
    "price, qty, discount, expected",
    [
        (10_000, 2, 0, 23_000),  # 배송비 추가
        (49_999, 1, 0, 52_999),  # 무료 배송 기준 바로 아래
        (50_000, 1, 0, 50_000),  # 무료 배송 기준
        (50_001, 1, 0, 50_001),  # 무료 배송 기준 바로 위
        (10_000, 2, 10, 21_000),  # 할인 후 배송비 추가
    ],
)
def test_final_total(price, qty, discount, expected):
    # 입력별 실제 최종금액과 기대값 비교
    assert final_total(price, qty, discount) == expected


def test_discount_below_zero():
    # 할인율 -1%는 허용 범위 밖이므로 ValueError 발생
    with pytest.raises(ValueError):
        final_total(10_000, 2, -1)


def test_discount_over_100():
    # 할인율 101%에서 예외와 오류 메시지를 함께 확인
    with pytest.raises(ValueError, match="invalid discount"):
        final_total(10_000, 2, 101)

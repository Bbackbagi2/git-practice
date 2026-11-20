# tests/test_csv_report.py — 임시 파일과 fixture를 이용한 CSV 검증
from orderlab.csv_report import revenue_from_csv


def test_csv_revenue(tmp_path):
    # 테스트 전용 임시 폴더에 주문 데이터 작성
    csv_file = tmp_path / "orders.csv"
    csv_file.write_text(
        "price,quantity\n10000,2\n5000,3\n",
        encoding="utf-8",
    )
    # 10,000 × 2 + 5,000 × 3 = 35,000원
    assert revenue_from_csv(csv_file) == 35_000


def test_csv_empty(tmp_path):
    # 헤더만 있고 주문 행이 없는 CSV 생성
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("price,quantity\n", encoding="utf-8")
    # 합산할 주문이 없으므로 매출은 0원
    assert revenue_from_csv(csv_file) == 0


def test_fixture_revenue(sample_csv):
    # pytest가 sample_csv fixture의 반환값을 인자로 전달
    assert revenue_from_csv(sample_csv) == 35_000

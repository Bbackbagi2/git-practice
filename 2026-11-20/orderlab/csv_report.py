# orderlab/csv_report.py — CSV 주문 데이터 매출 집계
import csv
from pathlib import Path


def revenue_from_csv(path: str | Path) -> int:
    # path는 문자열 또는 Path 객체; 숫자 변환 오류는 ValueError
    # CSV의 첫 행을 열 이름으로 사용해 각 주문 행을 읽음
    with open(path, encoding="utf-8", newline="") as f:
        rows = csv.DictReader(f)
        # 각 행의 가격 × 수량을 정수로 계산해 모두 더함
        return sum(int(row["price"]) * int(row["quantity"]) for row in rows)

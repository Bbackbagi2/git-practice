# generate_report.py — 샘플 매출을 정적 HTML 보고서로 생성
from pathlib import Path

from orderlab.csv_report import revenue_from_csv


def main():
    # 프로젝트 폴더에서 샘플 데이터를 읽어 site/index.html 생성
    revenue = revenue_from_csv("data/sample_orders.csv")
    site = Path("site")
    site.mkdir(exist_ok=True)
    (site / "index.html").write_text(
        f"<h1>OrderLab Report</h1><p>Revenue: {revenue:,} KRW</p>",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

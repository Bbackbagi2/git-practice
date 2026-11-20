# 보고서 생성 결과를 독립된 임시 폴더에서 검증
from generate_report import main


def test_generate_report(tmp_path, monkeypatch):
    # 임시 샘플 CSV를 준비하고 작업 폴더를 분리
    data = tmp_path / "data"
    data.mkdir()
    (data / "sample_orders.csv").write_text(
        "price,quantity\n10000,2\n5000,3\n", encoding="utf-8"
    )
    monkeypatch.chdir(tmp_path)

    # HTML이 생성되고 실제 매출이 보고서에 포함되는지 확인
    main()
    html = (tmp_path / "site" / "index.html").read_text(encoding="utf-8")
    assert "OrderLab Report" in html
    assert "Revenue: 35,000 KRW" in html

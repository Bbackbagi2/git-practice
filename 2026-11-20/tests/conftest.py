# tests/conftest.py — 같은 폴더와 하위 테스트에서 쓰는 fixture
import pytest


@pytest.fixture  # 기본 범위: 테스트 함수마다 한 번
def sample_csv(tmp_path):
    # 테스트마다 독립된 임시 폴더에 공통 주문 CSV 준비
    path = tmp_path / "sample.csv"
    path.write_text(
        "price,quantity\n10000,2\n5000,3\n",
        encoding="utf-8",
    )
    # fixture를 요청한 테스트에 파일 경로 전달
    return path

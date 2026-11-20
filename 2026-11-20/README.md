# 2026-11-20 Python CI/CD 실습

강의 자료 Level 1–5: 가격 계산, CSV, API와 CI/CD 실습.

```bash
cd 2026-11-20
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest --rootdir=/private/tmp tests/test_pricing.py tests/test_csv_report.py tests/test_api.py tests/test_report.py -q
ruff check .
ruff format --check .
```

명령은 git-practice 폴더에서 시작하는 기준이다. GitHub Actions 워크플로는 저장소 루트의 `.github/workflows/orderlab-ci.yml`에 있다.

위 pytest 명령은 이 Mac의 경로에 대괄호가 있어 기본 실행이 오류를 내는 상황을 피한다. GitHub Actions 등 일반 경로에서는 `python -m pytest -q`를 사용할 수 있다.

## Level 3–5

- CSV 정상·빈 파일·없는 파일·숫자 오류를 pytest로 확인한다.
- FastAPI 주문 생성·조회와 입력 오류를 `TestClient`로 검사한다.
- `python generate_report.py`는 `data/sample_orders.csv`를 읽어
  `site/index.html`을 생성한다.
- GitHub Actions는 push마다 Ruff와 Ubuntu/Windows 테스트를 실행하고,
  main push에서 모든 검사가 통과하면 정적 보고서를 Pages에 배포한다.
- 각 테스트 job은 `coverage.xml`을 운영체제별 artifact로 저장한다.

# 2026-11-20 Python CI/CD 실습

강의 자료 Level 1: 가격 × 수량 계산과 테스트.

```bash
cd 2026-11-20
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest --rootdir=/private/tmp tests/test_pricing.py -q
ruff check .
ruff format --check .
```

명령은 git-practice 폴더에서 시작하는 기준이다. GitHub Actions 워크플로는 저장소 루트의 `.github/workflows/`에 두어야 하므로 수업 진행 및 저장소 사용 방침을 확인한 뒤 추가한다.

현재 경로에 대괄호가 있어 pytest 기본 실행이 오류를 내므로 위처럼 rootdir과 테스트 파일을 지정한다.

# 🚗 CarBTI — 나의 성향으로 찾는 인생 차량

> "나에게 꼭 맞는 차는 뭘까?" MBTI처럼 몇 가지 질문에 답하면, 성향 유형을 계산해 어울리는 차량을 추천해주는 Streamlit 웹 애플리케이션입니다.

<p> <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Streamlit-1.60+-FF4B4B?logo=streamlit&logoColor=white"> <img src="https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/uv-package%20manager-DE5FE9"> <img src="https://img.shields.io/badge/Selenium-crawling-43B02A?logo=selenium&logoColor=white"> </p>

---

## 📌 서비스명

**CarBTI** (Car + MBTI) — 자동차 성향 검사 & 맞춤 차량 추천 서비스

## 📖 프로젝트 개요

운전 스타일, 차량에서 중요하게 생각하는 가치, 신기술에 대한 태도 등을 묻는 문항에 답하면 E/I, S/N 등의 축으로 점수를 합산해 나만의 **차 유형**을 도출합니다. 이후 크롤링으로 수집한 실제 차량 데이터베이스에서 해당 유형과 가장 잘 맞는 차량을 순위별로 추천하고, 차량 상세 정보(트림, 가격, 연비, 옵션 등)까지 확인할 수 있습니다.

- 🧭 성향 검사 → 결과 유형 계산 → 맞춤 차량 추천 → 차량 상세 정보까지 이어지는 원스톱 플로우
- 🕷️ 자체 크롤러로 제조사, 차량, 옵션, 판매 통계, 관련 뉴스 데이터를 수집해 DB에 적재
- 🗄️ 결과 유형/설명은 하드코딩이 아닌 DB(`car_mbti` 테이블) 조회로 관리해 콘텐츠 수정이 쉬움

## 👥 팀원

|  | 팀원 1 | 팀원 2 | 팀원 3 | 팀원 4 | 팀원 5 |
| --- | --- | --- | --- | --- | --- |
<<<<<<< HEAD
| 이름 | _조현주_ | _고태민_ | _권준호_ | _장인화_ | _정진봉_ |
| 역할 | _(예: 팀장 / DB 설계)_ | _(예: 크롤링)_ | _(예: 프론트엔드)_ | _(예: 백엔드)_ | _(예: 데이터 분석)_ |
| GitHub | [@](https://github.com/) | [@taemin1997](https://github.com/taemin1997) | [@Junho7-Kweon](https://github.com/Junho7-Kweon) | [@](https://github.com/) | [@](https://github.com/) |
=======
| 사진 | <img src="./images/레드.png" width="80"> | <img src="./images/블루.png" width="80"> | <img src="./images/그린.png" width="80"> | <img src="./images/옐로.png" width="80"> | <img src="./images/핑크.png" width="80"> |
| 이름 | _조현주_ | _고태민_ | _권준호_ | _장인화_ | _정진봉_ |
| 역할 | _(팀장 및 크롤링)_ | _(크롤링 및 DB 설계)_ | _(크롤링 및 화면서브 )_ | _(질문 설계 및 화면)_ | _(질문 설계 및 화면)_ |
| GitHub | [@zozuzu](https://github.com/zozuzu) | [@taemin1997](https://github.com/taemin1997) | [@Junho7-Kweon](https://github.com/Junho7-Kweon) | [@inaskn35 ](https://github.com/) | [@rupria](https://github.com/) |
>>>>>>> f0dd90426a6075b7ba4964e8a481a3489a77be64

> ✏️ 실제 팀원 정보로 표를 채워주세요.

## 🛠️ 기술 스택

| 분류 | 기술 |
| --- | --- |
| Language | ![Python](https://img.shields.io/badge/Python%203.12-3776AB?logo=python&logoColor=white) |
| Frontend / App | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) |
| Database | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white) ![PyMySQL](https://img.shields.io/badge/PyMySQL-4479A1?logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white) |
| Crawling | ![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=white) ![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-4B8BBE?logoColor=white) ![Requests](https://img.shields.io/badge/Requests-2E7D32?logoColor=white) |
| Data Handling | ![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white) |
| 환경/패키지 관리 | ![uv](https://img.shields.io/badge/uv-DE5FE9?logoColor=white) ![python-dotenv](https://img.shields.io/badge/python--dotenv-ECD53F?logoColor=black) |
| 개발 워크플로우 | ![Jupyter](https://img.shields.io/badge/Jupyter%20Notebook-F37626?logo=jupyter&logoColor=white) |
| 테스트 | ![unittest](https://img.shields.io/badge/unittest-3776AB?logo=python&logoColor=white) |

## 🧩 핵심 기술

- **성향 계산 로직**: 문항별 선택지에 부여된 점수(E/I, S/N 등)를 합산해 거리 기반으로 결과 유형을 산출
- **DB 스키마 자동 보장**: 앱 최초 구동 시 `ensure_schema()`로 스키마를 자동 점검·생성 (`@st.cache_resource`로 1회만 실행)
- **노트북 기반 단일 소스 관리**: `streamlit_set.ipynb`의 단일 셀이 `app.py`를 생성하는 소스 오브 트루스 역할
- **크롤링 파이프라인**: 제조사 → 차량 → 상세/옵션 → 판매통계 → 뉴스 순으로 수집기를 분리해 유지보수 용이

## 🗂️ Project Structure

```text
mini_project1/
├── app.py                     # Streamlit 메인 애플리케이션 (질문/결과/상세 페이지 라우팅)
├── main.py                    # 진입점 스크립트
├── streamlit_set.ipynb        # app.py를 생성하는 개발용 노트북 (단일 소스)
├── pyproject.toml / uv.lock   # 의존성 및 실행 환경 정의
├── crawling/
│   ├── db_config.py           # DB 커넥션 및 스키마 보장
│   ├── manufacturer_crawler.py
│   ├── vehicle_crawler.py
│   ├── vehicle_detail_crawler.py
│   ├── option_crawler.py
│   ├── car_mbti_crawler.py
│   ├── car_recommend_crawler.py
│   ├── sales_stats_crawler.py
│   └── news_crawler.py
├── db/
│   └── carbti_schema.sql      # 전체 테이블 DDL
├── data/raw/                  # 크롤링 원본 데이터 (JSON)
├── .streamlit/
│   └── secrets.toml.example   # DB 접속정보 예시
├── scripts/
│   └── check_environment.py   # 환경 점검 스크립트
└── tests/
    └── test_app_structure.py
```

## 🗄️ ERD

<<<<<<< HEAD
![CARbti ERD](./CARbti_ERD.png)
=======
![CARbti ERD](./images/CARbti_ERD.png)
>>>>>>> f0dd90426a6075b7ba4964e8a481a3489a77be64

`car_mbti`(성향 유형) — `car_recommend` — `vehicle` — `vehicle_detail` — `vehicle_option` — `option` 이 서로 연결되고, `vehicle`은 `manufacturer`, `news`, `sales_stat`과도 연관됩니다.

<details>
<summary>텍스트로 보는 테이블 관계 요약</summary>

```text
manufacturer 1─N vehicle 1─N vehicle_detail N─N option (via vehicle_option)
vehicle      1─N news
vehicle      1─N sales_stat
car_mbti     1─N car_recommend N─1 vehicle
```

</details>

## 🖥️ 구현 화면

| 시작 화면 | 질문 화면 | 결과 & 추천 화면 | 차량 상세 화면 |
| --- | --- | --- | --- |
| _(스크린샷)_ | _(스크린샷)_ | _(스크린샷)_ | _(스크린샷)_ |

## ⚙️ 실행 방법

필요한 도구: `Git`, [`uv`](https://docs.astral.sh/uv/)

```bash
git clone <저장소-주소>
cd SKN35-1st-3Team
uv sync --frozen
uv run python scripts/check_environment.py
uv run python -m unittest discover -s tests -v
uv run streamlit run app.py
```

### DB 종류별 설치

```bash
uv sync --frozen --extra mysql      # MySQL 
uv sync --frozen                    # SQLite (기본)
```

### DB 접속 설정

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

`.streamlit/secrets.toml`을 열어 실제 접속 정보로 수정합니다.

```toml
[connections.car_mbti]
url = "mysql+pymysql://username:password@host:3306/database"
```

> 🔒 실제 비밀번호가 담긴 `.streamlit/secrets.toml`, `.env`, `.venv/`는 Git에 커밋하지 않습니다.

## 📝 특이사항

- `.venv`는 PC마다 새로 생성하며 공유하지 않습니다. `uv`가 `.python-version` / `pyproject.toml` 기준으로 Python 3.12 환경을 자동 구성합니다.
- 노트북(`streamlit_set.ipynb`)을 고치면 반드시 셀을 실행해 `app.py`를 갱신한 뒤, 두 파일을 함께 커밋합니다.
- `app.py`의 `RESULT_PROFILES`에 정의된 `mbti_id`는 DB `car_mbti.mbti_id`와 반드시 일치해야 합니다.

## 🔗 관련 이슈 / 개선 내역

<<<<<<< HEAD
- [ ] _(이슈/개선 사항을 입력해주세요)_
=======
- [ ] _(이슈/개선 사항을 입력해주세요)_
>>>>>>> f0dd90426a6075b7ba4964e8a481a3489a77be64

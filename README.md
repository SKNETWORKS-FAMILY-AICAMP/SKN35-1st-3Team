# 🚗 CarBTI — 나의 성향으로 찾는 인생 차량

> "나에게 꼭 맞는 차는 뭘까?" MBTI처럼 몇 가지 질문에 답하면, 성향 유형을 계산해 어울리는 차량을 추천해주는 Streamlit 웹 애플리케이션입니다.

<p> <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Streamlit-1.60+-FF4B4B?logo=streamlit&logoColor=white"> <img src="https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/uv-package%20manager-DE5FE9"> <img src="https://img.shields.io/badge/Selenium-crawling-43B02A?logo=selenium&logoColor=white"> </p>

---

## 📌 서비스명

**CarBTI** (Car + MBTI) — 자동차 성향 검사 & 맞춤 차량 추천 서비스

[CarBTI](https://skn35-1st-3team-nnrf48gks6yzw4qemidzdq.streamlit.app/) 

## 📖 프로젝트 개요

운전 스타일, 차량에서 중요하게 생각하는 가치, 신기술에 대한 태도 등을 묻는 문항에 답하면 E/I, S/N 등의 축으로 점수를 합산해 나만의 **차 유형**을 도출합니다. 이후 크롤링으로 수집한 실제 차량 데이터베이스에서 해당 유형과 가장 잘 맞는 차량을 순위별로 추천하고, 차량 상세 정보(트림, 가격, 연비, 옵션 등)까지 확인할 수 있습니다.

- 🧭 성향 검사 → 결과 유형 계산 → 맞춤 차량 추천 → 차량 상세 정보까지 이어지는 원스톱 플로우
- 🕷️ 자체 크롤러로 제조사, 차량, 옵션, 판매 통계, 관련 뉴스 데이터를 수집해 DB에 적재
- 🗄️ 결과 유형/설명은 하드코딩이 아닌 DB(`car_mbti` 테이블) 조회로 관리해 콘텐츠 수정이 쉬움

## 👥 팀원

|  | 팀원 1 | 팀원 2 | 팀원 3 | 팀원 4 | 팀원 5 |
| --- | --- | --- | --- | --- | --- |
| 사진 | <img src="./images/레드.png" width="80"> | <img src="./images/블루.png" width="80"> | <img src="./images/그린.png" width="80"> | <img src="./images/옐로.png" width="80"> | <img src="./images/핑크.png" width="80"> |
| 이름 | _조현주_ | _고태민_ | _권준호_ | _장인화_ | _정진봉_ |
| 역할 | _(팀장 및 크롤링)_ | _(크롤링 및 DB 설계)_ | _(크롤링 및 화면서브 )_ | _(질문 설계 및 화면)_ | _(질문 설계 및 화면)_ |
| GitHub | [@zozuzu](https://github.com/zozuzu) | [@taemin1997](https://github.com/taemin1997) | [@Junho7-Kweon](https://github.com/Junho7-Kweon) | [@inaskn35 ](https://github.com/) | [@rupria](https://github.com/) |

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

![CARbti ERD](./images/CARbti_ERD.png)

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

[구현 동영상](https://drive.google.com/file/d/1-kQiLjVrv7RRMOlCnmR6H04EjQco6Ape/view?usp=sharing)

## ⚙️ 실행 방법

필요한 도구: `Git`, `uv`

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

## ⚠️ 한계점 및 트러블슈팅

| 환경 세팅 통일 | 크롤링 차단 대응 | 데이터 정밀도 |
| --- | --- | --- |
| 🎯 초기 설정 불일치 이슈 | 🛡️ robots.txt 및 동적 렌더링 한계 | 📊 실거래가 연동 고도화 필요 |

- **환경 세팅 통일**: 팀원별 로컬 Python/패키지 버전이 달라 초기 설정 단계에서 불일치가 발생했습니다. `uv`와 `pyproject.toml` / `.python-version`으로 환경을 고정해 재현성을 확보하는 방향으로 대응했습니다.
- **크롤링 차단 대응**: 일부 사이트는 `robots.txt`로 자동 수집이 막혀 있거나 동적 렌더링(JS 기반)으로 인해 단순 요청 크롤링으로는 데이터 수집이 어려웠습니다. 해당 구간은 Selenium 기반 크롤링 또는 수동 확인 후 시드 데이터 입력 방식으로 우회했습니다.
- **데이터 정밀도**: 현재 가격/시세 데이터는 공식 발표 자료 기반이라 실거래가와는 차이가 있을 수 있습니다. 추후 실거래가 API/데이터 연동을 통한 고도화가 필요합니다.

## 🔗 앞으로의 개선 내역

- [ ] **실거래가 데이터 연동**: 현재 비어있는 `sales_avg_price` 등 시세 정보를 실거래가 API/데이터와 연동해 정밀도 향상
- [ ] **외부 거래 사이트 연동 방향 확정**: 추천 차량 클릭 시 외부 신차/중고차 거래 사이트로 연결하는 기능의 신차/중고 구분 방식 재검토 및 확정
- [ ] **크롤링 자동화 범위 확대**: robots.txt 및 동적 렌더링으로 막혀 있던 구간(판매 통계 등)의 수집 자동화 검토

## 🙋 팀원 회고

**조현주**
> 35기 1차 프로젝트인 만큼 팀원들과 더 끈끈해지고 이야기도 많이 나누며 진행했습니다. 앞으로 6개월을 함께할 동기들과의 첫 프로젝트 경험이라 더 오래 기억에 남을 것 같습니다. 각자 강점에 맞게 역할을 나눈 덕분에 훨씬 수월하게 진행할 수 있었습니다. 3조 팀원 모두 고생 많았습니다!

**고태민**
> 처음 시작하는 프로젝트라 초반에는 막막했지만, 모두가 열심히 해준 덕분에 잘 마무리할 수 있어 다행이라고 생각합니다. 더 넣고 싶은 데이터와 기능이 많았는데 시간이 부족해 다 담지 못한 점이 아쉬웠습니다. 이번 경험을 바탕으로 남은 기간에는 항상 좋은 퀄리티를 지향하도록 하겠습니다.

**권준호**
> 처음으로 크롤링을 맡아 16개 차종의 스펙·뉴스 데이터를 수집하고, 제조사 공식 정보와 대조해 가격 오류 3건을 정정했습니다. DB 제약조건 검증과 클라우드 DB 전환 과정에도 참여했습니다. 처음 다뤄보는 도구가 많아 시행착오는 있었지만, 이를 통해 협업 시 역할과 컨벤션을 사전에 명확히 맞추는 것의 중요성을 배웠습니다.

**장인화**
> 1차 프로젝트라 익숙지 않은 환경설정 문제를 처리하느라 코드 작성에 많이 투입하지 못한 것 같아 아쉽고 팀원들에게 미안한 마음입니다. 그래도 제 나름의 방식으로 와이어프레임을 구성해볼 수 있었고, 그 레이아웃대로 실제 페이지가 구성된 것을 보니 뿌듯했습니다. 많이 알려주고 리드해주신 팀원분들께 감사드립니다.

**정진봉**
> 개발 프로젝트를 처음 진행하면서 설계의 중요성을 알게 되었습니다. 최초 회의 때 환경 세팅에 필요한 체크리스트가 있었다면 좋았을 것 같다는 생각이 들어, 이후 프로젝트에서 활용할 수 있도록 관련 문서를 정리해볼 계획입니다. 낯선 업무가 많았던 만큼 배운 것도 많았습니다.
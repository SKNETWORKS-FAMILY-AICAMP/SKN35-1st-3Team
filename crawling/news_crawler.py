"""
news_crawler.py
- 네이버 뉴스 검색 API로 16대 차량 관련 뉴스를 1건씩 크롤링
- 결과는 ../data/raw/vehicle_news.json 으로 저장

사전 준비:
1. https://developers.naver.com/apps/#/register 에서 애플리케이션 등록
   - 사용 API: "검색" 체크
2. 발급받은 Client ID / Client Secret을 아래 NAVER_CLIENT_ID, NAVER_CLIENT_SECRET에 입력
"""

import requests
import json
import time
import re
import os
from dotenv import load_dotenv

load_dotenv("../.env")

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

VEHICLE_LIST = {
    "ISTJ": "아반떼",
    "ISFJ": "벤츠 E클래스",
    "INFJ": "제네시스 G80",
    "INTJ": "볼보 XC60",
    "ISTP": "포르쉐 카이엔",
    "ISFP": "렉서스 ES",
    "INFP": "폭스바겐 티구안",
    "INTP": "아이오닉5",
    "ESTP": "제네시스 GV70",
    "ESFP": "미니 쿠퍼",
    "ENFP": "기아 레이",
    "ENTP": "테슬라 Model Y",
    "ESTJ": "현대 그랜저",
    "ESFJ": "기아 쏘렌토",
    "ENFJ": "기아 카니발",
    "ENTJ": "BMW 5시리즈",
}


def clean_html(text):
    """네이버 API가 <b>태그로 감싸서 주는 하이라이트/HTML 엔티티 제거"""
    text = re.sub(r"<.*?>", "", text)
    text = text.replace("&quot;", '"').replace("&amp;", "&").replace("&#39;", "'")
    return text.strip()


def get_press_name(url):
    """URL 도메인에서 언론사 이름을 대략 추정 (참고용, 완벽하지 않음)"""
    match = re.search(r"https?://(?:www\.)?([^/]+)", url)
    return match.group(1) if match else ""


def search_news(query):
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
    }
    params = {
        "query": query,
        "display": 5,   # 상위 5개 받아서 그중 1개 선택
        "start": 1,
        "sort": "sim",  # sim: 정확도순, date: 최신순
    }
    res = requests.get(url, headers=headers, params=params, timeout=10)
    res.raise_for_status()
    return res.json()


def crawl_one(persona_code, vehicle_name):
    data = search_news(f"{vehicle_name} 신차")
    items = data.get("items", [])
    if not items:
        return None

    item = items[0]  # 가장 관련도 높은 뉴스 1건만 사용
    news_url = item.get("originallink") or item.get("link")

    return {
        "persona_code": persona_code,
        "vehicle_name": vehicle_name,
        "news_title": clean_html(item["title"]),
        "news_url": news_url,
        "press": get_press_name(news_url),
        "publish_date": item["pubDate"],
        "summary": clean_html(item["description"]),
    }


if __name__ == "__main__":
    if "여기에" in NAVER_CLIENT_ID:
        print("먼저 NAVER_CLIENT_ID / NAVER_CLIENT_SECRET을 채워주세요!")
        exit()

    results = []

    for persona_code, vehicle_name in VEHICLE_LIST.items():
        print(f"검색 중: {vehicle_name} ({persona_code})")
        try:
            data = crawl_one(persona_code, vehicle_name)
            if data:
                print(" ->", data["news_title"])
                results.append(data)
            else:
                print(" -> 검색 결과 없음")
        except Exception as e:
            print(f"[실패] {vehicle_name}: {e}")

        time.sleep(0.5)

    with open("../data/raw/vehicle_news.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n총 {len(results)}건 완료 -> ../data/raw/vehicle_news.json")
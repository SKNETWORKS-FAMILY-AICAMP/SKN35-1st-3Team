"""
vehicle_detail_crawler.py
- carnoon.co.kr에서 16대 대표 차량의 상세 스펙을 크롤링
- 결과는 ../data/raw/vehicle_detail.json 으로 저장
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

VEHICLE_URLS = {
    "ISTJ": ("아반떼",     "https://www.carnoon.co.kr/newcar/vehicle/11414"),
    "ISFJ": ("E클래스",    "https://www.carnoon.co.kr/newcar/vehicle/11651"),
    "INFJ": ("G80",        "https://www.carnoon.co.kr/newcar/vehicle/11644"),
    "INTJ": ("XC60",       "https://www.carnoon.co.kr/newcar/vehicle/11028"),
    "ISTP": ("카이엔",     "https://www.carnoon.co.kr/newcar/vehicle/11544"),
    "ISFP": ("ES",         "https://www.carnoon.co.kr/newcar/vehicle/11026"),
    "INFP": ("티구안",     "https://www.carnoon.co.kr/newcar/vehicle/11020"),
    "INTP": ("아이오닉5",  "https://www.carnoon.co.kr/newcar/vehicle/11664"),
    "ESTP": ("GV70",       "https://www.carnoon.co.kr/newcar/vehicle/10534"),
    "ESFP": ("미니쿠퍼",   "https://www.carnoon.co.kr/newcar/vehicle/11688"),
    "ENFP": ("레이",       "https://www.carnoon.co.kr/newcar/vehicle/11116"),
    "ENTP": ("Model Y",    "https://www.carnoon.co.kr/newcar/vehicle/11738"),
    "ESTJ": ("그랜저",     "https://www.carnoon.co.kr/newcar/vehicle/11874"),
    "ESFJ": ("쏘렌토",     "https://www.carnoon.co.kr/newcar/vehicle/11572"),
    "ENFJ": ("카니발",     "https://www.carnoon.co.kr/newcar/vehicle/11605"),
    "ENTJ": ("5시리즈",    "https://www.carnoon.co.kr/newcar/vehicle/11584"),
}


def extract_spec(soup, label):
    tag = soup.find(string=lambda s: s and s.strip() == label)
    if not tag:
        return None

    parent = tag.parent

    if parent.name == "dt":
        dd = parent.find_next_sibling("dd")
        if dd:
            return dd.get_text(strip=True)

    next_el = parent.find_next_sibling()
    if next_el:
        text = next_el.get_text(strip=True)
        if text:
            return text

    return None


def extract_spec_multi(soup, labels):
    """여러 라벨 후보를 순서대로 시도 (내연기관용/전기차용 라벨이 다를 때 대비)"""
    for label in labels:
        val = extract_spec(soup, label)
        if val:
            return val
    return None


def extract_trim_and_price(soup):
    """
    '스마트 휘발유 15.0㎞/ℓ 20,650,000원' (내연기관) 또는
    'Standard 2WD 전기 5.1㎞/kWh 45,000,000원' (전기차) 패턴에서
    대표 트림명과 시작 가격을 추출.
    - 트림명에 공백이 있는 경우('TDI Premium' 등)도 대응
    - 디젤은 '디젤'/'경유' 둘 다 대응
    """
    text = soup.get_text()

    # 내연기관/하이브리드용 (㎞/ℓ 단위)
    pattern_fuel = r'([가-힣A-Za-z0-9]+(?:\s[가-힣A-Za-z0-9]+){0,2})\s+(휘발유|디젤|경유|LPG|LPi|가솔린)\s+[\d.]+㎞/ℓ\s+([\d,]+)원'
    match = re.search(pattern_fuel, text)
    if match:
        return match.group(1), int(match.group(3).replace(",", ""))

    # 전기차용 (㎞/kWh 단위)
    pattern_ev = r'([가-힣A-Za-z0-9]+(?:\s[가-힣A-Za-z0-9]+){0,2})\s+(전기)\s+[\d.]+㎞/kWh\s+([\d,]+)원'
    match = re.search(pattern_ev, text)
    if match:
        return match.group(1), int(match.group(3).replace(",", ""))

    return None, None


def crawl_one(persona_code, name, url):
    res = requests.get(url, headers=HEADERS, timeout=10)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    trim_name, base_price = extract_trim_and_price(soup)

    return {
        "persona_code": persona_code,
        "vehicle_name": name,
        "source_url": url,
        "trim_name": trim_name,
        "fuel_type": extract_spec(soup, "연료"),
        "displacement": extract_spec(soup, "배기량(㏄)"),
        "horsepower": extract_spec_multi(soup, ["최고출력(PS/rpm)", "모터 최고출력(PS)"]),
        "transmission": extract_spec(soup, "변속기"),
        "fuel_efficiency": extract_spec_multi(soup, ["복합연비(㎞/ℓ)", "복합전비(㎞/kWh)"]),
        "base_price": base_price,
    }


if __name__ == "__main__":
    results = []

    for persona_code, (name, url) in VEHICLE_URLS.items():
        print(f"크롤링 중: {name} ({persona_code})")
        try:
            data = crawl_one(persona_code, name, url)
            print(" ->", data)
            results.append(data)
        except Exception as e:
            print(f"[실패] {name}: {e}")

        time.sleep(1.5)

    with open("../data/raw/vehicle_detail.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n총 {len(results)}대 크롤링 완료 -> ../data/raw/vehicle_detail.json")

    # ---- 아래는 디버깅용. 파일 맨 끝에 붙여넣고 실행하세요 ----
res = requests.get(VEHICLE_URLS["ISTP"][1], headers=HEADERS, timeout=10)
soup = BeautifulSoup(res.text, "html.parser")

# 연료 관련 텍스트가 어디 있는지 찾기
for keyword in ["연료", "변속기", "원"]:
    tag = soup.find(string=lambda s: s and keyword in s)
    if tag:
        print(f"\n=== '{keyword}' 주변 구조 ===")
        print(tag.parent.parent.prettify()[:800])
    else:
        print(f"\n=== '{keyword}' 텍스트를 못 찾음 ===")
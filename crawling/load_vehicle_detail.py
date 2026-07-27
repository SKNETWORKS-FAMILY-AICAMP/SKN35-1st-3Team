"""
load_vehicle_detail.py
- data/raw/vehicle_detail.json 을 읽어서
- vehicle 테이블에서 이름으로 vehicle_id를 찾은 뒤
- vehicle_detail 테이블에 INSERT

주의: detail_transmission 컬럼에 check('auto','manual','CVT','DCT') 제약조건이 걸려있는데,
크롤링한 실제 값('자동 9단', 'e-CVT', '8단 팁트로닉 S' 등)이 이 4개 값과 정확히 일치하지 않아서
그대로 넣으면 INSERT가 실패할 수 있음. 아래 normalize_transmission()에서 대략 매핑하지만,
정확한 값이 필요하면 팀과 상의해서 check 제약조건 자체를 varchar로 자유화하는 걸 추천.

detail_drive_type은 check('FF','FR')만 허용하는데 카이엔처럼 AWD 전용 모델이 있어서
정확히 채울 수 없음 - 이 컬럼은 비워두고 팀에 제약조건 완화를 요청할 것.
"""

import pymysql
import json
import re

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "carbti",
    "charset": "utf8mb4",
}

# 카눈 페이지에 없어서 직접 조사한 좌석수
# (쏘렌토는 가격 근접값으로 추정, 카니발은 가격 정확히 일치해서 확실함)
SEAT_COUNT_MAP = {
    "아반떼": 5,
    "E클래스": 5,
    "G80": 5,
    "XC60": 5,
    "카이엔": 5,
    "ES": 5,
    "티구안": 5,
    "아이오닉5": 5,
    "GV70": 5,
    "쿠퍼": 4,      # 미니쿠퍼, 3도어 기준 추정
    "레이": 5,
    "Model Y": 5,
    "그랜저": 5,
    "쏘렌토": 5,    # 가격 근접값 기준 추정, 100% 확신은 아님
    "카니발": 7,    # 가격 정확히 일치, 확실
    "5시리즈": 5,
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_vehicle_id_map(cur):
    """vehicle 테이블에서 {차량명: vehicle_id} 매핑을 가져옴"""
    cur.execute("SELECT vehicle_id, vehicle_name FROM vehicle")
    return {name: vid for vid, name in cur.fetchall()}


def parse_int(value):
    """'1,598' 같은 문자열에서 숫자만 뽑아 int로 변환. 실패하면 None."""
    if value is None:
        return None
    match = re.search(r"[\d,]+", str(value))
    return int(match.group().replace(",", "")) if match else None


def parse_float(value):
    if value is None:
        return None
    match = re.search(r"[\d.]+", str(value))
    return float(match.group()) if match else None


def normalize_transmission(value):
    """check('auto','manual','CVT','DCT')에 억지로 맞추는 매핑 (정보 손실 있음, 임시용)"""
    if value is None:
        return None
    if "CVT" in value:
        return "CVT"
    if "DCT" in value:
        return "DCT"
    if "수동" in value:
        return "manual"
    return "auto"


def get_seat_count(vehicle_name):
    """vehicle 테이블 이름 기준으로 좌석수 조회. 매핑 없으면 None."""
    return SEAT_COUNT_MAP.get(vehicle_name)


def insert_vehicle_detail(cur, vehicle_id, vehicle_name, item):
    sql = """
        INSERT INTO vehicle_detail
        (detail_trim_name, detail_fuel_type, detail_displacement,
         detail_horsepower, detail_transmission, detail_seat_count,
         detail_base_price, detail_fuel_efficiency, vehicle_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, (
        item.get("trim_name"),
        item.get("fuel_type"),
        parse_int(item.get("displacement")),
        parse_int(item.get("horsepower")),
        normalize_transmission(item.get("transmission")),
        get_seat_count(vehicle_name),
        item.get("base_price"),
        parse_float(item.get("fuel_efficiency")),
        vehicle_id,
    ))


if __name__ == "__main__":
    data = load_json("../data/raw/vehicle_detail.json")

    conn = pymysql.connect(**DB_CONFIG)
    cur = conn.cursor()

    vehicle_id_map = get_vehicle_id_map(cur)

    success, skipped = 0, []
    for item in data:
        vehicle_name = item["vehicle_name"]
        vehicle_id = vehicle_id_map.get(vehicle_name)
        if vehicle_id is None:
            skipped.append(vehicle_name)
            continue
        try:
            insert_vehicle_detail(cur, vehicle_id, vehicle_name, item)
            success += 1
        except Exception as e:
            print(f"[실패] {vehicle_name}: {e}")

    conn.commit()
    cur.close()
    conn.close()

    print(f"\n저장 완료: {success}건")
    if skipped:
        print(f"매칭 실패(vehicle 테이블에 이름 없음): {skipped}")
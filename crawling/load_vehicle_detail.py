"""
load_vehicle_detail.py
- data/raw/vehicle_detail.json 을 읽어서
- vehicle 테이블에서 이름으로 vehicle_id를 찾은 뒤
- vehicle_detail 테이블에 INSERT
"""
import json
import re
import os
from db_config import get_db_connection

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
    "쿠퍼": 4,
    "레이": 5,
    "Model Y": 5,
    "그랜저": 5,
    "쏘렌토": 5,
    "카니발": 7,
    "5시리즈": 5,
}

DRIVE_TYPE_MAP = {
    "아반떼": "전륜구동",
    "E클래스": "후륜구동",
    "G80": "후륜구동",
    "XC60": "AWD",
    "카이엔": "AWD",
    "ES": "전륜구동",
    "티구안": "전륜구동",
    "아이오닉5": "후륜구동",
    "GV70": "후륜구동",
    "쿠퍼": "전륜구동",
    "레이": "전륜구동",
    "Model Y": "후륜구동",
    "그랜저": "전륜구동",
    "쏘렌토": "전륜구동",
    "카니발": "전륜구동",
    "5시리즈": "후륜구동",
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_vehicle_id_map(cur):
    cur.execute("SELECT vehicle_id, vehicle_name FROM vehicle")
    return {name: vid for vid, name in cur.fetchall()}


def parse_int(value):
    if value is None:
        return None
    match = re.search(r"[\d,]+", str(value))
    return int(match.group().replace(",", "")) if match else None


def parse_float(value):
    if value is None:
        return None
    match = re.search(r"[\d.]+", str(value))
    return float(match.group()) if match else None


def insert_vehicle_detail(cur, vehicle_id, vehicle_name, item):
    sql = """
        INSERT INTO vehicle_detail
        (detail_trim_name, detail_fuel_type, detail_displacement,
         detail_horsepower, detail_transmission, detail_drive_type,
         detail_seat_count, detail_base_price, detail_fuel_efficiency, vehicle_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, (
        item.get("trim_name"),
        item.get("fuel_type"),
        parse_int(item.get("displacement")),
        parse_int(item.get("horsepower")),
        item.get("transmission"),  # 원본 값 그대로 (check 제약조건 없음 확인됨)
        DRIVE_TYPE_MAP.get(vehicle_name),
        SEAT_COUNT_MAP.get(vehicle_name),
        item.get("base_price"),
        parse_float(item.get("fuel_efficiency")),
        vehicle_id,
    ))


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "..", "data", "raw", "vehicle_detail.json")
    data = load_json(json_path)

    conn = get_db_connection()
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
from db_config import get_db_connection

# ── 판매실적 데이터 ──────────────────────────────
sales_records = [
    # ══════════════════════════════════════════════════════
    # 2026년 6월
    # ══════════════════════════════════════════════════════

    # ── 기아 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "기아", "vehicle_name": "쏘렌토", "sales_year": 2026, "sales_month": 6, "sales_count": 8561, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "셀토스", "sales_year": 2026, "sales_month": 6, "sales_count": 6685, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "카니발", "sales_year": 2026, "sales_month": 6, "sales_count": 6267, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "스포티지", "sales_year": 2026, "sales_month": 6, "sales_count": 6176, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV5", "sales_year": 2026, "sales_month": 6, "sales_count": 3192, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "K5", "sales_year": 2026, "sales_month": 6, "sales_count": 3150, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "레이", "sales_year": 2026, "sales_month": 6, "sales_count": 2954, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV3", "sales_year": 2026, "sales_month": 6, "sales_count": 2838, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "K8", "sales_year": 2026, "sales_month": 6, "sales_count": 1981, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "모닝", "sales_year": 2026, "sales_month": 6, "sales_count": 1919, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "니로", "sales_year": 2026, "sales_month": 6, "sales_count": 1880, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV6", "sales_year": 2026, "sales_month": 6, "sales_count": 820, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV9", "sales_year": 2026, "sales_month": 6, "sales_count": 392, "sales_avg_price": None},

    # ── 현대자동차 (2026년 6월) ──────────────────────────────
    # 전기차 트림은 vehicle_seed.py 원래 방침대로 같은 모델에 합산함
    {"manufacturer_name": "현대자동차", "vehicle_name": "그랜저", "sales_year": 2026, "sales_month": 6, "sales_count": 10062, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "쏘나타", "sales_year": 2026, "sales_month": 6, "sales_count": 5102, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "팰리세이드", "sales_year": 2026, "sales_month": 6, "sales_count": 4211, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "아반떼", "sales_year": 2026, "sales_month": 6, "sales_count": 4201 + 115, "sales_avg_price": None},  # 아반떼 4,201 + 아반떼 N 115
    {"manufacturer_name": "현대자동차", "vehicle_name": "싼타페", "sales_year": 2026, "sales_month": 6, "sales_count": 4068, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "투싼", "sales_year": 2026, "sales_month": 6, "sales_count": 3285, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "스타리아", "sales_year": 2026, "sales_month": 6, "sales_count": 2579 + 456, "sales_avg_price": None},  # 더 뉴 스타리아 2,579 + 스타리아 일렉트릭 456
    {"manufacturer_name": "현대자동차", "vehicle_name": "코나", "sales_year": 2026, "sales_month": 6, "sales_count": 2558 + 519, "sales_avg_price": None},  # 코나 2,558 + 코나 일렉트릭 519
    {"manufacturer_name": "현대자동차", "vehicle_name": "아이오닉5", "sales_year": 2026, "sales_month": 6, "sales_count": 1693 + 1, "sales_avg_price": None},  # 아이오닉 5 1,693 + 아이오닉 5 N 1
    {"manufacturer_name": "현대자동차", "vehicle_name": "아이오닉9", "sales_year": 2026, "sales_month": 6, "sales_count": 1318, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "베뉴", "sales_year": 2026, "sales_month": 6, "sales_count": 1123, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "아이오닉6", "sales_year": 2026, "sales_month": 6, "sales_count": 773, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "캐스퍼", "sales_year": 2026, "sales_month": 6, "sales_count": 711 + 774, "sales_avg_price": None},  # 캐스퍼 711 + 캐스퍼 일렉트릭 774
    {"manufacturer_name": "현대자동차", "vehicle_name": "넥쏘", "sales_year": 2026, "sales_month": 6, "sales_count": 459, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): 포터2 3,270 / 버스·트럭(현대) 2,375 / 포터2 일렉트릭 558 / ST1 85

    # ── 제네시스 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "제네시스", "vehicle_name": "G80", "sales_year": 2026, "sales_month": 6, "sales_count": 2757 + 187, "sales_avg_price": None},  # G80 2,757 + Electrified G80 187
    {"manufacturer_name": "제네시스", "vehicle_name": "GV70", "sales_year": 2026, "sales_month": 6, "sales_count": 2294 + 134, "sales_avg_price": None},  # GV70 2,294 + Electrified GV70 134
    {"manufacturer_name": "제네시스", "vehicle_name": "GV80", "sales_year": 2026, "sales_month": 6, "sales_count": 1840, "sales_avg_price": None},
    {"manufacturer_name": "제네시스", "vehicle_name": "G90", "sales_year": 2026, "sales_month": 6, "sales_count": 361, "sales_avg_price": None},
    {"manufacturer_name": "제네시스", "vehicle_name": "G70", "sales_year": 2026, "sales_month": 6, "sales_count": 228, "sales_avg_price": None},
    {"manufacturer_name": "제네시스", "vehicle_name": "GV60", "sales_year": 2026, "sales_month": 6, "sales_count": 125 + 10, "sales_avg_price": None},  # GV60 125 + GV60 MAGMA 10
    # GV80 쿠페는 이번 달 목록에 없음(집계 제외 또는 판매 0으로 추정) -> 스킵

    # ── KG모빌리티 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "무쏘 스포츠 & 무쏘 칸", "sales_year": 2026, "sales_month": 6, "sales_count": 1333, "sales_avg_price": None},  # 원자료 표기: "무쏘"
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "토레스", "sales_year": 2026, "sales_month": 6, "sales_count": 624, "sales_avg_price": None},  # 원자료 표기: "뉴 토레스"
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "무쏘 EV", "sales_year": 2026, "sales_month": 6, "sales_count": 578, "sales_avg_price": None},
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "액티언", "sales_year": 2026, "sales_month": 6, "sales_count": 528, "sales_avg_price": None},
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "티볼리", "sales_year": 2026, "sales_month": 6, "sales_count": 372, "sales_avg_price": None},
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "렉스턴", "sales_year": 2026, "sales_month": 6, "sales_count": 111, "sales_avg_price": None},  # 원자료 표기: "렉스턴 뉴 아레나"
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "토레스 EVX", "sales_year": 2026, "sales_month": 6, "sales_count": 91, "sales_avg_price": None},
    # 코란도는 이번 달 목록에 없음 -> 스킵

    # ── 르노코리아 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "르노코리아", "vehicle_name": "그랑 콜레오스", "sales_year": 2026, "sales_month": 6, "sales_count": 1313, "sales_avg_price": None},
    {"manufacturer_name": "르노코리아", "vehicle_name": "아르카나", "sales_year": 2026, "sales_month": 6, "sales_count": 763, "sales_avg_price": None},
    # "필랑트"는 우리 vehicle 테이블에 없는 모델(신차) -> 스킵

    # ── 쉐보레 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "쉐보레", "vehicle_name": "트랙스 크로스오버", "sales_year": 2026, "sales_month": 6, "sales_count": 842, "sales_avg_price": None},
    {"manufacturer_name": "쉐보레", "vehicle_name": "트레일블레이저", "sales_year": 2026, "sales_month": 6, "sales_count": 174, "sales_avg_price": None},
    # "단종차량"은 특정 모델이 아니라 집계 카테고리 -> 스킵

    # ── 테슬라 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "테슬라", "vehicle_name": "Model Y", "sales_year": 2026, "sales_month": 6, "sales_count": 9188, "sales_avg_price": None},
    {"manufacturer_name": "테슬라", "vehicle_name": "Model X", "sales_year": 2026, "sales_month": 6, "sales_count": 1027, "sales_avg_price": None},
    {"manufacturer_name": "테슬라", "vehicle_name": "Model 3", "sales_year": 2026, "sales_month": 6, "sales_count": 414, "sales_avg_price": None},
    {"manufacturer_name": "테슬라", "vehicle_name": "Model S", "sales_year": 2026, "sales_month": 6, "sales_count": 394, "sales_avg_price": None},
    # Cybertruck은 우리 vehicle 테이블에 없는 모델 -> 스킵

    # ── BMW (2026년 6월) ──────────────────────────────
    # i/M 등 전동화·고성능 트림은 vehicle_seed.py 방침대로 같은 베이스 모델에 합산 (i4는 원본에서도 별도 라인이라 유지)
    {"manufacturer_name": "BMW", "vehicle_name": "5시리즈", "sales_year": 2026, "sales_month": 6, "sales_count": 2266 + 300 + 74, "sales_avg_price": None},  # 5 Series 2,266 + i5 300 + M5 74
    {"manufacturer_name": "BMW", "vehicle_name": "X3", "sales_year": 2026, "sales_month": 6, "sales_count": 619 + 58, "sales_avg_price": None},  # X3 619 + The New iX3 58
    {"manufacturer_name": "BMW", "vehicle_name": "X5", "sales_year": 2026, "sales_month": 6, "sales_count": 495 + 2, "sales_avg_price": None},  # X5 495 + X5 M 2
    {"manufacturer_name": "BMW", "vehicle_name": "3시리즈", "sales_year": 2026, "sales_month": 6, "sales_count": 448 + 2, "sales_avg_price": None},  # 3 Series 448 + M3 2
    {"manufacturer_name": "BMW", "vehicle_name": "7시리즈", "sales_year": 2026, "sales_month": 6, "sales_count": 427 + 60, "sales_avg_price": None},  # 7 Series 427 + i7 60
    {"manufacturer_name": "BMW", "vehicle_name": "X7", "sales_year": 2026, "sales_month": 6, "sales_count": 305, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "X6", "sales_year": 2026, "sales_month": 6, "sales_count": 221 + 4, "sales_avg_price": None},  # X6 221 + X6 M 4
    {"manufacturer_name": "BMW", "vehicle_name": "X1", "sales_year": 2026, "sales_month": 6, "sales_count": 176 + 85, "sales_avg_price": None},  # X1 176 + iX1 85
    {"manufacturer_name": "BMW", "vehicle_name": "4시리즈", "sales_year": 2026, "sales_month": 6, "sales_count": 154 + 3, "sales_avg_price": None},  # 4 Series 154 + M4 3
    {"manufacturer_name": "BMW", "vehicle_name": "X4", "sales_year": 2026, "sales_month": 6, "sales_count": 110, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "1시리즈", "sales_year": 2026, "sales_month": 6, "sales_count": 110, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "2시리즈", "sales_year": 2026, "sales_month": 6, "sales_count": 3 + 87 + 75 + 63, "sales_avg_price": None},  # 2 Series 3 + Active Tourer 87 + Gran Coupe 75 + M2 63
    {"manufacturer_name": "BMW", "vehicle_name": "i4", "sales_year": 2026, "sales_month": 6, "sales_count": 80, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "X2", "sales_year": 2026, "sales_month": 6, "sales_count": 63 + 58, "sales_avg_price": None},  # X2 63 + iX2 58
    # 매칭 제외(우리 vehicle 테이블에 없음): iX 111 / Z4 46 / 8 Series 43 / XM 20 / M8 1

    # ── 메르세데스-벤츠 (2026년 6월) ──────────────────────────────
    # Maybach/전동화 트림은 vehicle_seed.py 방침대로 같은 베이스 모델에 합산
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "E클래스", "sales_year": 2026, "sales_month": 6, "sales_count": 2114, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLC", "sales_year": 2026, "sales_month": 6, "sales_count": 1221, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLE", "sales_year": 2026, "sales_month": 6, "sales_count": 634, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "G클래스", "sales_year": 2026, "sales_month": 6, "sales_count": 327 + 9, "sales_avg_price": None},  # G-Class 327 + Electric G-Class 9
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "S클래스", "sales_year": 2026, "sales_month": 6, "sales_count": 292 + 28, "sales_avg_price": None},  # S-Class 292 + Maybach S-Class 28
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "C클래스", "sales_year": 2026, "sales_month": 6, "sales_count": 206, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLS", "sales_year": 2026, "sales_month": 6, "sales_count": 145 + 29, "sales_avg_price": None},  # GLS-Class 145 + Maybach GLS 29
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "EQE", "sales_year": 2026, "sales_month": 6, "sales_count": 26 + 43, "sales_avg_price": None},  # EQE 26 + EQE SUV 43
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLB", "sales_year": 2026, "sales_month": 6, "sales_count": 34, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "AMG GT", "sales_year": 2026, "sales_month": 6, "sales_count": 10 + 6, "sales_avg_price": None},  # AMG GT 10 + The New AMG GT 6
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "CLA", "sales_year": 2026, "sales_month": 6, "sales_count": 18, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLA", "sales_year": 2026, "sales_month": 6, "sales_count": 18, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "EQS", "sales_year": 2026, "sales_month": 6, "sales_count": 7 + 8, "sales_avg_price": None},  # EQS SUV 7 + Maybach EQS SUV 8
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "A클래스", "sales_year": 2026, "sales_month": 6, "sales_count": 12, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): CLE 242 / EQB 111 / SL-Class 20 / EQA 4 / Maybach SL 1

    # ── 아우디 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "아우디", "vehicle_name": "A6", "sales_year": 2026, "sales_month": 6, "sales_count": 455 + 10 + 20, "sales_avg_price": None},  # The new A6 455 + A6 10 + A6 e-tron 20
    {"manufacturer_name": "아우디", "vehicle_name": "Q4 e-tron", "sales_year": 2026, "sales_month": 6, "sales_count": 438, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "Q5", "sales_year": 2026, "sales_month": 6, "sales_count": 427, "sales_avg_price": None},  # 원자료 표기: "The new Q5"
    {"manufacturer_name": "아우디", "vehicle_name": "Q3", "sales_year": 2026, "sales_month": 6, "sales_count": 97 + 2, "sales_avg_price": None},  # The new Q3 97 + Q3 2
    {"manufacturer_name": "아우디", "vehicle_name": "A3", "sales_year": 2026, "sales_month": 6, "sales_count": 84, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "Q8", "sales_year": 2026, "sales_month": 6, "sales_count": 54 + 4, "sales_avg_price": None},  # Q8 54 + Q8 e-tron 4
    {"manufacturer_name": "아우디", "vehicle_name": "Q7", "sales_year": 2026, "sales_month": 6, "sales_count": 54, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "A8", "sales_year": 2026, "sales_month": 6, "sales_count": 21, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "A4", "sales_year": 2026, "sales_month": 6, "sales_count": 3, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "e-tron GT", "sales_year": 2026, "sales_month": 6, "sales_count": 2, "sales_avg_price": None},  # 원자료 표기: "The new e-tron GT"
    {"manufacturer_name": "아우디", "vehicle_name": "A7", "sales_year": 2026, "sales_month": 6, "sales_count": 1, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): The new A5+A5 64 / Q6 e-tron 36

    # ── 렉서스 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "렉서스", "vehicle_name": "ES", "sales_year": 2026, "sales_month": 6, "sales_count": 545, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "NX", "sales_year": 2026, "sales_month": 6, "sales_count": 530, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "RX", "sales_year": 2026, "sales_month": 6, "sales_count": 288, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "UX", "sales_year": 2026, "sales_month": 6, "sales_count": 165, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "LX", "sales_year": 2026, "sales_month": 6, "sales_count": 32, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "LS", "sales_year": 2026, "sales_month": 6, "sales_count": 12, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): LM 122 / IS는 이번 달 목록에 없음

    # ── 볼보 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "볼보", "vehicle_name": "EX30", "sales_year": 2026, "sales_month": 6, "sales_count": 624 + 322, "sales_avg_price": None},  # EX30 624 + EX30 CC 322
    {"manufacturer_name": "볼보", "vehicle_name": "XC60", "sales_year": 2026, "sales_month": 6, "sales_count": 366, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "S90", "sales_year": 2026, "sales_month": 6, "sales_count": 117, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "XC40", "sales_year": 2026, "sales_month": 6, "sales_count": 115, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "XC90", "sales_year": 2026, "sales_month": 6, "sales_count": 111, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "V60", "sales_year": 2026, "sales_month": 6, "sales_count": 24, "sales_avg_price": None},  # 원자료 표기: "V60 Cross Country"
    # S60, EX90은 이번 달 목록에 없음 -> 스킵

    # ── 토요타 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "토요타", "vehicle_name": "RAV4", "sales_year": 2026, "sales_month": 6, "sales_count": 674, "sales_avg_price": None},  # 원자료 표기: "All New RAV4"
    {"manufacturer_name": "토요타", "vehicle_name": "캠리", "sales_year": 2026, "sales_month": 6, "sales_count": 214, "sales_avg_price": None},
    {"manufacturer_name": "토요타", "vehicle_name": "프리우스", "sales_year": 2026, "sales_month": 6, "sales_count": 112, "sales_avg_price": None},
    {"manufacturer_name": "토요타", "vehicle_name": "시에나", "sales_year": 2026, "sales_month": 6, "sales_count": 71, "sales_avg_price": None},
    {"manufacturer_name": "토요타", "vehicle_name": "하이랜더", "sales_year": 2026, "sales_month": 6, "sales_count": 24, "sales_avg_price": None},
    {"manufacturer_name": "토요타", "vehicle_name": "GR86", "sales_year": 2026, "sales_month": 6, "sales_count": 24, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): Alphard 186 / Crown 96 (코롤라·코롤라 크로스는 이번 달 목록에 없음)

    # ── 미니 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "미니", "vehicle_name": "쿠퍼", "sales_year": 2026, "sales_month": 6, "sales_count": 389, "sales_avg_price": None},  # 원자료 표기: "Cooper"
    {"manufacturer_name": "미니", "vehicle_name": "쿠퍼 SE", "sales_year": 2026, "sales_month": 6, "sales_count": 134, "sales_avg_price": None},  # 원자료 표기: "Mini Electric"
    {"manufacturer_name": "미니", "vehicle_name": "컨트리맨", "sales_year": 2026, "sales_month": 6, "sales_count": 157 + 2, "sales_avg_price": None},  # Countryman 157 + Countryman Electric 2
    # 매칭 제외(우리 vehicle 테이블에 없음): Aceman 80 / Convertible 74 (쿠퍼 S는 이번 자료에 별도 표기 없음)

    # ── 포르쉐 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "포르쉐", "vehicle_name": "타이칸", "sales_year": 2026, "sales_month": 6, "sales_count": 196, "sales_avg_price": None},  # 원자료 표기: "Taycan"
    {"manufacturer_name": "포르쉐", "vehicle_name": "카이엔", "sales_year": 2026, "sales_month": 6, "sales_count": 158, "sales_avg_price": None},  # 원자료 표기: "Cayenne"
    {"manufacturer_name": "포르쉐", "vehicle_name": "파나메라", "sales_year": 2026, "sales_month": 6, "sales_count": 137, "sales_avg_price": None},  # 원자료 표기: "Panamera"
    {"manufacturer_name": "포르쉐", "vehicle_name": "마칸", "sales_year": 2026, "sales_month": 6, "sales_count": 123, "sales_avg_price": None},  # 원자료 표기: "Macan Electric"
    {"manufacturer_name": "포르쉐", "vehicle_name": "911", "sales_year": 2026, "sales_month": 6, "sales_count": 102, "sales_avg_price": None},  # 원자료 표기: "The New 911"
    # 카이맨은 이번 달 목록에 없음 -> 스킵

    # ── 폭스바겐 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "폭스바겐", "vehicle_name": "ID.4", "sales_year": 2026, "sales_month": 6, "sales_count": 249, "sales_avg_price": None},
    {"manufacturer_name": "폭스바겐", "vehicle_name": "골프", "sales_year": 2026, "sales_month": 6, "sales_count": 198, "sales_avg_price": None},  # 원자료 표기: "Golf"
    {"manufacturer_name": "폭스바겐", "vehicle_name": "아틀라스", "sales_year": 2026, "sales_month": 6, "sales_count": 31, "sales_avg_price": None},  # 원자료 표기: "Atlas"
    # 매칭 제외(우리 vehicle 테이블에 없음): Touareg 91 / ID.5 33 (티구안·파사트·아테온·ID.7은 이번 달 목록에 없음)

    # ── 혼다 (2026년 6월) ──────────────────────────────
    {"manufacturer_name": "혼다", "vehicle_name": "파일럿", "sales_year": 2026, "sales_month": 6, "sales_count": 24, "sales_avg_price": None},  # 원자료 표기: "New Pilot"
    {"manufacturer_name": "혼다", "vehicle_name": "CR-V", "sales_year": 2026, "sales_month": 6, "sales_count": 15, "sales_avg_price": None},
    {"manufacturer_name": "혼다", "vehicle_name": "어코드", "sales_year": 2026, "sales_month": 6, "sales_count": 7, "sales_avg_price": None},  # 원자료 표기: "Accord"
    # 매칭 제외(우리 vehicle 테이블에 없음): Odyssey 1 (시빅·HR-V는 이번 달 목록에 없음)

    # ══════════════════════════════════════════════════════
    # 2026년 5월
    # ══════════════════════════════════════════════════════

    # ── 기아 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "기아", "vehicle_name": "쏘렌토", "sales_year": 2026, "sales_month": 5, "sales_count": 7836, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "스포티지", "sales_year": 2026, "sales_month": 5, "sales_count": 4760, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "카니발", "sales_year": 2026, "sales_month": 5, "sales_count": 4543, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "셀토스", "sales_year": 2026, "sales_month": 5, "sales_count": 3169, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV3", "sales_year": 2026, "sales_month": 5, "sales_count": 3021, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV5", "sales_year": 2026, "sales_month": 5, "sales_count": 2581, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "레이", "sales_year": 2026, "sales_month": 5, "sales_count": 2363 + 1056, "sales_avg_price": None},  # 레이 2,363 + 레이 EV 1,056
    {"manufacturer_name": "기아", "vehicle_name": "K5", "sales_year": 2026, "sales_month": 5, "sales_count": 2237, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "모닝", "sales_year": 2026, "sales_month": 5, "sales_count": 2234, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "K8", "sales_year": 2026, "sales_month": 5, "sales_count": 1752, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "니로", "sales_year": 2026, "sales_month": 5, "sales_count": 1355, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV6", "sales_year": 2026, "sales_month": 5, "sales_count": 905, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV9", "sales_year": 2026, "sales_month": 5, "sales_count": 263, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): PV5 2,303 / 봉고 3 1,575 / EV4 1,196 / 버스/특수(기아) 738 / 봉고 3 EV 449 / 타스만 250 / K9 141
    # 모하비는 이번 달 목록에 없음 -> 스킵

    # ── 현대자동차 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "현대자동차", "vehicle_name": "그랜저", "sales_year": 2026, "sales_month": 5, "sales_count": 3321 + 1862, "sales_avg_price": None},  # 더 뉴 그랜저 3,321 + 그랜저 1,862
    {"manufacturer_name": "현대자동차", "vehicle_name": "아반떼", "sales_year": 2026, "sales_month": 5, "sales_count": 4431 + 95, "sales_avg_price": None},  # 아반떼 4,431 + 아반떼 N 95
    {"manufacturer_name": "현대자동차", "vehicle_name": "쏘나타", "sales_year": 2026, "sales_month": 5, "sales_count": 4118, "sales_avg_price": None},  # 원자료 표기: "쏘나타 디 엣지"
    {"manufacturer_name": "현대자동차", "vehicle_name": "싼타페", "sales_year": 2026, "sales_month": 5, "sales_count": 2862, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "아이오닉5", "sales_year": 2026, "sales_month": 5, "sales_count": 2574 + 1, "sales_avg_price": None},  # 아이오닉 5 2,574 + 아이오닉 5 N 1
    {"manufacturer_name": "현대자동차", "vehicle_name": "투싼", "sales_year": 2026, "sales_month": 5, "sales_count": 2183, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "스타리아", "sales_year": 2026, "sales_month": 5, "sales_count": 1912, "sales_avg_price": None},  # 원자료 표기: "더 뉴 스타리아"
    {"manufacturer_name": "현대자동차", "vehicle_name": "팰리세이드", "sales_year": 2026, "sales_month": 5, "sales_count": 1825, "sales_avg_price": None},  # 원자료 표기: "디 올 뉴 팰리세이드"
    {"manufacturer_name": "현대자동차", "vehicle_name": "코나", "sales_year": 2026, "sales_month": 5, "sales_count": 1643 + 452, "sales_avg_price": None},  # 코나 1,643 + 코나 일렉트릭 452
    {"manufacturer_name": "현대자동차", "vehicle_name": "아이오닉9", "sales_year": 2026, "sales_month": 5, "sales_count": 1482, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "캐스퍼", "sales_year": 2026, "sales_month": 5, "sales_count": 1152 + 384, "sales_avg_price": None},  # 캐스퍼 일렉트릭 1,152 + 캐스퍼 384
    {"manufacturer_name": "현대자동차", "vehicle_name": "아이오닉6", "sales_year": 2026, "sales_month": 5, "sales_count": 1049, "sales_avg_price": None},  # 원자료 표기: "더 뉴 아이오닉 6"
    {"manufacturer_name": "현대자동차", "vehicle_name": "베뉴", "sales_year": 2026, "sales_month": 5, "sales_count": 903, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "넥쏘", "sales_year": 2026, "sales_month": 5, "sales_count": 338, "sales_avg_price": None},  # 원자료 표기: "디 올 뉴 넥쏘"
    # 매칭 제외(우리 vehicle 테이블에 없음): 포터2 3,375 / 버스/트럭(현대) 1,292 / 포터2 일렉트릭 895 / 더 뉴 마이티 582 / 카운티 198 / ST1 130 / 쏠라티 117 / 카운티 일렉트릭 20

    # ── 제네시스 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "제네시스", "vehicle_name": "G80", "sales_year": 2026, "sales_month": 5, "sales_count": 2088 + 132, "sales_avg_price": None},  # G80 2,088 + Electrified G80 132
    {"manufacturer_name": "제네시스", "vehicle_name": "GV70", "sales_year": 2026, "sales_month": 5, "sales_count": 1647 + 151, "sales_avg_price": None},  # GV70 1,647 + Electrified GV70 151
    {"manufacturer_name": "제네시스", "vehicle_name": "GV80", "sales_year": 2026, "sales_month": 5, "sales_count": 1547, "sales_avg_price": None},
    {"manufacturer_name": "제네시스", "vehicle_name": "G90", "sales_year": 2026, "sales_month": 5, "sales_count": 405, "sales_avg_price": None},
    {"manufacturer_name": "제네시스", "vehicle_name": "GV60", "sales_year": 2026, "sales_month": 5, "sales_count": 129 + 10, "sales_avg_price": None},  # GV60 129 + GV60 MAGMA 10
    {"manufacturer_name": "제네시스", "vehicle_name": "G70", "sales_year": 2026, "sales_month": 5, "sales_count": 52, "sales_avg_price": None},
    # GV80 쿠페는 이번 달 목록에 없음 -> 스킵

    # ── KG모빌리티 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "무쏘 스포츠 & 무쏘 칸", "sales_year": 2026, "sales_month": 5, "sales_count": 1137, "sales_avg_price": None},  # 원자료 표기: "무쏘"
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "무쏘 EV", "sales_year": 2026, "sales_month": 5, "sales_count": 755, "sales_avg_price": None},
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "티볼리", "sales_year": 2026, "sales_month": 5, "sales_count": 548, "sales_avg_price": None},
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "액티언", "sales_year": 2026, "sales_month": 5, "sales_count": 468, "sales_avg_price": None},
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "토레스", "sales_year": 2026, "sales_month": 5, "sales_count": 183, "sales_avg_price": None},  # 원자료 표기: "뉴 토레스"
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "렉스턴", "sales_year": 2026, "sales_month": 5, "sales_count": 128, "sales_avg_price": None},  # 원자료 표기: "렉스턴 뉴 아레나"
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "토레스 EVX", "sales_year": 2026, "sales_month": 5, "sales_count": 99, "sales_avg_price": None},
    # 코란도는 이번 달 목록에 없음 -> 스킵

    # ── 르노코리아 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "르노코리아", "vehicle_name": "그랑 콜레오스", "sales_year": 2026, "sales_month": 5, "sales_count": 1248, "sales_avg_price": None},
    {"manufacturer_name": "르노코리아", "vehicle_name": "아르카나", "sales_year": 2026, "sales_month": 5, "sales_count": 444, "sales_avg_price": None},
    # "필랑트"는 우리 vehicle 테이블에 없는 모델 -> 스킵

    # ── 쉐보레 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "쉐보레", "vehicle_name": "트랙스 크로스오버", "sales_year": 2026, "sales_month": 5, "sales_count": 648, "sales_avg_price": None},
    {"manufacturer_name": "쉐보레", "vehicle_name": "트레일블레이저", "sales_year": 2026, "sales_month": 5, "sales_count": 143, "sales_avg_price": None},
    # "트래버스"는 우리 vehicle 테이블에 없는 모델 -> 스킵

    # ── 테슬라 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "테슬라", "vehicle_name": "Model Y", "sales_year": 2026, "sales_month": 5, "sales_count": 8762, "sales_avg_price": None},
    {"manufacturer_name": "테슬라", "vehicle_name": "Model 3", "sales_year": 2026, "sales_month": 5, "sales_count": 1301, "sales_avg_price": None},
    {"manufacturer_name": "테슬라", "vehicle_name": "Model X", "sales_year": 2026, "sales_month": 5, "sales_count": 508, "sales_avg_price": None},
    {"manufacturer_name": "테슬라", "vehicle_name": "Model S", "sales_year": 2026, "sales_month": 5, "sales_count": 170, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): Cybertruck 125

    # ── BMW (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "BMW", "vehicle_name": "5시리즈", "sales_year": 2026, "sales_month": 5, "sales_count": 2060 + 234 + 42, "sales_avg_price": None},  # 5 Series 2,060 + i5 234 + M5 42
    {"manufacturer_name": "BMW", "vehicle_name": "X3", "sales_year": 2026, "sales_month": 5, "sales_count": 743, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "X5", "sales_year": 2026, "sales_month": 5, "sales_count": 542 + 2, "sales_avg_price": None},  # X5 542 + X5 M 2
    {"manufacturer_name": "BMW", "vehicle_name": "3시리즈", "sales_year": 2026, "sales_month": 5, "sales_count": 534 + 19, "sales_avg_price": None},  # 3 Series 534 + M3 19
    {"manufacturer_name": "BMW", "vehicle_name": "7시리즈", "sales_year": 2026, "sales_month": 5, "sales_count": 373 + 69, "sales_avg_price": None},  # 7 Series 373 + i7 69
    {"manufacturer_name": "BMW", "vehicle_name": "X7", "sales_year": 2026, "sales_month": 5, "sales_count": 355, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "X6", "sales_year": 2026, "sales_month": 5, "sales_count": 282 + 3, "sales_avg_price": None},  # X6 282 + X6 M 3
    {"manufacturer_name": "BMW", "vehicle_name": "X1", "sales_year": 2026, "sales_month": 5, "sales_count": 176 + 134, "sales_avg_price": None},  # X1 176 + iX1 134
    {"manufacturer_name": "BMW", "vehicle_name": "X4", "sales_year": 2026, "sales_month": 5, "sales_count": 130, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "4시리즈", "sales_year": 2026, "sales_month": 5, "sales_count": 128 + 13, "sales_avg_price": None},  # 4 Series 128 + M4 13
    {"manufacturer_name": "BMW", "vehicle_name": "1시리즈", "sales_year": 2026, "sales_month": 5, "sales_count": 113, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "2시리즈", "sales_year": 2026, "sales_month": 5, "sales_count": 97 + 58 + 26 + 14, "sales_avg_price": None},  # Gran Coupe 97 + Active Tourer 58 + M2 26 + 2 Series 14
    {"manufacturer_name": "BMW", "vehicle_name": "X2", "sales_year": 2026, "sales_month": 5, "sales_count": 74 + 52, "sales_avg_price": None},  # X2 74 + iX2 52
    {"manufacturer_name": "BMW", "vehicle_name": "i4", "sales_year": 2026, "sales_month": 5, "sales_count": 70, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): iX 107 / 8 Series 40 / Z4 37 / XM 28

    # ── 메르세데스-벤츠 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "E클래스", "sales_year": 2026, "sales_month": 5, "sales_count": 1285, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLC", "sales_year": 2026, "sales_month": 5, "sales_count": 560, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLE", "sales_year": 2026, "sales_month": 5, "sales_count": 433, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "G클래스", "sales_year": 2026, "sales_month": 5, "sales_count": 301 + 4, "sales_avg_price": None},  # G-Class 301 + Electric G-Class 4
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "S클래스", "sales_year": 2026, "sales_month": 5, "sales_count": 204 + 15, "sales_avg_price": None},  # S-Class 204 + Maybach S-Class 15
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLS", "sales_year": 2026, "sales_month": 5, "sales_count": 128 + 8, "sales_avg_price": None},  # GLS-Class 128 + Maybach GLS 8
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "C클래스", "sales_year": 2026, "sales_month": 5, "sales_count": 104, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "EQE", "sales_year": 2026, "sales_month": 5, "sales_count": 42 + 3, "sales_avg_price": None},  # EQE SUV 42 + EQE 3
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLB", "sales_year": 2026, "sales_month": 5, "sales_count": 36, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "A클래스", "sales_year": 2026, "sales_month": 5, "sales_count": 23, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLA", "sales_year": 2026, "sales_month": 5, "sales_count": 23, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "AMG GT", "sales_year": 2026, "sales_month": 5, "sales_count": 8 + 8, "sales_avg_price": None},  # The New AMG GT 8 + AMG GT 8
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "CLA", "sales_year": 2026, "sales_month": 5, "sales_count": 8, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "EQS", "sales_year": 2026, "sales_month": 5, "sales_count": 4, "sales_avg_price": None},  # EQS SUV 4
    # 매칭 제외(우리 vehicle 테이블에 없음): CLE 211 / EQB 120 / EQA 14 / SL-Class 11

    # ── 아우디 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "아우디", "vehicle_name": "A6", "sales_year": 2026, "sales_month": 5, "sales_count": 615 + 7 + 2, "sales_avg_price": None},  # The new A6 615 + A6 e-tron 7 + A6 2
    {"manufacturer_name": "아우디", "vehicle_name": "Q4 e-tron", "sales_year": 2026, "sales_month": 5, "sales_count": 361, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "Q5", "sales_year": 2026, "sales_month": 5, "sales_count": 332, "sales_avg_price": None},  # 원자료 표기: "The new Q5"
    {"manufacturer_name": "아우디", "vehicle_name": "A3", "sales_year": 2026, "sales_month": 5, "sales_count": 65, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "Q8", "sales_year": 2026, "sales_month": 5, "sales_count": 43, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "Q7", "sales_year": 2026, "sales_month": 5, "sales_count": 25, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "A8", "sales_year": 2026, "sales_month": 5, "sales_count": 2, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "e-tron GT", "sales_year": 2026, "sales_month": 5, "sales_count": 1, "sales_avg_price": None},  # 원자료 표기: "The new e-tron GT"
    {"manufacturer_name": "아우디", "vehicle_name": "Q3", "sales_year": 2026, "sales_month": 5, "sales_count": 1, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): The new A5 55

    # ── 렉서스 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "렉서스", "vehicle_name": "ES", "sales_year": 2026, "sales_month": 5, "sales_count": 572, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "NX", "sales_year": 2026, "sales_month": 5, "sales_count": 419, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "RX", "sales_year": 2026, "sales_month": 5, "sales_count": 200, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "UX", "sales_year": 2026, "sales_month": 5, "sales_count": 51, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "LX", "sales_year": 2026, "sales_month": 5, "sales_count": 37, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "LS", "sales_year": 2026, "sales_month": 5, "sales_count": 8, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): LM 4 (IS는 이번 달 목록에 없음)

    # ── 볼보 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "볼보", "vehicle_name": "XC60", "sales_year": 2026, "sales_month": 5, "sales_count": 336, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "EX30", "sales_year": 2026, "sales_month": 5, "sales_count": 317 + 24, "sales_avg_price": None},  # EX30 317 + EX30 CC 24
    {"manufacturer_name": "볼보", "vehicle_name": "XC90", "sales_year": 2026, "sales_month": 5, "sales_count": 134, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "XC40", "sales_year": 2026, "sales_month": 5, "sales_count": 112, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "S90", "sales_year": 2026, "sales_month": 5, "sales_count": 109, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "V60", "sales_year": 2026, "sales_month": 5, "sales_count": 26, "sales_avg_price": None},  # 원자료 표기: "V60 Cross Country"
    # S60, EX90은 이번 달 목록에 없음 -> 스킵

    # ── 토요타 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "토요타", "vehicle_name": "캠리", "sales_year": 2026, "sales_month": 5, "sales_count": 180, "sales_avg_price": None},  # 원자료 표기: "Camry"
    {"manufacturer_name": "토요타", "vehicle_name": "프리우스", "sales_year": 2026, "sales_month": 5, "sales_count": 144, "sales_avg_price": None},  # 원자료 표기: "Prius"
    {"manufacturer_name": "토요타", "vehicle_name": "시에나", "sales_year": 2026, "sales_month": 5, "sales_count": 82, "sales_avg_price": None},  # 원자료 표기: "Sienna"
    {"manufacturer_name": "토요타", "vehicle_name": "RAV4", "sales_year": 2026, "sales_month": 5, "sales_count": 21, "sales_avg_price": None},
    {"manufacturer_name": "토요타", "vehicle_name": "하이랜더", "sales_year": 2026, "sales_month": 5, "sales_count": 21, "sales_avg_price": None},  # 원자료 표기: "Highlander"
    {"manufacturer_name": "토요타", "vehicle_name": "GR86", "sales_year": 2026, "sales_month": 5, "sales_count": 14, "sales_avg_price": None},  # 원자료 표기: "GR 86"
    # 매칭 제외(우리 vehicle 테이블에 없음): Alphard 181 / Crown 161 (코롤라·코롤라 크로스는 이번 달 목록에 없음)

    # ── 미니 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "미니", "vehicle_name": "쿠퍼", "sales_year": 2026, "sales_month": 5, "sales_count": 267, "sales_avg_price": None},  # 원자료 표기: "Cooper"
    {"manufacturer_name": "미니", "vehicle_name": "컨트리맨", "sales_year": 2026, "sales_month": 5, "sales_count": 122 + 10, "sales_avg_price": None},  # Countryman 122 + Countryman Electric 10
    {"manufacturer_name": "미니", "vehicle_name": "쿠퍼 SE", "sales_year": 2026, "sales_month": 5, "sales_count": 96, "sales_avg_price": None},  # 원자료 표기: "Mini Electric"
    # 매칭 제외(우리 vehicle 테이블에 없음): Aceman 57 / Convertible 52 (쿠퍼 S는 이번 자료에 별도 표기 없음)

    # ── 포르쉐 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "포르쉐", "vehicle_name": "카이엔", "sales_year": 2026, "sales_month": 5, "sales_count": 286, "sales_avg_price": None},  # 원자료 표기: "Cayenne"
    {"manufacturer_name": "포르쉐", "vehicle_name": "마칸", "sales_year": 2026, "sales_month": 5, "sales_count": 197, "sales_avg_price": None},  # 원자료 표기: "Macan Electric"
    {"manufacturer_name": "포르쉐", "vehicle_name": "타이칸", "sales_year": 2026, "sales_month": 5, "sales_count": 125, "sales_avg_price": None},  # 원자료 표기: "Taycan"
    {"manufacturer_name": "포르쉐", "vehicle_name": "파나메라", "sales_year": 2026, "sales_month": 5, "sales_count": 109, "sales_avg_price": None},  # 원자료 표기: "Panamera"
    {"manufacturer_name": "포르쉐", "vehicle_name": "911", "sales_year": 2026, "sales_month": 5, "sales_count": 103, "sales_avg_price": None},  # 원자료 표기: "The New 911"
    # 카이맨은 이번 달 목록에 없음 -> 스킵

    # ── 폭스바겐 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "폭스바겐", "vehicle_name": "ID.4", "sales_year": 2026, "sales_month": 5, "sales_count": 209, "sales_avg_price": None},
    {"manufacturer_name": "폭스바겐", "vehicle_name": "골프", "sales_year": 2026, "sales_month": 5, "sales_count": 136, "sales_avg_price": None},  # 원자료 표기: "Golf"
    {"manufacturer_name": "폭스바겐", "vehicle_name": "아틀라스", "sales_year": 2026, "sales_month": 5, "sales_count": 52, "sales_avg_price": None},  # 원자료 표기: "Atlas"
    # 매칭 제외(우리 vehicle 테이블에 없음): Touareg 51 / ID.5 3 (티구안·파사트·아테온·ID.7은 이번 달 목록에 없음)

    # ── 혼다 (2026년 5월) ──────────────────────────────
    {"manufacturer_name": "혼다", "vehicle_name": "CR-V", "sales_year": 2026, "sales_month": 5, "sales_count": 35, "sales_avg_price": None},
    {"manufacturer_name": "혼다", "vehicle_name": "어코드", "sales_year": 2026, "sales_month": 5, "sales_count": 12, "sales_avg_price": None},  # 원자료 표기: "Accord"
    # 매칭 제외(우리 vehicle 테이블에 없음): Odyssey 15 / New Pilot 13

    # ══════════════════════════════════════════════════════
    # 2026년 4월
    # ══════════════════════════════════════════════════════

    # ── 기아 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "기아", "vehicle_name": "쏘렌토", "sales_year": 2026, "sales_month": 4, "sales_count": 12078, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "카니발", "sales_year": 2026, "sales_month": 4, "sales_count": 4995, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "스포티지", "sales_year": 2026, "sales_month": 4, "sales_count": 4972, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV3", "sales_year": 2026, "sales_month": 4, "sales_count": 3898, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "레이", "sales_year": 2026, "sales_month": 4, "sales_count": 3636 + 1241, "sales_avg_price": None},  # 레이 3,636 + 레이 EV 1,241
    {"manufacturer_name": "기아", "vehicle_name": "셀토스", "sales_year": 2026, "sales_month": 4, "sales_count": 3580, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV5", "sales_year": 2026, "sales_month": 4, "sales_count": 3308, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "모닝", "sales_year": 2026, "sales_month": 4, "sales_count": 3186, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "K5", "sales_year": 2026, "sales_month": 4, "sales_count": 2366, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "K8", "sales_year": 2026, "sales_month": 4, "sales_count": 1461, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "니로", "sales_year": 2026, "sales_month": 4, "sales_count": 1289, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV6", "sales_year": 2026, "sales_month": 4, "sales_count": 1062, "sales_avg_price": None},
    {"manufacturer_name": "기아", "vehicle_name": "EV9", "sales_year": 2026, "sales_month": 4, "sales_count": 393, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): 봉고 3 3,059 / PV5 2,262 / EV4 1,432 / 봉고 3 EV 339 / 타스만 302 / 버스(기아) 130 / K9 119
    # 모하비는 이번 달 목록에 없음 -> 스킵

    # ── 현대자동차 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "현대자동차", "vehicle_name": "그랜저", "sales_year": 2026, "sales_month": 4, "sales_count": 6622, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "쏘나타", "sales_year": 2026, "sales_month": 4, "sales_count": 5754, "sales_avg_price": None},  # 원자료 표기: "쏘나타 디 엣지"
    {"manufacturer_name": "현대자동차", "vehicle_name": "아반떼", "sales_year": 2026, "sales_month": 4, "sales_count": 5350 + 125, "sales_avg_price": None},  # 아반떼 5,350 + 아반떼 N 125
    {"manufacturer_name": "현대자동차", "vehicle_name": "싼타페", "sales_year": 2026, "sales_month": 4, "sales_count": 3902, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "투싼", "sales_year": 2026, "sales_month": 4, "sales_count": 3858, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "팰리세이드", "sales_year": 2026, "sales_month": 4, "sales_count": 3422, "sales_avg_price": None},  # 원자료 표기: "디 올 뉴 팰리세이드"
    {"manufacturer_name": "현대자동차", "vehicle_name": "스타리아", "sales_year": 2026, "sales_month": 4, "sales_count": 3039, "sales_avg_price": None},  # 원자료 표기: "더 뉴 스타리아"
    {"manufacturer_name": "현대자동차", "vehicle_name": "코나", "sales_year": 2026, "sales_month": 4, "sales_count": 2140 + 419, "sales_avg_price": None},  # 코나 2,140 + 코나 일렉트릭 419
    {"manufacturer_name": "현대자동차", "vehicle_name": "아이오닉5", "sales_year": 2026, "sales_month": 4, "sales_count": 1668 + 6, "sales_avg_price": None},  # 아이오닉 5 1,668 + 아이오닉 5 N 6
    {"manufacturer_name": "현대자동차", "vehicle_name": "아이오닉9", "sales_year": 2026, "sales_month": 4, "sales_count": 1225, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "베뉴", "sales_year": 2026, "sales_month": 4, "sales_count": 1061, "sales_avg_price": None},
    {"manufacturer_name": "현대자동차", "vehicle_name": "캐스퍼", "sales_year": 2026, "sales_month": 4, "sales_count": 638 + 504, "sales_avg_price": None},  # 캐스퍼 일렉트릭 638 + 캐스퍼 504
    {"manufacturer_name": "현대자동차", "vehicle_name": "아이오닉6", "sales_year": 2026, "sales_month": 4, "sales_count": 475, "sales_avg_price": None},  # 원자료 표기: "더 뉴 아이오닉 6"
    {"manufacturer_name": "현대자동차", "vehicle_name": "넥쏘", "sales_year": 2026, "sales_month": 4, "sales_count": 441, "sales_avg_price": None},  # 원자료 표기: "디 올 뉴 넥쏘"
    # 매칭 제외(우리 vehicle 테이블에 없음): 포터2 4,078 / 버스/트럭(현대) 800 / 포터2 일렉트릭 765 / 마이티 330 / 카운티 221 / 쏠라티 172 / ST1 129 / 카운티 일렉트릭 27

    # ── 제네시스 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "제네시스", "vehicle_name": "G80", "sales_year": 2026, "sales_month": 4, "sales_count": 2373 + 150, "sales_avg_price": None},  # G80 2,373 + Electrified G80 150
    {"manufacturer_name": "제네시스", "vehicle_name": "GV70", "sales_year": 2026, "sales_month": 4, "sales_count": 1911 + 157, "sales_avg_price": None},  # GV70 1,911 + Electrified GV70 157
    {"manufacturer_name": "제네시스", "vehicle_name": "GV80", "sales_year": 2026, "sales_month": 4, "sales_count": 1693, "sales_avg_price": None},
    {"manufacturer_name": "제네시스", "vehicle_name": "G90", "sales_year": 2026, "sales_month": 4, "sales_count": 409, "sales_avg_price": None},
    {"manufacturer_name": "제네시스", "vehicle_name": "GV60", "sales_year": 2026, "sales_month": 4, "sales_count": 94 + 19, "sales_avg_price": None},  # GV60 94 + GV60 MAGMA 19
    {"manufacturer_name": "제네시스", "vehicle_name": "G70", "sales_year": 2026, "sales_month": 4, "sales_count": 62, "sales_avg_price": None},
    # GV80 쿠페는 이번 달 목록에 없음 -> 스킵

    # ── KG모빌리티 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "무쏘 스포츠 & 무쏘 칸", "sales_year": 2026, "sales_month": 4, "sales_count": 1135, "sales_avg_price": None},  # 원자료 표기: "무쏘"
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "무쏘 EV", "sales_year": 2026, "sales_month": 4, "sales_count": 810, "sales_avg_price": None},
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "액티언", "sales_year": 2026, "sales_month": 4, "sales_count": 520, "sales_avg_price": None},
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "티볼리", "sales_year": 2026, "sales_month": 4, "sales_count": 415, "sales_avg_price": None},
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "토레스", "sales_year": 2026, "sales_month": 4, "sales_count": 327, "sales_avg_price": None},
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "렉스턴", "sales_year": 2026, "sales_month": 4, "sales_count": 90, "sales_avg_price": None},  # 원자료 표기: "렉스턴 뉴 아레나"
    {"manufacturer_name": "KG모빌리티", "vehicle_name": "토레스 EVX", "sales_year": 2026, "sales_month": 4, "sales_count": 85, "sales_avg_price": None},
    # 코란도는 이번 달 목록에 없음 -> 스킵

    # ── 르노코리아 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "르노코리아", "vehicle_name": "그랑 콜레오스", "sales_year": 2026, "sales_month": 4, "sales_count": 1550, "sales_avg_price": None},
    {"manufacturer_name": "르노코리아", "vehicle_name": "아르카나", "sales_year": 2026, "sales_month": 4, "sales_count": 336, "sales_avg_price": None},
    # "필랑트"는 우리 vehicle 테이블에 없는 모델 -> 스킵

    # ── 쉐보레 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "쉐보레", "vehicle_name": "트랙스 크로스오버", "sales_year": 2026, "sales_month": 4, "sales_count": 613, "sales_avg_price": None},
    {"manufacturer_name": "쉐보레", "vehicle_name": "트레일블레이저", "sales_year": 2026, "sales_month": 4, "sales_count": 168, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): 콜로라도 4 / 트래버스 1

    # ── 테슬라 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "테슬라", "vehicle_name": "Model Y", "sales_year": 2026, "sales_month": 4, "sales_count": 10086, "sales_avg_price": None},
    {"manufacturer_name": "테슬라", "vehicle_name": "Model 3", "sales_year": 2026, "sales_month": 4, "sales_count": 2596, "sales_avg_price": None},
    {"manufacturer_name": "테슬라", "vehicle_name": "Model X", "sales_year": 2026, "sales_month": 4, "sales_count": 427, "sales_avg_price": None},
    {"manufacturer_name": "테슬라", "vehicle_name": "Model S", "sales_year": 2026, "sales_month": 4, "sales_count": 76, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): Cybertruck 5

    # ── BMW (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "BMW", "vehicle_name": "5시리즈", "sales_year": 2026, "sales_month": 4, "sales_count": 1887 + 319 + 40, "sales_avg_price": None},  # 5 Series 1,887 + i5 319 + M5 40
    {"manufacturer_name": "BMW", "vehicle_name": "X3", "sales_year": 2026, "sales_month": 4, "sales_count": 692, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "X5", "sales_year": 2026, "sales_month": 4, "sales_count": 564 + 10, "sales_avg_price": None},  # X5 564 + X5 M 10
    {"manufacturer_name": "BMW", "vehicle_name": "3시리즈", "sales_year": 2026, "sales_month": 4, "sales_count": 553 + 7, "sales_avg_price": None},  # 3 Series 553 + M3 7
    {"manufacturer_name": "BMW", "vehicle_name": "7시리즈", "sales_year": 2026, "sales_month": 4, "sales_count": 445 + 89, "sales_avg_price": None},  # 7 Series 445 + i7 89
    {"manufacturer_name": "BMW", "vehicle_name": "X7", "sales_year": 2026, "sales_month": 4, "sales_count": 403, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "X6", "sales_year": 2026, "sales_month": 4, "sales_count": 261 + 6, "sales_avg_price": None},  # X6 261 + X6 M 6
    {"manufacturer_name": "BMW", "vehicle_name": "X1", "sales_year": 2026, "sales_month": 4, "sales_count": 188 + 136, "sales_avg_price": None},  # X1 188 + iX1 136
    {"manufacturer_name": "BMW", "vehicle_name": "X4", "sales_year": 2026, "sales_month": 4, "sales_count": 179, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "4시리즈", "sales_year": 2026, "sales_month": 4, "sales_count": 164 + 4, "sales_avg_price": None},  # 4 Series 164 + M4 4
    {"manufacturer_name": "BMW", "vehicle_name": "1시리즈", "sales_year": 2026, "sales_month": 4, "sales_count": 90, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "X2", "sales_year": 2026, "sales_month": 4, "sales_count": 82 + 85, "sales_avg_price": None},  # X2 82 + iX2 85
    {"manufacturer_name": "BMW", "vehicle_name": "i4", "sales_year": 2026, "sales_month": 4, "sales_count": 73, "sales_avg_price": None},
    {"manufacturer_name": "BMW", "vehicle_name": "2시리즈", "sales_year": 2026, "sales_month": 4, "sales_count": 68 + 55 + 9, "sales_avg_price": None},  # Active Tourer 68 + Gran Coupe 55 + 2 Series 9
    # 매칭 제외(우리 vehicle 테이블에 없음): iX 112 / Z4 55 / 8 Series 42 / XM 24 / M2 15 / M8 1

    # ── 메르세데스-벤츠 (2026년 4월) ──────────────────────────────
    # 원자료에 "EQS" 항목이 두 줄로 중복 표기되어 합산함
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "E클래스", "sales_year": 2026, "sales_month": 4, "sales_count": 1695, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLE", "sales_year": 2026, "sales_month": 4, "sales_count": 640, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLC", "sales_year": 2026, "sales_month": 4, "sales_count": 597, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "G클래스", "sales_year": 2026, "sales_month": 4, "sales_count": 304 + 3, "sales_avg_price": None},  # G-Class 304 + Electric G-Class 3
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "S클래스", "sales_year": 2026, "sales_month": 4, "sales_count": 298 + 82, "sales_avg_price": None},  # S-Class 298 + Maybach S-Class 82
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "EQE", "sales_year": 2026, "sales_month": 4, "sales_count": 119 + 31, "sales_avg_price": None},  # EQE SUV 119 + EQE 31
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "A클래스", "sales_year": 2026, "sales_month": 4, "sales_count": 92, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "C클래스", "sales_year": 2026, "sales_month": 4, "sales_count": 87, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "CLA", "sales_year": 2026, "sales_month": 4, "sales_count": 80, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLB", "sales_year": 2026, "sales_month": 4, "sales_count": 78, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "AMG GT", "sales_year": 2026, "sales_month": 4, "sales_count": 71 + 19, "sales_avg_price": None},  # AMG GT 71 + The New AMG GT 19
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLS", "sales_year": 2026, "sales_month": 4, "sales_count": 41 + 25, "sales_avg_price": None},  # GLS-Class 41 + Maybach GLS 25
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "GLA", "sales_year": 2026, "sales_month": 4, "sales_count": 24, "sales_avg_price": None},
    {"manufacturer_name": "메르세데스-벤츠", "vehicle_name": "EQS", "sales_year": 2026, "sales_month": 4, "sales_count": 12 + 4 + 1 + 1, "sales_avg_price": None},  # EQS SUV 12 + Maybach EQS SUV 4 + EQS 1 + EQS 1
    # 매칭 제외(우리 vehicle 테이블에 없음): CLE 305 / EQB 133 / Maybach SL 20 / EQA 18 / SL-Class 16

    # ── 아우디 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "아우디", "vehicle_name": "Q4 e-tron", "sales_year": 2026, "sales_month": 4, "sales_count": 368, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "Q5", "sales_year": 2026, "sales_month": 4, "sales_count": 289, "sales_avg_price": None},  # 원자료 표기: "The new Q5"
    {"manufacturer_name": "아우디", "vehicle_name": "A3", "sales_year": 2026, "sales_month": 4, "sales_count": 87, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "A6", "sales_year": 2026, "sales_month": 4, "sales_count": 66 + 19 + 9, "sales_avg_price": None},  # The new A6 66 + A6 19 + A6 e-tron 9
    {"manufacturer_name": "아우디", "vehicle_name": "Q8", "sales_year": 2026, "sales_month": 4, "sales_count": 39, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "Q7", "sales_year": 2026, "sales_month": 4, "sales_count": 30, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "Q3", "sales_year": 2026, "sales_month": 4, "sales_count": 2, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "A8", "sales_year": 2026, "sales_month": 4, "sales_count": 2, "sales_avg_price": None},
    {"manufacturer_name": "아우디", "vehicle_name": "e-tron GT", "sales_year": 2026, "sales_month": 4, "sales_count": 1, "sales_avg_price": None},  # 원자료 표기: "The new e-tron GT"
    # 매칭 제외(우리 vehicle 테이블에 없음): The new A5 5 / Q6 e-tron 1 (A7은 이번 달 목록에 없음)

    # ── 렉서스 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "렉서스", "vehicle_name": "NX", "sales_year": 2026, "sales_month": 4, "sales_count": 363, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "ES", "sales_year": 2026, "sales_month": 4, "sales_count": 334, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "RX", "sales_year": 2026, "sales_month": 4, "sales_count": 226, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "UX", "sales_year": 2026, "sales_month": 4, "sales_count": 76, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "LX", "sales_year": 2026, "sales_month": 4, "sales_count": 36, "sales_avg_price": None},
    {"manufacturer_name": "렉서스", "vehicle_name": "LS", "sales_year": 2026, "sales_month": 4, "sales_count": 7, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): LM 37 (IS는 이번 달 목록에 없음)

    # ── 볼보 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "볼보", "vehicle_name": "XC60", "sales_year": 2026, "sales_month": 4, "sales_count": 359, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "XC90", "sales_year": 2026, "sales_month": 4, "sales_count": 184, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "EX30", "sales_year": 2026, "sales_month": 4, "sales_count": 145 + 101, "sales_avg_price": None},  # EX30 145 + EX30 CC 101
    {"manufacturer_name": "볼보", "vehicle_name": "S90", "sales_year": 2026, "sales_month": 4, "sales_count": 144, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "XC40", "sales_year": 2026, "sales_month": 4, "sales_count": 133, "sales_avg_price": None},
    {"manufacturer_name": "볼보", "vehicle_name": "V60", "sales_year": 2026, "sales_month": 4, "sales_count": 39, "sales_avg_price": None},  # 원자료 표기: "V60 Cross Country"
    # S60, EX90은 이번 달 목록에 없음 -> 스킵

    # ── 토요타 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "토요타", "vehicle_name": "캠리", "sales_year": 2026, "sales_month": 4, "sales_count": 239, "sales_avg_price": None},  # 원자료 표기: "Camry"
    {"manufacturer_name": "토요타", "vehicle_name": "프리우스", "sales_year": 2026, "sales_month": 4, "sales_count": 148, "sales_avg_price": None},  # 원자료 표기: "Prius"
    {"manufacturer_name": "토요타", "vehicle_name": "시에나", "sales_year": 2026, "sales_month": 4, "sales_count": 67, "sales_avg_price": None},  # 원자료 표기: "Sienna"
    {"manufacturer_name": "토요타", "vehicle_name": "하이랜더", "sales_year": 2026, "sales_month": 4, "sales_count": 43, "sales_avg_price": None},  # 원자료 표기: "Highlander"
    {"manufacturer_name": "토요타", "vehicle_name": "GR86", "sales_year": 2026, "sales_month": 4, "sales_count": 24, "sales_avg_price": None},  # 원자료 표기: "GR 86"
    {"manufacturer_name": "토요타", "vehicle_name": "RAV4", "sales_year": 2026, "sales_month": 4, "sales_count": 2, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): Alphard 174 / Crown 132 (코롤라·코롤라 크로스는 이번 달 목록에 없음)

    # ── 미니 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "미니", "vehicle_name": "쿠퍼", "sales_year": 2026, "sales_month": 4, "sales_count": 314, "sales_avg_price": None},  # 원자료 표기: "Cooper"
    {"manufacturer_name": "미니", "vehicle_name": "컨트리맨", "sales_year": 2026, "sales_month": 4, "sales_count": 146 + 27, "sales_avg_price": None},  # Countryman 146 + Countryman Electric 27
    {"manufacturer_name": "미니", "vehicle_name": "쿠퍼 SE", "sales_year": 2026, "sales_month": 4, "sales_count": 94, "sales_avg_price": None},  # 원자료 표기: "Mini Electric"
    # 매칭 제외(우리 vehicle 테이블에 없음): Aceman 72 / Convertible 43 (쿠퍼 S는 이번 자료에 별도 표기 없음)

    # ── 포르쉐 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "포르쉐", "vehicle_name": "카이엔", "sales_year": 2026, "sales_month": 4, "sales_count": 246, "sales_avg_price": None},  # 원자료 표기: "Cayenne"
    {"manufacturer_name": "포르쉐", "vehicle_name": "타이칸", "sales_year": 2026, "sales_month": 4, "sales_count": 155, "sales_avg_price": None},  # 원자료 표기: "Taycan"
    {"manufacturer_name": "포르쉐", "vehicle_name": "마칸", "sales_year": 2026, "sales_month": 4, "sales_count": 122, "sales_avg_price": None},  # 원자료 표기: "Macan Electric"
    {"manufacturer_name": "포르쉐", "vehicle_name": "파나메라", "sales_year": 2026, "sales_month": 4, "sales_count": 80, "sales_avg_price": None},  # 원자료 표기: "Panamera"
    {"manufacturer_name": "포르쉐", "vehicle_name": "911", "sales_year": 2026, "sales_month": 4, "sales_count": 76, "sales_avg_price": None},  # 원자료 표기: "The New 911"
    # 카이맨은 이번 달 목록에 없음 -> 스킵

    # ── 폭스바겐 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "폭스바겐", "vehicle_name": "ID.4", "sales_year": 2026, "sales_month": 4, "sales_count": 196, "sales_avg_price": None},
    {"manufacturer_name": "폭스바겐", "vehicle_name": "골프", "sales_year": 2026, "sales_month": 4, "sales_count": 169, "sales_avg_price": None},  # 원자료 표기: "Golf"
    {"manufacturer_name": "폭스바겐", "vehicle_name": "아틀라스", "sales_year": 2026, "sales_month": 4, "sales_count": 75, "sales_avg_price": None},  # 원자료 표기: "Atlas"
    # 매칭 제외(우리 vehicle 테이블에 없음): Touareg 18 (티구안·파사트·아테온·ID.5·ID.7은 이번 달 목록에 없음)

    # ── 혼다 (2026년 4월) ──────────────────────────────
    {"manufacturer_name": "혼다", "vehicle_name": "CR-V", "sales_year": 2026, "sales_month": 4, "sales_count": 65, "sales_avg_price": None},
    # 매칭 제외(우리 vehicle 테이블에 없음): Odyssey 1
]


def get_vehicle_map():
    """(manufacturer_name, vehicle_name) -> vehicle_id 매핑 반환"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT v.vehicle_id, v.vehicle_name, m.manufacturer_name
        FROM vehicle v
        JOIN manufacturer m ON v.manufacturer_id = m.manufacturer_id
        """
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {(mname, vname): vid for vid, vname, mname in rows}


def get_estimated_price_map():
    """
    vehicle_id -> 추정 평균가 매핑 반환.
    vehicle_detail에 등록된 트림들의 detail_base_price 평균을 사용함.
    (실거래가 공식 통계가 없어서 카탈로그 가격 기준 추정치로 대신함)
    트림 정보가 하나도 없는 vehicle_id는 매핑에서 빠짐(그 경우 sales_avg_price는 NULL로 남음).
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT vehicle_id, AVG(detail_base_price)
        FROM vehicle_detail
        WHERE detail_base_price IS NOT NULL
        GROUP BY vehicle_id
        """
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {vid: round(avg_price) for vid, avg_price in rows}


def insert_sales_stats(records):
    vehicle_map = get_vehicle_map()
    price_map = get_estimated_price_map()

    conn = get_db_connection()
    cur = conn.cursor()

    # 이미 들어가있는 (vehicle_id, year, month) 조합 조회 -> 중복 방지
    cur.execute("SELECT vehicle_id, sales_year, sales_month FROM sales_stat")
    existing = set(cur.fetchall())

    sql = """
        INSERT INTO sales_stat (sales_year, sales_month, sales_count, sales_avg_price, vehicle_id)
        VALUES (%s, %s, %s, %s, %s)
    """

    saved, skipped, no_match, no_price = 0, 0, [], []
    for r in records:
        if r.get("sales_year") is None or r.get("sales_month") is None:
            print(f"[연/월 미입력, 스킵] {r['manufacturer_name']} {r['vehicle_name']}")
            skipped += 1
            continue

        key = (r["manufacturer_name"], r["vehicle_name"])
        vehicle_id = vehicle_map.get(key)
        if vehicle_id is None:
            no_match.append(f"{r['manufacturer_name']} {r['vehicle_name']}")
            skipped += 1
            continue

        if (vehicle_id, r["sales_year"], r["sales_month"]) in existing:
            print(f"[이미 있음, 스킵] {r['manufacturer_name']} {r['vehicle_name']} {r['sales_year']}-{r['sales_month']}")
            skipped += 1
            continue

        # sales_avg_price가 명시적으로 채워져 있으면 그 값을 쓰고,
        # 없으면(None) vehicle_detail 트림 평균가로 추정치를 채움
        avg_price = r.get("sales_avg_price")
        if avg_price is None:
            avg_price = price_map.get(vehicle_id)
            if avg_price is None:
                no_price.append(f"{r['manufacturer_name']} {r['vehicle_name']}")

        cur.execute(
            sql,
            (
                r["sales_year"],
                r["sales_month"],
                r.get("sales_count"),
                avg_price,
                vehicle_id,
            ),
        )
        existing.add((vehicle_id, r["sales_year"], r["sales_month"]))
        saved += 1
        price_note = f", 추정가={avg_price:,}원" if avg_price else ""
        print(f"저장: {r['manufacturer_name']} {r['vehicle_name']} {r['sales_year']}-{r['sales_month']} -> {r['sales_count']}대{price_note}")

    conn.commit()
    cur.close()
    conn.close()

    print(f"\n총 {saved}개 저장 완료 / {skipped}개 스킵")
    if no_match:
        print("\nvehicle 테이블에서 매칭 안 된 모델 (이름 확인 필요):")
        for n in no_match:
            print(f"  - {n}")
    if no_price:
        print("\nvehicle_detail에 트림 가격이 없어서 sales_avg_price가 NULL로 들어간 모델:")
        for n in no_price:
            print(f"  - {n}")


if __name__ == "__main__":
    insert_sales_stats(sales_records)
# 운송수단별 탄소배출량 (kg CO2/km)
transport_emissions = {
    "트럭": 0.2,
    "선박": 0.015,
    "항공기": 0.5,
    "전기차": 0.05
}

# 포장재별 탄소배출량 (kg CO2/1개)
package_emissions = {
    "비닐": 0.1,
    "종이": 0.05,
    "재활용 종이": 0.02,
    "식물성 포장": 0.01
}

# 탄소 배출량 계산 함수
def calculate_emissions(distance_km, transport_type, package_type):
    if transport_type not in transport_emissions:
        raise ValueError("운송수단을 잘못 입력했습니다.")
    if package_type not in package_emissions:
        raise ValueError("포장재를 잘못 입력했습니다.")

    transport_emission = transport_emissions[transport_type]
    package_emission = package_emissions[package_type]
    
    total_emission = distance_km * transport_emission + package_emission
    return round(total_emission, 4)

# 🌱 친환경 점수 시스템
def get_eco_score(emission):
    if emission < 1:
        return "🌟 매우 친환경적 (Eco Score: A)"
    elif emission < 5:
        return "👍 보통 (Eco Score: B)"
    else:
        return "⚠️ 개선 필요 (Eco Score: C)"

# 🔁 시뮬레이션 예시
if __name__ == "__main__":
    # 예시 데이터
    distance = 1200  # km
    transport = "선박"
    packaging = "재활용 종이"

    emission = calculate_emissions(distance, transport, packaging)
    score = get_eco_score(emission)

    print(f"총 탄소배출량: {emission} kg CO2")
    print(f"친환경 점수: {score}")

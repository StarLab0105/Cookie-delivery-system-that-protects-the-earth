import math
import matplotlib.pyplot as plt
import numpy as np

# 운송수단별 CO₂ 배출 계수 (kgCO₂/km)
transport_emission_factors = {
    "truck": 0.2,
    "ship": 0.015,
    "airplane": 0.5,
    "electric_car": 0.05,
    "bicycle Electric" : 0.005,
    "hydrogen car" : 0.25,
    "hydrogen truck" : 0.15 
}

# 포장재별 CO₂ 배출 계수 (kgCO₂/package)
packaging_emission_factors = {
    "plastic": 0.2,
    "paper": 0.1,
    "recycled paper": 0.05,
    "wooden" : 0.15,
    "vinyl" : 0.05,
    "iron" : 0.35,
    "glass" : 0.05,
    "styrofoam" : 0.25
}

# 샘플 도시의 위도/경도 (임의)
locations = {
    "seoul": (37.5665, 126.9780),
    "busan": (35.1796, 129.0756),
    "newyork": (40.7128, -74.0060),
    "tokyo": (35.6895, 139.6917),
    "berlin": (52.5200, 13.4050),
    "washington DC" : (45,116),
    "paris" : (48,2)
}

# haversine 거리 계산
def calculate_distance(coord1, coord2):
    R = 6371  # 지구 반지름 (km)
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

# 점수 계산
def calculate_eco_score(transport_emission, packaging_emission):
    total_emission = transport_emission + packaging_emission
    eco_score = max(0, 100 - int(total_emission * 7.00))
    return total_emission, eco_score

# 사용자 입력
def run_simulation():
    print("🚚 에코 쿠키 배송 시뮬레이터 🌱")
    print("사용 가능한 도시:", list(locations.keys()))

    origin = input("출발지(공장 위치): ").lower()
    destination = input("배송지(고객 위치): ").lower()

    transport = input("운송수단 (truck, ship, airplane, electric_car, bicycle Electric, hydrogen car,hydrogen truck): ").lower()
    packaging = input("포장재 (plastic, paper, recycled_paper, wooden, vinyl, iron, glass, styrofoam): ").lower()

    if origin not in locations or destination not in locations:
        print("⚠️ 유효하지 않은 도시명입니다.")
        return

    if transport not in transport_emission_factors:
        print("⚠️ 유효하지 않은 운송수단입니다.")
        return

    if packaging not in packaging_emission_factors:
        print("⚠️ 유효하지 않은 포장재입니다.")
        return

    distance = calculate_distance(locations[origin], locations[destination])
    transport_emission = distance * transport_emission_factors[transport]
    packaging_emission = packaging_emission_factors[packaging]

    total_emission, eco_score = calculate_eco_score(transport_emission, packaging_emission)

    print("\n📦 배송 결과:")
    print(f"  - 거리: {distance:.2f} km")
    print(f"  - 운송 탄소 배출: {transport_emission:.3f} kgCO₂")
    print(f"  - 포장 탄소 배출: {packaging_emission:.3f} kgCO₂")
    print(f"  ✅ 총 탄소 배출량: {total_emission:.3f} kgCO₂")
    print(f"  🌿 친환경 점수: {eco_score}/100")

    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)

    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    plt.subplot(2, 1, 1)                # nrows=2, ncols=1, index=1
    y = np.arange(3)
    Type = ['transport_emission', 'packaging_emission', 'total_emission']
    values = [transport_emission,packaging_emission,total_emission]
    colors = ['y', 'dodgerblue', 'C2']
    plt.barh(y, values, color=colors,height=0.4)
    plt.yticks(y, Type)

    plt.subplot(2, 1, 2)           
    ratio = [ 100-eco_score,eco_score]
    labels = ['BAD_eco_score','GOOD_eco_score']
    explode = [0.1, 0.1]
    colors = ['#ff9999', '#8fd9b6']
    plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode, shadow=True, colors=colors)
    plt.tight_layout()
    plt.show()

    if eco_score < 70:
        print("⚠️ 더 친환경적인 선택을 고려해보세요!")
        if transport != "electric_car":
            print("  👉 전기차를 선택하면 탄소를 크게 줄일 수 있어요!")
        if packaging != "recycled_paper":
            print("  👉 재활용 종이를 사용해보는 건 어때요?")

# 실행
if __name__ == "__main__":
    run_simulation()

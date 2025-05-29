import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 오류 해결 >>> 시각화 필요

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
    "plastic": 30,
    "paper": 15,
    "recycled paper": 7.5,
    "wooden" : 7.5,
    "vinyl" : 6,
    "iron" : 35,
    "glass" : 25,
    "styrofoam" : 40
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
def calculate_eco_score(transport_emission, packaging_emission,distance):
    total_emission = transport_emission + packaging_emission
    emsision_per = distance / total_emission
    eco_score = max(0, 100 - int(emsision_per))
    return total_emission, eco_score

# 사용자 입력
def run_simulation():
    print("🚚 에코 쿠키 배송 시뮬레이터 🌱")
    print("사용 가능한 도시:", list(locations.keys()))
    locations_caculate = ["seoul","busan","newyork","tokyo","berlin","washington DC","paris"]
    distance_list = []
    city_list = []
    transport_emission_list =[]
    total_emission_list = [0] * 6
    eco_score_list = [0] * 6
    origin = input("출발지(공장 위치): ").lower()
    transport = input("운송수단 (truck, ship, airplane, electric_car, bicycle Electric, hydrogen car,hydrogen truck): ").lower()
    packaging = input("포장재 (plastic, paper, recycled_paper, wooden, vinyl, iron, glass, styrofoam): ").lower()

    if origin not in locations not in locations:
        print("⚠️ 유효하지 않은 도시명입니다.")
        return

    if transport not in transport_emission_factors:
        print("⚠️ 유효하지 않은 운송수단입니다.")
        return

    if packaging not in packaging_emission_factors:
        print("⚠️ 유효하지 않은 포장재입니다.")
        return

    for i in locations_caculate:
        if i == origin:
            continue
        else:
            distance = (calculate_distance(locations[origin], locations[i]))
            city_list.append(i)
            distance_list.append(distance)
    for i in range(0,6):
        transport_emission= distance_list[i] * transport_emission_factors[transport]
        transport_emission_list.append(transport_emission)
    packaging_emission = packaging_emission_factors[packaging]
    for i in range(0,6):
        total_emission_list[i], eco_score_list[i] = calculate_eco_score(transport_emission_list[i], packaging_emission,distance_list[i])
    print("\n\n")
    print("전체 탄소 배출량",total_emission_list)
    print("친환경 점수",eco_score_list)
    print("포장지 배출량",packaging_emission)
    print("운송수단 배출량",transport_emission_list)
    print("거리 목록",distance_list)
    print("도시목록",city_list)
    Title = "Origin : {} \n Transport : {} \n Packaging : {}".format(origin,transport,packaging)
    p1 = plt.bar(city_list, transport_emission_list, color='red', alpha=0.7, label='transport_emission')
    p2 = plt.bar(city_list, packaging_emission, color='blue', alpha=0.7, bottom=transport_emission_list, label='packaging_emission')
    plt.title(Title)
    plt.xlabel("City", labelpad=20)
    plt.ylabel("Total emission (kg CO2)", labelpad=-1)
    plt.legend(frameon=True, shadow=True, facecolor='inherit', edgecolor='green', borderpad=0.8, labelspacing=1.1)
    plt.show()

 
# 실행
if __name__ == "__main__":
    run_simulation()

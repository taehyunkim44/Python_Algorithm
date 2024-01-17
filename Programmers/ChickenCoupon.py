# 프로그래머스 치킨 쿠폰
def solution(chicken):
    coupons = chicken
    service_chickens = 0
    
    while coupons >= 10:
        service_chickens += coupons // 10
        coupons = coupons % 10 + coupons // 10

    return service_chickens

# 프로그래머스 유한소수 판별하기
def gcd(a, b):
    # 최대공약수(GCD)를 계산하는 함수
    while b:
        a, b = b, a % b
    return a

def solution(a, b):
    # 기약분수로 나타내기 위해 최대공약수(GCD)를 계산
    common_divisor = gcd(a, b)
    
    # 분모(b)를 최대공약수로 나누어 기약분수로 만듦
    reduced_a = a // common_divisor
    reduced_b = b // common_divisor
    
    # 분모(b)의 소인수가 2와 5만 포함되어 있는지 확인
    while reduced_b % 2 == 0:
        reduced_b //= 2
    while reduced_b % 5 == 0:
        reduced_b //= 5
    
    # 기약분수로 만든 후에 분모(b)가 1이면 유한소수, 그렇지 않으면 무한소수
    if reduced_b == 1:
        return 1
    else:
        return 2

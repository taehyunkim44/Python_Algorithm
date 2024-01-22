# 프로그래머스 특이한 정렬

def solution(numlist, n):
    # numlist의 원소를 n으로부터의 거리를 기준으로 정렬
    numlist.sort(key=lambda x: (abs(x - n), -x))

    return numlist

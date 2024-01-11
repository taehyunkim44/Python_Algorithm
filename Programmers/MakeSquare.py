#  프로그래머스 정사각형 만들기

def solution(arr):
    row = len(arr)
    col = len(arr[0])

    max_size = max(row, col)

    for i in range(row):
        arr[i] += [0] * (max_size - col)
    
    if row < col:
        for _ in range(col - row):
            arr.append([0] * max_size)
    
    return arr
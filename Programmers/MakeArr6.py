# 프로그래머스 배열 만들기6
def solution(arr):
    stk = []
    
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                stk.pop()
                i += 1
            elif stk[-1] != arr[i]:
                stk.append(arr[i])
                i += 1
    
    if len(stk) == 0:
        return [-1]
    
    return stk
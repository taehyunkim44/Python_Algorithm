# 프로그래머스 OX퀴즈
def solution(quiz):
    answer = []
    for i in quiz:
        answer.append(ox(i))
    return answer

def ox(str):
    list = str.split(" ")
    if list[1] == "-":
        if int(list[0]) - int(list[2]) == int(list[4]):
            return "O"
        else:
            return "X"
    else:
        if int(list[0]) + int(list[2]) == int(list[4]):
            return "O"
        else:
            return "X"
        
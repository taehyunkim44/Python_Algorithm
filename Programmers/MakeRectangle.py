// 프로그래머스 직사각형 넓이 구하기
def solution(dots):
    # 네 꼭짓점의 좌표에서 x와 y의 최소값과 최대값을 찾음
    min_x = min(dots[0][0], dots[1][0], dots[2][0], dots[3][0])
    max_x = max(dots[0][0], dots[1][0], dots[2][0], dots[3][0])
    min_y = min(dots[0][1], dots[1][1], dots[2][1], dots[3][1])
    max_y = max(dots[0][1], dots[1][1], dots[2][1], dots[3][1])

    # 가로와 세로 길이 계산
    width = max_x - min_x
    height = max_y - min_y

    # 넓이 계산
    area = width * height

    return abs(area)  # 넓이는 항상 양수이므로 절댓값 처리
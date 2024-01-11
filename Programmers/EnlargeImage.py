#  프로그래머스 그림확대
def solution(picture, k):
    # 그림 파일의 높이와 너비 계산
    height = len(picture)
    width = len(picture[0])

    # k배 확대한 그림의 높이와 너비 계산
    new_height = height * k
    new_width = width * k

    # k배 확대한 그림을 저장할 리스트 초기화
    result = []

    # 원본 그림을 k배 확대하여 result 리스트에 저장
    for i in range(new_height):
        original_row = picture[i // k]  # 원본 그림에서 가져올 행
        new_row = ""  # k배 확대한 행 초기화

        for j in range(new_width):
            new_row += original_row[j // k]  # 원본 픽셀 값을 k번 반복하여 추가

        result.append(new_row)  # k배 확대한 행을 결과 리스트에 추가

    return result
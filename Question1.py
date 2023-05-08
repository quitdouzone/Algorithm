## Qusetion1
# 자세한내용 : https://www.acmicpc.net/problem/23971
# 2021년 12월, 네 번째로 개최된 ZOAC의 오프닝을 맡은 성우는 오프라인 대회를 대비하여 강의실을 예약하려고 한다.
#
# 강의실에서 대회를 치르려면 거리두기 수칙을 지켜야 한다!
#
# 한 명씩 앉을 수 있는 테이블이 행마다 W개씩 H행에 걸쳐 있을 때, 모든 참가자는
# 세로로 N칸 또는 가로로 M칸 이상 비우고 앉아야 한다. 즉, 다른 모든 참가자와
# 세로줄 번호의 차가 N보다 크거나 가로줄 번호의 차가 M보다 큰 곳에만 앉을 수 있다.
#
# 논문과 과제에 시달리는 성우를 위해 강의실이 거리두기 수칙을 지키면서 최대 몇 명을 수용할 수 있는지 구해보자.


def solution(H, W, N, M):
    answer = 0
    seat_position = []
    full_seat_cnt = 0

    for i in range(0, H, M+1):
        for j in range(0, W, N+1):
            full_seat_cnt += 1
            print(i, j, full_seat_cnt)

    answer = full_seat_cnt
    return answer

def submit_code(data:str): #호율성 오류 정답확인
    input_data_list = input().split(' ')
    #input_data_list = data.split(' ')
    full_seat_cnt = 0
    H = int(input_data_list[0])
    W = int(input_data_list[1])
    N = int(input_data_list[2])
    M = int(input_data_list[3])

    for i in range(0, H, M + 1): #이중 반복문 시간복잡도 O(n2)
        for j in range(0, W, N + 1):
            full_seat_cnt += 1
            print(i, j, full_seat_cnt)
    answer = full_seat_cnt
    return answer

def answer():
    # 이번 문제 오류원인 구현이 아닌 단순 수치계산으로 접근하여함
    # 단순하게 접근하면 더 쉽게 풀릴 문제 답을 찾아가는 방식의 다각화 필요
    # 해당 문제 접근 방식
            # 전체 5칸, 띄어앉아야 하는 길이가 4일 때(5/5=1) 딱 1명이 들어오며,
            # 띄어앉아야 하는 길이가 3으로 줄어들 때(5/4=1.25) 1명이 추가되며,
            # 띄어앉아야 하는 길이가 2로 줄어들 때(5/3=1.67) 인원이 변하지 않으며,
            # 띄어앉아야 하는 길이가 1로 줄어들 때(5/2=2/5) 1명이 더 추가되는 규칙이 발견된다
    import math
    H, W, N, M = list(map(int, input().split(' '))) # map 함수를 활용한 리스트 언팩킹 방식 활용하여 코드 간결하게 표현
    print(H, W, N, M)
    max_row = math.ceil(W/(M+1))
    max_col = math.ceil(H/(N+1))
    print(max_row, max_col)
    answer = max_row * max_col
    return answer


if __name__ == '__main__':
    #answer = submit_code('5 4 1 1')
    answer = answer()
    print(answer)
## Qusetion2
# 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.
#
# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다.
# 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.
#
# 세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

def solution():
    while True:
        a, b, c = list(map(int, input().split(' ')))
        if a == 0 and b == 0 and c == 0:
            print('')
        else:
            # 삼각형 구분
            # max_tri_var = max([a, b, c])
            # list_1 = [a, b, c]
            # list_1.remove(max_tri_var)
            sorted_list = sorted([a, b, c])
            print(sorted_list)
            #print(list_1)
            if sorted_list[2] >= sum(sorted_list[:-1]):
                print('Invalid')
            elif a == b:
                if a == c:
                    print('Equilateral')
                else:
                    print('Isosceles')
            elif a == c:
                if b == c:
                    print('Equilateral')
                else:
                    print('Isosceles')
            elif b == c:
                if a == c:
                    print('Equilateral')
                else:
                    print('Isosceles')
            else:
                print('Scalene')



if __name__ == '__main__':
    solution()
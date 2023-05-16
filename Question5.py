#Question5

# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
#
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.


def solution(): # Key Error?
    result = set()
    last_cnt = int(input())
    cnt = 0
    while cnt < last_cnt:
        ordr_value_list = input().split(' ')
        ordr = ordr_value_list[0].lower()
        if ordr != 'all' and ordr != 'empty':
            value = int(ordr_value_list[1])

        if ordr == 'add':
            result.add(value)

        elif ordr == 'remove':
            result.remove(value)

        elif ordr == 'check':
            if value in result:
                print(1)
            else:
                print(0)
        elif ordr == 'toggle':
            if value in result:
                result.pop(value)
            else:
                result.add(value)
        elif ordr == 'all':
            result = set([i for i in range(1, 21)])
        else:
            result = {}
        cnt+=1



if __name__ == '__main__':
    solution()
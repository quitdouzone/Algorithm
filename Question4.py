#Question4

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.


def solution(): #틀렸다고 나오는데 어디가 틀렸는지 모르겠음 외부 라이브러리 사용하면 안되는건가.. 반례가 있나?
    from collections import Counter
    value = input()
    value = value.lower()

    str_list = list(value)
    data_dict = Counter(str_list)
    data_list = list(dict(data_dict).items())
    print(data_list)
    if len(data_list) == 1:
        result = data_list[0][0]
        print(result)
    elif data_list[0][1] != data_list[1][1]:
        result = data_dict.most_common(1)[0][0]
        print(result)
    else:
        print('?')
if __name__ == '__main__':
    solution()
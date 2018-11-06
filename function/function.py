"""
함수란 하나의 기능을 수행하는 코드 묶음을 말함.

* 함수 기본 구조
대괄호로 표시한 항목은 없어도 됩니다.

def 함수이름([입력값1], [입력값2], ...):
    실행할 코드
    [return 반환값]
"""


# 수학에서 배우는 함수처럼 입력값과 출력값이 있는 함수
def do_sum(int1, int2):
    """
    :param int1: 입력값
    :param int2: 입력값
    :return: 함수 결과값
    """
    return int1 + int2


print("sum(5,10) = {}\n".format(do_sum(5, 10)))


# 입력값과 출력값이 없는 함수
def print_hello_world():
    print("hello world\n")


print_hello_world()


# 입력값은 있는데 출력값은 없는 함수
def print_string(string):
    print("{}".format(string))


print_string("input text~!\n")

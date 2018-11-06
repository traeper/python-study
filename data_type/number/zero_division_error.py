int1 = 12

print("0으로 나눌 수 있을까? 아래 주석을 풀어서 실행해보세요.")
# print("{}/{} = {}\n".format(int1, 0, int1 / 0))

"""
ZeroDivisonError?
수를 0으로 나누는 불가능하기에 파이썬은 에러로 취급.
실전 프로그래밍을 할 때 나눗셈을 실행하는 프로그램을 작성한다면 예외처리를 해주는 습관을 가지면 좋을 수 있음.

try:
    division_error = 3 / 0
except ZeroDivisionError as e:
    # safe code, system does not terminate by this error.
    print("ZeroDivisionError " + e.__str__())
"""





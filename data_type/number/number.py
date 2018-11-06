

# 정수 (Integer Number)

int1 = 12
int2 = -12

print("int1 = {}, int2 = {}\n".format(int1, int2))

# 실수 (Floating Number)
float1 = 3.14
float2 = 2.718

print("float1 = {}, float2 = {}\n".format(float1, float2))

# 연산
"""
+: 덧셈
-: 뺄셈
*: 곱셈
/: 나눗셈
//: 몫
%: 나머지
**: 거듭제곱
"""

#############################################
# 나눗셈
#############################################
int3 = 12
int4 = 14
int5 = 7

# 정수 간 나눗셈 연산의 결과는 실수.
print("정수 간 나눗셈 연산의 결과는 실수")
print("{}/{} = {}\n".format(int3, int5, int3 / int5))

# 정수 간 나눗셈이 나누어 떨어지더라도 결과는 실수.
print("정수 간 나눗셈이 나누어 떨어지더라도 결과는 실수")
print("{}/{} = {}\n".format(int4, int5, int4 / int5))

# 정수형 값만 얻고 싶으면 //로 나누어서 몫을 구하거나 int()로 강제 형변환을 시켜줘야 함.
print("소수점 값은 버리고 정수형 값만 얻고 싶으면 //로 나누어서 몫을 구하거나 int()로 강제 형변환을 시켜줘야 함")
print("{}//{} = {}, int(int4/int5) = {}\n".format(int4, int5, int4 // int5, int(int4/int5)))

# 나머지 구하기
print("나머지 구하기")
print("{}%{} = {}\n".format(int3, int5, int3 % int5))

# 정수형 변수를 0으로 나눌 수 있을까? -> zero_division_error.py 확인

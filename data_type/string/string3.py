"""
문자열 연산
"""

# 문자열 합치기
apple = "Apple"
banana = "Banana"

concat = apple + banana
print("문자열 합치기")
print("{}+{} = {}\n".format(apple, banana, concat))

# 문자열 반복하기
repeat_apple = apple * 3
print("문자열 반복하기")
print("{}*3 = {}\n".format(apple, repeat_apple))

"""
문자열 포매팅
"""

# 문자열 대입
print("문자열 대입")
print("My name is %s.\n" % "John")

print("문자열 여러개 대입")
print("first %s, second %s, third %s" % (apple, banana, concat))

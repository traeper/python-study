"""
for 반복문을 이용하면 리스트와 같은 여러 값을 담는 자료형이나 함수에 대해 코드를 반복실행할 수 있음.

continue : 다음 차례로 건너 뜀 실행
"""

arr = [1, 2, 3, 4, 5]

# 숫자 3은 출력 제외
for n in arr:
    if n == 3:
        continue

    print(n)

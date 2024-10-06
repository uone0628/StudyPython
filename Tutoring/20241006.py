# 한 줄 주석

'''
여러 줄 주석
'''



# 변수 : 데이터를 저장하는 공간으로, 이름을 붙여서 사용 (값을 할당할 때 생성)
x = 10  # 정수형 변수
name = "Handong"  # 문자열형 변수

# 데이터 타입
'''
정수(int) : 정수 값을 나타냄
실수(float) : 소수점을 포함한 숫자
문자열(str) : 문자들의 집합, ('') 또는 ("") 으로 감싸야 함
불리언(bool) : 참(True) 또는 거짓(False) 값을 가짐
'''



# 출력 방법
print("Hello, World!")  # 문자열 출력
print(x)  # 변수 x의 값 출력

# 입력 방법
name = input("이름을 입력하세요: ")  # 입력 받기 전 안내 문자 입력 가능
print("안녕하세요, " + name + "님!")  # 여러 데이터 타입을 합쳐서 한 번에 출력 가능



# 데이터 타입 변환
num_str = "10"  # 10을 문자열로 선언
num_int = int(num_str)  # 문자열을 정수로 변환



# 산술 연산자 : 기본적인 수학 연산을 수행
'''
덧셈(+) : 두 수를 더함
뺄셈(-) : 첫 번째 수 - 두 번째 수
곱셈(*) : 두 수를 곱함
나눗셈(/) : 첫 번째 수 / 두 번째 수 (결과는 항상 실수형)
몫(//) : 나눗셈의 결과에서 소수점을 버리고 정수 부분만 반환
나머지(%) : 나눗셈의 나머지를 반환
거듭제곱(**) : 첫 번째 수를 두 번째 수만큼 거듭 제곱 (a의 b제곱)
'''

# 예시
a = 5
b = 3
result = a + b  # result는 8
result = a - b  # result는 2
result = a * b  # result는 15
result = a / b  # result는 1.666...
result = a // b  # result는 1
result = a % b  # result는 2
result = a ** b  # result는 125 (5의 3제곱)



# 비교 연산자 : 두 값을 비교하고, 그 결과를 불리언 값으로 반환
'''
같음(==) : 두 값이 같은지 비교
다름(!=) : 두 값이 다른지 비교
보다 큼(>) : 첫 번째 값 > 두 번째 값
보다 작음(<) : 첫 번째 값 < 두 번째 값
크거나 같음(>=) : 첫 번째 값 >= 두 번째 값
작거나 같음(<=) : 첫 번째 값 <= 두 번째 값
'''

# 예시 (a와 b의 값은 위와 동일)
result = (a == b)  # result는 False
result = (a != b)  # result는 True
result = (a > b)  # result는 True
result = (a < b)  # result는 False
result = (a >= b)  # result는 True
result = (a <= b)  # result는 False



# 논리 연산자 : 불리언 값을 조합하는 데에 사용
'''
AND(and) : 두 조건이 모두 참일 때 True 반환
OR(or) : 두 조건 중 하나라도 참이면 True 반환
NOT(not) : 조건의 반대 값 반환
'''

# 예시 (a와 b의 값은 위와 동일)
result = (a > 0 and b > 0)  # result는 True
result = (a > 0 or b < 0)  # result는 True
result = not (a > 0)  # result는 False



# 대입 연산자 : 변수에 값을 할당할 때 사용
'''
기본 대입(=) : 오른쪽 값을 왼쪽 변수에 할당
복합 대입 연산 : 산술 연산과 대입을 결합
'''

# 예시
x = 10  # 기본 대입
x += 5  # x = x + 5
x -= 2  # x = x - 2
x *= 3  # x = x * 3
x /= 4  # x = x / 4



# 비트 연산자 : 이진수 형태로 값을 조작 (비트 개념까지 안 배우려나..?)
'''
AND(&) : 두 비트가 모두 1일 때 1을 반환
OR(|) : 두 비트 중 하나라도 1이면 1을 반환
XOR(^) : 두 비트가 다를 때 1을 반환
NOT(~) : 비트를 반전
왼쪽 시프트(<<) : 비트를 왼쪽으로 이동
오른쪽 시프트(>>) : 비트를 오른쪽으로 이동
'''
### 비트 연산자도 배운다면 다시 개념 공부해서 알려드리기
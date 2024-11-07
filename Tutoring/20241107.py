# List와 함수의 차이

# 리스트 생성
my_list = [1, 2, 3, 4, 5]

# 리스트에 요소 추가
my_list.append(6)  # [1, 2, 3, 4, 5, 6]

# 리스트에서 요소 삭제
my_list.remove(3)  # [1, 2, 4, 5, 6]

# 인덱스를 사용하여 요소 접근
first_element = my_list[0]  # 1



# 함수 정의
def add_numbers(a, b):
    return a + b

# 함수 호출
result = add_numbers(3, 5)  # 8



# 리스트 생성
numbers = [1, 2, 3, 4, 5]

# 리스트의 모든 요소를 더하는 함수 정의
def sum_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

# 함수 호출
result = sum_list(numbers)  # 15

print(result)
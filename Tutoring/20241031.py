try:
    num = int(input("정수를 입력하세요: "))
    result = 10 / num
except ValueError:
    print("유효한 정수가 아닙니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print(f"결과: {result}")
finally:
    print("프로그램이 종료되었습니다.")

# 2.while.py

while True:
    try:
        number = int(input("정수를 입력하세요: "))
        if number <= 0:
            print("프로그램을 종료합니다.")
            break
        if number % 2 == 0:
            print(f"{number}는 짝수입니다.")
        else:
            print(f"{number}는 홀수입니다.")
    except ValueError:
        print("유효한 정수를 입력해주세요.")

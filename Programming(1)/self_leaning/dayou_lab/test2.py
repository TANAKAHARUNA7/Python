# 첫 번째 수를 두 번째 수로 나누는 프로그램 작성.
# 0으로 나눌 수 없다는 예외 처리

while (True):
    num1 = float(input("첫 번째 수를 입력하세요: "))
    num2 = float(input("두 번째 수를 입력하세요: "))

    if (num2 != 0):
        sum = num1 / num2
        print (num1, "÷", num2, "=", f"{sum:.2f}")
        break
    else:
        print("두 번째 수는 0이외 숫자를 입력하세요.")


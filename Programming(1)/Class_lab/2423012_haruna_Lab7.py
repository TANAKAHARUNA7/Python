# 사용자로부터 두 개의 정수 숫자를 입력 받고, 그 합, 차, 곱, 나눗셈의결과를출력하는 프로그램을 작성한다.
# 사용자에게 두 정수 숫자를 입력 받습니다.
num1 = int(input("첫 번째 숫자를 입력하세요: "))

num2 = int(input("두 번째 숫자를 입력하세요: "))

# 입력받은 숫자들의 합, 차, 곱, 나눗셈 결과를 계산합니다.

sum = num1 + num2 

sub = num1 - num2 

mul = num1 * num2

div = num1 / num2

# 계산된 결과를 출력합니다.

print("합: ",float(sum))
print("차: ",float(sub))
print("곱: ",float(mul))
print("나눗셈: ",float(div))
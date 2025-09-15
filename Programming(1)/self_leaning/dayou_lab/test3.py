
num = 0
while True:
    # 사용자로부터 1부터 10까지의 숫자를 입력 받는다.
    num = int(input("1부터 10까지의 숫자를 입력하세요: "))
    
    if 1 <= num <= 10:
        break
    
# 숫자가 짝수인지 홀수인지 판별
if num % 2 == 0:
    print("홀수입니다")
else:
    print("짝수입니다")

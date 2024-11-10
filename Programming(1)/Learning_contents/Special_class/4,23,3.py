# 정수를 입력받아 입력받은 정수를 출력
# 3의 배수 또는 4의 배수가 입력되면 프로그램 종료
while True:
    num = int(input("정수 입력"))
    
    if num % 3 == 0 or num % 4 == 0:
            print(num)
            break
    
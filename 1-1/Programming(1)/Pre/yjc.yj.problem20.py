# 해당 기능을 실행후 다시 메뉴로 돌아 오는 기능
import random
while True:
    
    # 사용자에게 메뉴를 출력
    print("-" * 20)
    print("1. 구구단 출력")
    print("2. 랜덤값 삼각형 출력")
    print("3. 종료")
    print("-" * 20)
    
    # 입력을 받아 
    menu = int(input("원하는 메뉴 번호를 입력하세요: "))

    if menu == 1:
        
        # 1,구구단 출력
        while True:
            
            # 사용자로부터 출력할 구구단의 범위를 입력받음
            input_num = input("출력하는 구구단을 아래 형식으로 입력하세요: ")
            num_list = input_num.split("~")  # "~"를 뺀 처리
            
            # 입력 값을 정수로 처리
            start = int(num_list[0])
            end = int(num_list[1]) if len(num_list) > 1 else start
            if 2 <= start <= 9 and 2 <= end <= 9:
                for i in range(start, end + 1):
                    for j in range(1,10):
                        print(f"{i} x {j} = {i * j}")
                    print()
                break
            
            # 입력값이2~9 범위를 벗어날 경우 에러메시지를 출력하고 재입력요구
            else:
                print("2~9 사이의 숫자를 입력해수세요.")
    
    # 랜덤값 삼각형 출력         
    elif menu == 2:
        while True:
            
            tliangl = int(input("삼각형의 높이 줄 수를 입력하세요(2이상 2이하)\n"))
            
            random_list = []
            if 2 <= tliangl <= 3:
                for i in range(1, tliangl + 1):
                    for j in range(tliangl - i):
                        print(" " , end="")
                    for u in range(i):
                        while True:
                            random_num = random.randint(0,9)
                            if random_num not in random_list:
                                random_list.append(random_num)
                                break
                        print(random_num , end= "")
                    print()
            else:
                print("2 또는 3을 입력하세요")
    
    elif menu == 3:
        print("프로글래밍 종료.")    
        break
    else:
        print("1~3의 숫자를 입력하세요.")
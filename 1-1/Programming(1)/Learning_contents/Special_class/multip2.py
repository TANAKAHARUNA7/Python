while True:
    print("-----------")
    print("1.구구단 출력")
    print("2.프로그램 종료")
    print("-----------")
    
    menu = input()
    
    if menu == "1":
        num1 = int(input("출력할 구구단의 단을 임력하세요.구구단의 단은 2~9 사이 입력\n"))
        while True:
            for i in range(1,10):
                div = num1 * i
                print(f"{num1} x {i} = {div}")
                break
        print("잘못 입력하셨습니다. 다시 입력하세요.")
    elif menu == "2":
        print("이용해주셔서 감사합니다.")
        break
    else:
        print("잘못 입력하셨습니다.다시 입력하세요.")
        
            
            
            
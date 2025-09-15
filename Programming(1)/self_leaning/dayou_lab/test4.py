list = []
while True:
    # 1번과 0번 중 입력 받는다 
    print("1.숫자 추가")
    print("0.종료 추가")
    choice = int(input("선텍하세요: ")) 

    # 1번 -> 숫자를 입력 받아 리스트에 추가
    if choice == 1:
        num = int(input("숫자를 입력하세요: "))
        list.append(num)
        print(num , "이(가) 리스트에 추가되었습니다.")
        
    # 0번 ->  while문 종료하기
    elif choice == 0:
        print("프로그램 종료합니다.")
        print("최종 리스트: ", list)
        break
    else :
        print("잘 못된 선택입니다. 다시 시도해주세요.")
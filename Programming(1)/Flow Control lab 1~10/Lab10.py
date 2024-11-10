# 컴퓨터가 1부터100 사이의 숫자를 랜덤하게 선택
import random
#input_randomNum = 55
input_randomNum = random.randint(1,100)

# 기회 count 
count = 1
msg = ""

# 맞추기 위한 기회는 10번
while True:
    input_num = int(input(f"{count}/10 -1부터 100 사이의 숫자를 맞춰보세요 (종료하려면 0 입력): "))
    
    # 종료 조건
    # 1, 10번으로 맞추지 못하면 "모든 기회를 사용하였습니다. 정답은 [숫자]입니다."라고 출력.
    if count > 9:
        print(f"모든 기회를 사용하였습니다. 정답은 {input_randomNum}입니다.")
        break
    # 2, 사용자가 0을 입력했을때
    elif input_num == 0:
        break
    # 3, 입력한 숫자 = 컴퓨터가 선택한 숫자 = "정답입니다!"라고 출력되고 게임 종료
    elif input_num == input_randomNum:
            msg = "정답입니다!\n""게임이 끝났습니다."
            print(msg)
            break
        # 사용자 입력 숫자 < 컴퓨터가 선택한 숫자 = "더 큰 숫자입니다."라고 출력
    elif input_num < input_randomNum:
            msg = "더 큰 숫자입니다."
            print(msg)
    # 사용자 입력 숫자 > 컴퓨터가 선택한 숫자 = "더 작은 숫자입니다."라고 출력    
    elif input_num > input_randomNum:
            msg = "더 작은 숫자입니다."   
            print(msg)
    count += 1
     




        
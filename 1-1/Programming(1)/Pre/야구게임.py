space = 4
star = 1

#    *
#   **
#  ***
# ****
for i in range(0,space):
    for j in range(0,star):
        print(" " * i +  "*" * j)
        print()
    print()
    space -= 1
    star += 1


############################################################################
# 컴퓨터가 생성한 중복되지 않는 3개의 난수를 플레이어가 맞추는 게임.
import random

random_num_list = []
random_num_count = 0

# 0~9 사이의 중복되지 않는 정수 3개를 생성.
while random_num_count < 3:
    
    random_num = random.randint(0,9)

    for index in range(random_num_count):
        if random_num_list[index] == random_num:
            break
    else:
        random_num_list.append(random_num)
        random_num_count += 1    
print(random_num_list)
        
# 플레이어부터 0~9 사이의 정수 3개를 입력을 받는다.

count_game = 1
strike_out = 0
msg = "게임 종료"

while True:
    
    strike, ball = 0, 0
    
    print(f"시도 {count_game}: 입력한 숫자 - ",end="")
    input_num = [int(input()) for i in range(3)]


# 플레이어가 입력한 숫자랑 컴퓨터가 생성한 값을 비겨한다.
# strike = 숫자도 자리도 같다
# ball = 같은 숫자가 리스트 안에 있다
# strike out = 리스트 안에 같은 숫자가 하나도 없다 
    for i in range(3):
        for j in range(3):
            if input_num[i] == random_num_list[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
# 결과 출력                    
    if strike == 0 and ball == 0 :
        print("Strike Out")
        strike_out += 1
    else:
        print(f"결과: {strike} Strike, {ball} Ball, Out {strike_out}")
        
# 패배 조건
# 시도 횟수가 5번이상.
# 스트라이크아웃(Strike out) 횟수가 2번 이상.
    if count_game >= 5 or strike_out >= 2:
        msg += ": Strike Out가 2회 초과 " if strike_out >= 2 else ": 패배 (시도 횟수 5회 초과)"
        print(msg)
        break       
# 승리 조건
# 난수 값을 자리 순서대로 모두 맞출 경우
    elif strike == 3:
        msg += ": 승리"
        print(msg)
        break
    else:
        count_game += 1
        
print(f"정답: {random_num_list[0]} {random_num_list[1]} {random_num_list[2]}")
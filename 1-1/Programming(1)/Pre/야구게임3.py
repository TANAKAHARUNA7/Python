# 1.컴퓨터 난수 생성
# 0~9 사이의 중복되지 않는 정수 3개를 생성.
import random

# 0~9의 정수 list를 생성
com_random = [value for value in range(0,10)]
print(com_random)

# List 안의 정수를 랜덤하게 7개 삭재하고 3개의 정수를 남긴다.
for i in range(7):
    del com_random[random.randint(0,len(com_random) -1)]
print(com_random)


# 2.플레이어 입력

game_count = 1
strike_out = 0
msg = "개임 종료: "

while True:
    
    strike = 0
    ball = 0
    
    # 0~9 사이의 정수 3개의 입력을 받는다.
    input_num = input("정수 입력")
    input_num = [int(num) for num in input_num.split() ]
    out_put = print(f"시도 {game_count}: 입력한 숫자 - {input_num[0]} {input_num[1]} {input_num[2]}")

# 반별
    for i in range(3):
        for j in range(3):
            if com_random[i] == input_num[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    
# 3. 결과 출력
    if strike == 0 and ball == 0:
        strike_out += 1
        print(f"{strike} Strike, {ball} Ball, {strike_out} Out,\t") 
    else:
        print(f"{strike} Strike, {ball} Ball")
        
    # 게임 패배 조건    
    # 2.스트라이크 아웃(Strike out) 횟수가 2번 이상.    
    if strike_out >= 2:
        print(f"{msg} 패배 (Strike Out 2회)")
        break
        
    # 1.시도 횟수가 5번 이상.
    elif game_count >= 5:
        print(f"{msg} 패배 (시도 횟수 5회 초과)")
        break
    
    # 게임 승리 조건    
    # 1. 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우.
    if strike == 3:
        print(f"{msg} 승리")
        break
    game_count += 1
    
print(f"정답: {com_random[0]} {com_random[1]} {com_random[2]}")
        









import random

# NO.1
# 0~9 사이의 중복되지 않는 정수 3개를 생성.
random_list = []
random_num_count = 0

while random_num_count < 3:
    
    com_random = random.randint(0,9)
    check = False
    
    for i in range(random_num_count):
        if random_list[i] == com_random:
            check = True
            break
        
    if not check:
        random_list.append(com_random)
        random_num_count += 1
print(random_list)
     
         

count_game = 1
count_strike_out = 0

# No.2
# 플레이어부터 0~9 사이의 정수 3개를 입력을 받는다.
while True:
        
    count_strike, count_ball = 0 , 0
             
    print(f"시도{count_game}: 입력한 숫자 - ")
    input_num = [int(input()) for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if input_num[i] == random_list[j]:
                if i == j:
                    count_strike += 1
                else: 
                    count_ball += 1
                
    # 현재 상황 본석   
    if count_strike == 0 and count_ball == 0 :
        count_strike_out += 1
        print("Strike Out!!")
    else:    
        print(f"결과: {count_strike} Strike, {count_ball} Ball, {count_strike_out} Out")
        
# 게임결과 출력
    # lose
    # 시도 횟수가 5번 이상.
    # 스트라이크 아웃(Strike out) 횟수가 2번 이상.
    if count_game >= 5 or count_strike_out >= 2: 
        msg = '5회 이상 실행' if count_game >= 5 else 'Strike Out 2회 이상' 
        print(f"게임 종료: 패배 {msg}\n정답: {random_list[0]} {random_list[1]} {random_list[2]}")
        break
    
    # Win
    # 난수 값을 자리 순서대로 모두 맞춘 경우
    if count_strike >= 3:
        print(f"게임 종료: 승리\n정답: {random_list[0]} {random_list[1]} {random_list[2]}")
        break
    else:
        count_game += 1
        
        
    
    
          
         
         



# 게임 승리 조건
# 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우
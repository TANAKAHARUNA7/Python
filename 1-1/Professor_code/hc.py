# 빙고게임
# 빙고 줄의 개수(3이상 6이하: O x O)를 입력 받은 후, 1이상 36이하의 중복되지 않는 난수로 빙고판을 모두 채운다.
# 엔터키로 난수를 받아 일치하면 빙고 판의 해당 숫자를 '*'로 바꾸고, 일치하지 않으면 계속 게임이 진행된다.
# 빙고 2줄이 완성되면 게임 승리, 38회 시도 초과이면서 빙고 2줄 미만인 경우 게임 패배

import random

# 빙고 줄의 개수를 입력 받는다.
while True:
    bingo_num = int(input("O x O 빙고 줄의 개수를 입력하세요(3이상 6이하): "))
    if 3 <= bingo_num <= 6:
        break
    else:
        print("3이상 6이하의 숫자를 입력하세요.")

# 1이상 36이하의 중복되지 않는 난수로 빙고판을 채운다.
while True:
    input_change = int(input("1: 빙고판 초기화, 2: 게임 시작(최초 실행은 1): "))
    
    # 1을 선택했을 경우
    if input_change == 1:
        # 빙고보드 생성
        bingo_board = []
        
        # 중복되지 않는 난수로 빙고판을 채운다.
        count = 0
        while True:
            rand_num = random.randint(1, 36)
            for index in range(count):
                if bingo_board[index] == rand_num:
                    break
            else:
                bingo_board.append(rand_num)
                count += 1
            
            if count == bingo_num * bingo_num:
                break
                
        for i in range(bingo_num):
            for j in range(bingo_num):
                print(bingo_board[i * bingo_num + j], "\t", end=" ")
            print()
        
    elif input_change == 2:
        print("게임을 시작합니다.")
        break
    
    else:
        print("1과 2 중 하나를 선택하세요.")
        
# 엔터키로 난수를 받아 빙고판에 숫자가 있으면 해당 숫자를 '*'로 바꾼다.
trial_count = 1
bingo = 0
while trial_count <= 38:
    if bingo == 2:
        print("빙고! 게임을 종료합니다.")
        break
    
    rand_int = random.randint(1, 36)
    enter = input(f"Enter 키를 누르세요. (현재 시도 횟수: {trial_count})")
    for index in range(bingo_num * bingo_num):
        if bingo_board[index] == rand_int:
            bingo_board[index] = "*"
        
    for i in range(bingo_num):
        for j in range(bingo_num):
            print(bingo_board[i * bingo_num + j], "\t", end=" ")
        print()
        
    # 빙고 검사
    # 가로 확인 알고리즘
    # for row in range(bingo_num):
    #     for col in range(bingo_num):
    #         if bingo_board[col + (row * bingo_num)] != "*":
    #             break
    #         else:
    #             bingo += 1

    # # 세로 확인 알고리즘
    # for col in range(bingo_num):
    #     for row in range(bingo_num):
    #         if bingo_board[col + (row * bingo_num)] != "*":
    #             break
    #         else:
    #             bingo += 1

    # # 대각선 : 왼쪽 -> 오른쪽 \
    # for row in range(bingo_num):
    #     if bingo_board[row + (row + bingo_num)] != "*":
    #         break
    #     else:
    #         bingo += 1
        
    # # 대각선 : 오른쪽 -> 왼쪽 /
    # for row in range(bingo_num):
    #     if bingo_board[(row + 1) * (bingo_num - 1)] != "*":
    #         break
    #     else:
    #         bingo += 1
    
    trial_count += 1
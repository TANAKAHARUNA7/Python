

letter_list = ["wlkuoppfn", "joiighjsas","rioenxj"]
# msg = ["첫","두","세"]
# input_letter  = [f"{input(msg[num] + "번째 단어를 입력하세요: ")}"for num in range(3)]

import random


msg = ["첫","두","세"]
letter_list = []
count = 0

# 단어 입력 받는다
while count < 3:
    
    # 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장합니다.
    input_letter = (input(msg[count] + "번째 단어를 입력하세요: "))
    
    # 단어의 글자 범위는 5 이상, 20 이하로 제한됩니다.
    if 5 <= len(input_letter) <= 20:
        letter_list.append(input_letter)
        count += 1
    else:
        print("5 이상, 20 이하로 입력하세요.")
print(letter_list)


# 2. 단어 선택
# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택합니다.
ran_letter = letter_list[random.randint(0,2)]
print(f"단어 선텍 완료 게임을 시작합니다. 선텍된 단어: {ran_letter}")

ran_letter = list(ran_letter)
# 3. 게임 시작
# 선택된 단어의 글자 50%를 구한다

ran_letter_half = len(ran_letter) / 2
print(ran_letter_half)

# 올림처리
if ran_letter_half % 2 != 0:
    ran_letter_half = len(ran_letter) // 2 + 1

print(ran_letter_half)

# 단어 글짜를 하나씩 원소화
ran_letter_index = []
for i in range(len(ran_letter)):
    ran_letter_index.append(i)
print(ran_letter_index)

# Blind 처리하는 index를 randam하게 선텍한다.    
for i in range(len(ran_letter) - ran_letter_half):
    del ran_letter_index[random.randint(0,ran_letter_half)]
print(ran_letter_index)

# 답장용 list 와 따로 blind 처리하는 list를 생성
copy_letter = ran_letter[:]
# print(copy_letter)

# 선택 단어를 Blind화
for blind in ran_letter_index:
    copy_letter[blind] = "_"
# print(copy_letter)

# 4. 알파벳 입력
# 키보드로부터 알파벳 한 글자를 입력받습니다.
game_count = 1

while True:
    
    print(f"{game_count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.")
    print(copy_letter)
    
    input_word = input()
    
    if input_word in ran_letter:
        for i in ran_letter_index:
            if ran_letter[i] == input_word:
                copy_letter[i] = input_word
                print(copy_letter)
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")
    game_count += 1

# 5. Blind 해제
    if copy_letter == ran_letter:
        break

print(f"성공. 시도 횟수 : {game_count}")
    # 입력받은 알파벳이 단어 내에 존재할 경우 Blind를 해제합니다.

    # 존재하지 않을 경우 “없음” 메시지를 출력합니다


       
# 6. 게임 종료
# 단어의 모든 글자를 맞출 경우 게임이 종료되고 게임 시도 횟수를 출력
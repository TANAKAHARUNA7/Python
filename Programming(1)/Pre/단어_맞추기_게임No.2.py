# 단어 입력
# 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장합니다.
# input_word = [♡]

import random

# letter_list = []
# count1 = 0
# while count1 < 3:
  
#     msg = ["첫", "두", "세"]
    
#     input_word = input(f"{msg[count1]} 번째 문자를 입력하세요")
    
#     # 단어의 글자 범위는 5 이상, 20 이하로 제한됩니다.
#     if not 5 <= len(input_word) <= 20:
#         print("5~20글자로 작성하세요.")
#     else:
#         letter_list.append(input_word)
#         count1 += 1       

# print(letter_list)
 
letter_list = ["asdfghj","werty","klfhuo"]
 
    
# 2. 단어 선택
# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택합니다.
random_letter = random.choice(letter_list)
print(random_letter)

# 3. 게임 시작
# 선택된 단어의 글자 50%를 구한다
random_list_halfu = len(random_letter) / 2
print(random_list_halfu)

# 올림처리
if random_list_halfu % 2 != 0:
    random_list_halfu = random_list_halfu + 0.5
    random_list_halfu = int(random_list_halfu)
print(random_list_halfu) 

# Blind 처리된 알파벳을 랜덤하게 선택.
index_list = []
for index in range(len(random_letter)):
    index_list.append(index)
print(index_list)

for i in range(len(random_letter) - random_list_halfu):
    del index_list[random.randint(0,random_list_halfu)]
print(index_list)
# 답장용 list 와 따로 blind 처리하는 list를 생성
blind_letter = list(random_letter[:]) 

# 선택 단어 글자 중 50% Blind
for i in index_list:
    blind_letter[i] = "_" 
print(blind_letter)
random_letter = list(random_letter)

# 4. 알파벳 입력
# 키보드로부터 알파벳 한 글자를 입력받습니다.
# 5. Blind 해제

count = 1
while True:
    
    word = input("글자 입력")
    
    # 입력받은 알파벳이 단어 내에 존재할 경우 Blind를 해제합니다.
    if word in random_letter:
        for i in index_list:
            if word == random_letter[i]:
                blind_letter[i] = word
        print(blind_letter)
    # 존재하지 않을 경우 “없음” 메시지를 출력합니다
    else:
        print("없음")
        continue
    
    count+= 1 
       
# 6. 게임 종료
# 단어의 모든 글자를 맞출 경우 게임이 종료되고 게임 시도 횟수를 출력
    if blind_letter == random_letter:
        print(f"성공.시도 횟수{count}번")
        break


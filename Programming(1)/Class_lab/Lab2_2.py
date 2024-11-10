# 중복 값이 없는 정수의 개수
import random

trail_num = int(input("N값을 입력하세요: "))
# 중복
made_list = []

for trai_count in range(0, trail_num):
    
    while True:
        random_num = random.randint(1,100)
        found_duplication = False
          #重複の有無を確認
        for made_index in range(0, trai_count):
            if made_list [made_index] == random_num:
                found_duplication = True
                break
          #重複してない数字のリスト
        if not found_duplication:
            made_list.append(random_num)
            break
 # 重複していない数字を出力       
print(made_list)   
 # 元素の長さを確認し  
while True:
    input_index = int(input("index: "))
    # 位置を出力 
    if 0 <= input_index < len(made_list):
        print("원소 값: ", made_list[input_index]) 
        break   
    print("out of index")
    
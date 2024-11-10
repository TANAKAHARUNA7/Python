# コンピュータが生成した3つの重複しない乱数を推測する野球ゲーム
import random

# 0 ~ 9 の間の重複しない整数を 3 つ生成
def com_random(random_num1 , random_num2 , random_numValue):

    com_num_list = []
    com_num_count = 0
   
    while com_num_count < random_numValue: 
        
        com_num = random.randint(random_num1,random_num2)
        
        num_check = False
        
        for index in range(com_num_count):
            if  com_num_list[index] == com_num:
                num_check = True
                break
            
        if not num_check:
            com_num_list.append(com_num)
            com_num_count += 1
            
    return com_num_list

com_random(0, 9, 3)


input_count = 0

while input_count > 5:

    # 0 ~ 9　の間の整数の入力を受ける
    input_num = [int(input()) for i in range(3)]
    print(f"開始{input_count}: 入力した数字‐ {input_num}")
          
# strike判定 数字の位置が同じ
    for i in input_num:
        for j com_random:
    

# ball判定　位置は違うが同じ数字がある

# out判定　数字も位置も違う


# 敗北条件
# 1. 5回以上挑戦する
# 2.　strike　out回数が2回以上の場合


# 勝利条件
# プレイアーが乱数すべてを当てた場合
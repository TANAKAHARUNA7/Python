# ユーザよりサイコロを振る回数（範囲：100～10000）の入力を受ける

import random

while True:
    trial_value = int(input("100~10000までの整数を入力してください"))
    if 100 <= trial_value <= 10000:
        break

# 無効な数字は再入力を受ける

# サイコロの目（1～6までの数字）の出現回数をカウントするリストを生成
# サイコロの目　1  2  3  4  5  6
random_list = [0, 0, 0, 0, 0, 0]

# 指定された回数分サイコロを振る
for i in range(trial_value):
    randam_num = random.randint(1,6)
    random_list[randam_num - 1] += 1

max = 0   
for i in range(6):
    if random_list[i] > max :  # サイコロの目の中で一番多く出た数を求める
        max = random_list[i]
 
          
for i in range(6):    
    # 結果をヒストグラムで視覚化 ""
    star = random_list[i] / max * 10
    # 確率を求める
    kakuritu = random_list[i] / trial_value * 100
        
    # 出現回数と確率を表示
    print(f"{i+ 1}:\t",end="")
    print("*" * int(star),"\t", end="")
    print(f"({random_list[i]} times, {kakuritu}%)")



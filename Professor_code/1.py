  
import random
d1, d2, d3, d4, d5, d6 = 0,0,0,0,0,0
max_num = 0
max_star = "*" * 10
# 1,ユーザ入力
while True:
    
    # ユーザから100～1,000,000 範囲内でサイコロを振る回数の入力を受ける
    input_train = int(input("Enter the number of dice rolls(between 100 and 1,000,000)"))

    # 範囲以外の場合は再入力うける
    if 100 <= input_train <= 1000000:
        # 2, 乱数生成及びカウント
        for i in range(input_train + 1):  # ユーザが入力した回数分サイコロをふる
            daice_value = random.randint(1,6)  # サイコロの結果は1～6まで
            # 各数字の出現頻度をカウント
            if daice_value == 1:
                d1 += 1
            elif daice_value == 2:
                d2 += 1
            elif daice_value == 3:
                d3 += 1    
            elif daice_value == 4:
                d4 += 1   
            elif daice_value == 5:
                d5 += 1
            else:
                d6 += 1
        
        dice_list = [d1,d2,d3,d4,d5,d6]
        for i in dice_list:
            if i > max_num:
                max_num = i
        print(i)
    # サイコロの目の最大値を求める                     
        max_num = max(dice_list)
    
    # 星の出力数を求める                
        star_count1 = ( d1 / max_num ) * 10
        star_count2 = ( d2 / max_num ) * 10
        star_count3 = ( d3 / max_num ) * 10
        star_count4 = ( d4 / max_num ) * 10
        star_count5 = ( d5 / max_num ) * 10
        star_count6 = ( d6 / max_num ) * 10
    
    # 3,結果の視覚化
    # 出現頻度をヒストグラムで視覚化
        print("Dice Roll Frequency Histogram:")  
        print(f"1: {int(star_count1) * "*"} ({d1} times, {d1/input_train * 10}%)")    
        print(f"2: {int(star_count2) * "*"} ({d2} times, {d2/input_train * 10}%)")
        print(f"3: {int(star_count3) * "*"} ({d3} times, {d3/input_train * 10}%)")
        print(f"4: {int(star_count4) * "*"} ({d4} times, {d4/input_train * 10}%)")
        print(f"5: {int(star_count5) * "*"} ({d5} times, {d5/input_train * 10}%)")
        print(f"6: {int(star_count6) * "*"} ({d6} times, {d6/input_train * 10}%)")      
        break
    # 範囲以外の数値が出力された場合再入力をうける
    else:
        print("Please enter a number within the specified range.") 


##########################################################################


# サイコロが投げた結果の頻度を分析して、ヒストグラムで結果を視覚化するプログラム
#　1,ユーザ入力
#  a、ユーザからサイコロを振る回数を　100～1000000の範囲で入力をうける
import random

while True:
    input_num = int(input("サイコロを振る回数を入力して下さい"))
    # input_num = 1000
    
    #  c、無効な値が入力された場合は再入力を要求
    if  100 <= input_num <= 1000000:
            #　b、サイコロの結果は１～６までで各数字の出現回数をカウントするためのリストを生成する
            # 1 2 3 4 5 6
        count_list = [0,0,0,0,0,0]
        
        # 2,乱数生成、及びカウント
         #　a,　ユーザが入力した回数だけサイコロをふる
        for daice in range(input_num):
            random_daice = random.randint(1,6)
            count_list[random_daice - 1] += 1    
        
    #　3、結果の視覚化
    #　1~6までの各数字の出現頻度をヒストグラムで視覚化
    #　1～6のうち何が一番多くでたか最大値を求める
        maxnum = 0
        for i in range(6):
            if count_list[i] > maxnum:
                maxnum = count_list[i]

    #　c、各数字ごとに確率とヒストグラムを計算
    # ”＊”は最大頻度に対する相対的な割合を表し、最大10個の”＊”を表示するを表示する
        for i in range(6):
            probability = count_list[i] / input_num * 100
            star = count_list[i] / maxnum * 10
            print(f"{i + 1}: {int(star) * "*"}\t({count_list[i]} \ttimes, \t{probability:.2f}%)")
        break
    else:
        print("100~1000000以内の範囲で入力してください")


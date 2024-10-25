# 開始、終了、N – これらの値を使用して、開始と終了の間で重複しない N 個の乱数を作成し 1 次元リストに格納して出力
# 入力
import random
    
print("난수를 생성할 범위와 개수를 입력하세요.")
    
while True:
    
    while True:
    # 開始: 乱数の開始範囲  0 以上
        start = int(input("Start (0 이상의 정수): "))
        
        if start > 0:
            break
        else:
            print("0이상의 정수를 입력하세요.")
        

    while True:
    
    # 終了: 乱数の終了範囲  開始 – N より大きくなければならない
        end = int(input("End (Start보다 큰 정수): "))
        if end > start:
            break
        else:
            print(f"End는 Start({start})보다 더 커야합니다")
         
    while True:
    # 生成される乱数の数 : 開始と終了の間
        N = int(input("N (생성할 난수의 개수): "))
        if start < N < end:
            break
        else:
            print(f"N은 {start}부터 {end} 사이의 정수여야 합니다.")


    num_list = []
    for i in range(N):
        
        while True:
            ran_num = random.randint(start,end-1)
            if  ran_num not in num_list:
                num_list.append(ran_num)
                break
            
    print(num_list)
    break
            

        # 出力 
        # すべての入力は、有効になるまで再入力が必要
        # 生成された乱数値は、1 次元リストに格納する

    
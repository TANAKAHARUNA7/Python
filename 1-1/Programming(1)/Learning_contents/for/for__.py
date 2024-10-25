

for num in range(2,10):
    if num % 2 == 0:
        print("偶数",num)
        continue  # 繰り返し処理を1つSKIPさせる　　
    print("奇数",num)     #数字を1つ飛ばしたいときや文字列から特定の文字を除外したいときに使う

    
list = [1, 2, 3, 4, 5]   

for num in list:
    if(num == 3):
        continue
    print(num)
    
    
    
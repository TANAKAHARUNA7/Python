
import random
while True:
    # ユーザからサイズを３～６までの整数で入力をうける
    input_size = int(input("Enter the size of the bingo bord (3 to 6): "))
    
    ran_list = []
    count = 0  
    
    if  3 <= input_size <= 6:
        # 重複しないランダム整数を生成
        for i in range(input_size):
            for j in range(input_size):
                ran_num = random.randint(1,36)
                ran_list.append(ran_num)
                print(f"{ran_num}", "\t" ,end="")
            print()
    else:
        print("Size must be between 4 and 6. Please try again.")



import random
# 単語当てゲーム
# 英単語3つ入力を受け、リストに保存する。
input_word_list = []
input_word_count = 1

while input_word_count <= 3:
    
    input_word = input(f"{input_word_count}回目の単語を入力してください\n")
    
    # 単語の文字数は5 ～ 20文字
    if 5 <= len(input_word) <= 20:    
        input_word_list.append(input_word)
        input_word_count += 1
          
    # 該当しない場合再入力を要求         
    else:
        print("5~20の文字で構成された単語を入力してください")
        

# 入力された3つの単語の中で一つをランダムに選択
print("単語選択完了、ゲーム開始。選択された単語: ", end="")
random_com_word =  random.choice(input_word_list)
print(random_com_word)


num = len(random_com_word)
if num % 2 == 0:
    num_up = int(num) // 2 
else:
    num_up = int(num) // 2 + 1

print(num_up)





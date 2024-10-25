# じゃんけんプログラム
import random
# ユーザからグー、チョキ、パーを選択してもらう
x = input("グー、チョキ、パーの中で一つを選択してください: ")

choices = ['グー','チョキ','パー']
computer_choice = random.choice(choices)
# グー、チョキ、パーをランダムに出力
print('コンピューターの選択',computer_choice)

# 無勝敗の場合
if x == computer_choice:
        print("結果: 無勝敗です")
# ユーザの勝利
elif ( x == 'グー' ) and ( computer_choice == 'チョキ') or ( x == 'チョキ' ) and ( computer_choice == 'パー') or  ( x == 'パー' ) and ( computer_choice == 'グー'):
    print("結果: あなたの勝ちです")
# コンピューターの勝利   
elif ( x == 'パー') and ( computer_choice == 'チョキ') or ( x == 'チョキ') and ( computer_choice == 'グー')or ( x == 'グー') and ( computer_choice == 'パー'):
    print("結果: あなたの負けです")
# エラー
else:
    print("間違った入力です。グー、チョキ、パーの中で入力してください")
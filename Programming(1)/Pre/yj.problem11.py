#　ユーザから長さの入力を受けてその長さのランダムパスワードを生成する関数を作成する
import random
# 大文字、小文字、数字を組み合わせてパスワードを生成する
def generate_password(length):
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = uppercase_letters.lower() # 大文字を小文字に変更
    digits = '0123456789'
    # 全ての可能な文字を一つの文字列に結合
    all_characters = uppercase_letters + lowercase_letters + digits

    # パスワード初期化
    password = "" 
    
    # 指定された長さの分だけランダムに文字を選択
    for _ in range(length):
        
        password += random.choice(all_characters) # ランダム文字パスワードを追加
  
    # 生成されたパスワードを変換
    return password

generated_password = int(input("パスワードの文字を入力してください"))
passwordddd = generate_password(generated_password)
    
print(generate_password(generated_password))  
    
   
    
    
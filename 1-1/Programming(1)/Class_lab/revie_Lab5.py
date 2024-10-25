#日本語の性別を英語に変換
sex = input("性別を入力してください（女／男）:")

sex1 = "男"
sex2 = "女"

if sex == sex1:
    print("MEN")
elif sex == sex2:
    print("WOMEN")    
# 以外の入力についてはエラーメッセージ出力
else:
    print("間違った入力です")   
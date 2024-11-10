# 3つの数字を受ける
num1 = int(input("1つ目の数字を入力したください: "))
num2 = int(input("2つ目の数字を入力したください: "))
num3 = int(input("3つ目の数字を入力したください: "))

# 結果を出力
# ⓵すべての数字が同じです
if num1 == num2 == num3 :
    print("すべての数字が同じです")
# ⓶二つの数字が同じです　同じ数字も出力
elif num1 == num2 :
    print("二つの数字が同じです.",num1,"と",num2)
elif num1 == num3:
    print("二つの数字が同じです.",num1,"と",num3)
elif num2 == num3:
    print("二つの数字が同じです.",num3,"と",num2)
# ⓷すべての数字が違います　一番大きい数字を出力
else:
    max_num = num1
    if max_num < num2:
        max_num = num2
    if max_num < num3:
        max_num = num3
    print("すべての数字が違います.一番大きい数字は",max_num)
 
        
        
        
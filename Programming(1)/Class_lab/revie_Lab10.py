
#
# 3つの整数数字を受ける。

num1 = int(input("1つ目の数字を入力してください: "))
num2 = int(input("1つ目の数字を入力してください: "))
num3 = int(input("1つ目の数字を入力してください: "))

maxNum = num1

if num2 > maxNum:
    maxNum = num2
if num3 > maxNum:
    maxNum = num3
print("一番大きい数字は",maxNum,"です")

# # 受け取った数字の中で最も大きい数字を決定し出力します
# if num1 < num2 > num3 or num1 == num3 < num2 or num2 > num3 > num1:
#     print("一番大きい数字は",num2,"です")
# elif num2 < num1 > num3 or num2 == num3 < num1 or num1 > num3 == num1:
#     print("一番大きい数字は",num1,"です")
# elif num2 < num3 > num1 or num1 == num2 < num3 :
#     print("一番大きい数字は",num3,"です")

    
    
    
    
    
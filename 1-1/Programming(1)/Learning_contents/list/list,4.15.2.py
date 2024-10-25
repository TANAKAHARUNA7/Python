# bar = [] #リスト生成

# for value in range(1,20):
#     bar.append(value)
    
# print(bar)
# # [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

# #一つ目のリストの値は？
# print(bar[0]) # 1


# foo = []

# foo.append(10)
# foo.append(20)
# foo.append(30)
# foo.append(5)
# # foo.append(90)
    
    
# for index in range(0,4): # range(x, y-1)
#      print(foo[index]) #リストfoo内の各要素をインデックスを使って出力
    
# print("foo listのサイズは",len(foo)) # len() → fooの中にある文字数を計算
    
# print([index]) # foo = [] の中にある元素の数を表示(0～


numbers = [4,1,3,2]
print("")

number = [4,1,3,2]
print("元々の手順: ", number)

number.append(5)
print("要素追加後: ", number)

number.remove(2)
print("要素削除後: ", number)

mixed_list = [1, "apple", 3.14, [2, 4, 6], True]
print("混合データタイプリスト:",mixed_list)

squares = [x** 2 for x in range(10)]
print("リストコンプレッション: ", squares)


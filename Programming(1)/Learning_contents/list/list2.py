
# bar = [2,3,4,5,6]

# foo = bar[-1:0:-1] 

# print(type(foo))

# print(foo)


# # CRUD : Update
# # Befor [2,3,4,5,6]
# bar[1] = 20

# bar[0:3] = [100,200,300]

# print(bar)


# bar = [100,200,300,400,500,600,700]
# CRUD : Delete
# 元素削除：元素の１つの削除、リスト内全体の元素の削除
# 1) del 命令語を使用し該当するインデックスの元素を削除 
# 2) remove 　関数を使用し
# 3) pop() インデックスの値を使用し元素を削除する。
# # del , pop()はインデックスの値を使用し元素を削除する。
bar = [10,20,50,30,40,50,60]
# print("befor",bar)
# del bar[1]

# print("after",bar,len(bar))

# bar.remove(50)   # 一番初めに出会った指定の元素を削除する
# print("after",bar,len(bar))  

#bar.pop(2)  #　指定したインデックスの元素を削除する。 
print("after",bar,len(bar))
print(bar.pop(2))

bar.pop() # インデックスを使用しなければ最後の元素が削除される。
print("after",bar,len(bar))

# clear() -> リストの中身元素を全て削除するがbarという参考変数は残っている。
bar = [1,2,3,4,5,6]
bar.clear()
print(bar)

# del -> fooという参考変数自体を削除する
foo = [1,2,3,4,5,6]
del foo



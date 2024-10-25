# リスト生成
my_list = [10, 20, 30, 40, 50]
print("Initial list:", my_list) 

#　リストの特定の要素に接近
print("Element at index 2:",my_list[2]) # 30

# リストの特定の要素をアップデート
my_list[1] = 25
print("Updated list:",my_list) # [10, 25, 30, 40, 50]

# リストに要素追加
my_list.append(60)

# リスト内の要素を指定された位置に挿入
my_list.insert(2,15)

# 全体リスト出力
print("Full list:",my_list)  # [10, 25, 15, 30, 40, 50, 60]

# リストの特定の要素を削除
my_list.remove(25) # [10, 15, 30, 40, 50, 60]

# リストの特定のインデックスにある要素を削除
del my_list[0] 

# リストの特定のインデックスにある要素そ削除
poppend_element = my_list.pop()  # 最後の要素を削除または、返還
print("List after poping the last element:",my_list)  # [15, 30, 40, 50]
print("Popend element:",poppend_element)  # 60

# リスト全体の要素を削除
my_list.clear()  # []

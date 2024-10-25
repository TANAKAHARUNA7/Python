
import random
n = 5
max_num = 6

sample_list = [value for value in range(1, max_num) ]
# sample_list -> [1, 2, 3, 4, 5]

random_list = []

for trial_count in range(0, n):
    random_index = random.randint(0, len(sample_list) -1 )
    random_num = sample_list.pop(random_index)
    random_list.append(random_num)    
    
print(random_list)    

#
# bar = []

# for value in range(1,101):
#     bar.append(value)
# print(bar)


bar = [10,20,30,40]
foo = bar[:] # 指定していないため元素をすべて表示
print(foo)   # [10,20,30,40]

foo = bar[2:] # 元素3番目から最後まで
print(foo)    # [30,40]

foo = bar[:3] # 元素0から3番目まで
print(foo)    # [10,20,30]

foo = bar[-1:-4:-1] # 後ろから順に元素を出力。
print(foo)          # [40,30,20] ｰ4はｰ3まで。（一個手前まで。）

foo = bar[-1::-1] #　後ろから一番最初の元素まで１つづつ表示　75列目と同じ結果。
print(foo)        # [40,30,20,10]
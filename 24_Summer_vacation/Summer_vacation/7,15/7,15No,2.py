
# bar = lambda x, y : x * y
# print(bar(2,3))  # 6

###########################################
bar = lambda x, y : x * y

bar = [[10, 9] 
    ,  [8 , 2]
    ,  [3 , 10]]


def get_value (record):
    return record[1]

result = sorted( bar, key = get_value, reverse= True)

result = sorted( bar, key = lambda record : record [1], reverse= True)

print(result)

result = sorted(bar, reverse=True)  # [[10, 9], [8, 2], [3, 10]]　＜大きい順＞　1番目のindex値で順番を設定

print(result)

result = sorted(bar, reverse=False)  # 

print(result)


###########################################
 
# def Anoymous(x, y):
#     return x * y

# bar = Anoymous

# ###########################################



# def foo(x, y):
#     return x * y   

# pos = foo
# print(pos(4,3))  # 12

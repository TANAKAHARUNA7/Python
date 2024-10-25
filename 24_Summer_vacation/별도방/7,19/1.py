# bar = [[7,9], [2,6],[10,4]]

# # def get_value(record):
# #     return record[1]

# # result = sorted(bar, key= get_value)

# # 媒介変数＝record　
# result = sorted(bar, key= lambda record : record[1])

# print(result)

####################################################

bar ={4, 5, 1, 10}

print(type(bar))  # <class 'set'>

result = sorted(bar)

print(result)  # [1, 4, 5, 10]

#####################################################

bar = dict()

bar = {"a": 10, "b" : 30, "f" : 15, "c" : 20}

result = sorted(bar.keys())

print(result)

######################################################


# foo = [value for g in range(2) for value in range(3)]  # [0, 1, 2, 0, 1, 2]
        #  ↓
# for g in range(2) :
#     for value in range(3):
#         value


# foo = [[value for g in range(2)] for value in range(3)]
# print(foo)  # [[0, 0], [1, 1], [2, 2]]


bar = {
    "ycj" : {"name" : "정영철", "age" : 20},
    "lny" : {"name" : "이나영", "age" : 30}
        }

foo = [d for d in bar.values()]
print(foo)
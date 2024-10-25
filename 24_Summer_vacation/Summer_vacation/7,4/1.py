# bar = [10, 20, 30, 40]

# for item in bar:
#     print(item)
    
# print("-" * 30)

# for index in range(-1, -5, -1):
#     print(bar[index])
    
# # 원소 30를 100으로 변경
# # bar[좌표] = 100
# bar[2] = 100
  
######################################################

foo = [10, 20, 30, 40]

print(foo)

while len(foo) > 0:
    item = foo.pop(0)
    print(item)

foo.insert(3, 70)
print(foo)


# del foo[2]  # 리스트 안에서 아이 없어 진다
# print(foo.pop(2))  # 그냥 치운게 아니라 출력할 수 있다




# foo = [0, 0, 0, 0]

# foo = [0 for _ in range(6)]  # [0, 0, 0, 0, 0, 0]

# print(foo)

# foo = [0] * 6   # [0, 0, 0, 0, 0, 0]

# print(foo)



################################################

kin = [[1,2,3,4],[0,0,0,0],[5,6,7,8]]


rows = 3
cols = 3
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

matrix = [[0]*4 for _ in range(3)]









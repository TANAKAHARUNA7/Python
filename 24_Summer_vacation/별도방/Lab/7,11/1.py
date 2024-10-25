# bar = [4, 5, 2, 10, 9]

# # sorted(, reverse = True )リスト内を大きい順に表示
# # sorted(, reverse = False )リスト内を小さい順に表示
# result = sorted(bar,reverse = False)[0:2]

# print(bar)
# print(result)

#######################################
bar = [
        [4, 5, 20],
        [7, 8, 10],
        [1, 2, 3]
        ]

result = sorted(bar,key= lambda row : row[2], reverse = True)

# lambda function 람다 함수
# lambda 인자 값 : 수식

print(result)
# foo = lambda x, y : x + y
# print(foo(2, 4))
# print(bar)

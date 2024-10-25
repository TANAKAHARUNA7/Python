# bar = [10,20] # list 생성 []

# foo = (30,40) # Tuple 생성 ()

# print(bar[0], foo[0])

# bar[0] = 100  # Mutable
# foo[0] = 200  # Tuple:Imutable

###################################################


bar = []

for _ in range(5):
    bar.append(input("값: "))

print(bar)

foo = set()  # 重複した値がある場合、全て合併して出力

for _ in range(5):
    foo.add(input("값: "))
print(foo)



###################################################




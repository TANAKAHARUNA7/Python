import random

bar = [ random.randint(1,7) for _ in range(10)]
print(bar)

foo = set()

for index in range(10):
    foo.add(bar[index])
print(foo)

bar = {}

print(type(bar))

bar["ycj"] = "정영철"

foo = [ 10, 20, 3, 5, 6, 200, 300] 

for value in foo:
    if value == 300:
        print("300이 리스트 내 있습니다.")




   
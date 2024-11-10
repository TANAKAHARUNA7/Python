# 
# 
bar = []
foo = list()

bar.append(10)
bar.append(20)

bar.insert(1,100)


# Read
for i in range(len(bar)): # bar[]の中身を表示　　
    print(bar[i])

har = [value for value in range(10,20)]
# 10,11,12,13,14,15,16,17,18,19
# slicing
# 참소변수 [start : stop : step]
#start : 0 -> stop : 4 -1
lee = har[0:4:1]

print("lee", lee)
print("har",har)



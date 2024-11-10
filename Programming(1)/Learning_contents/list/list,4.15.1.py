
foo = [10,20,30]

bar  = [100, 200, 300]

bar = foo

bar[0] = 7000

print(foo[0],bar[0]) 


bar = [90, 10, 20]

foo = bar

pos = foo

pos[2] = 100

print(bar[2])


a = [40 ,29 ,0 ,30]

b = [42, 90, 50 , 60]

a[2] = 900

b = a
print(b[2], a[2])


bar = [90 ,10 ,20 ]

def test(argValue):
    for index in range(0,len(argValue)): # range(0,3)と同じこと
        argValue[index] += 1
        
test(bar)

print(bar)


bar = [1, 2, 3, 4]

bar = []

foo = bar 

# foo = []
foo.append(10)

print(bar[0])


bar = [value**2 for value in range(1, 11)]

print(bar)


B = [1, 2, 3, 4, 5]

B.append(10)
print(B)

B.insert(2, 7)

print(B)

bar = [3, 5, 7]

foo = [5, 2, 6]  

bar = bar + foo 

bar.extend(foo) # 75列と同様にリスト同士を合体させる

print(bar)
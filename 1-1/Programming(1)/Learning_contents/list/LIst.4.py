bar = [10,20,30]

def test(argValue):
    for index in range(0,len(argValue)): # range(0,3)と同じこと
        argValue[index] += 1
        
test(bar)
print(bar)


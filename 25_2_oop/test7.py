
def bar():...
def test():
    print("a")
    yield 1
    print("b")
    yield 2
    print("c")
    yield 3
    print("d")
    yield 4

obj = test()
print(obj.__next__()) 
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())

def my_range(num:int):
    count:int = 0
    
    while(count < num):
        yield count
        count += 1

for x in my_range(5):
    print(x)
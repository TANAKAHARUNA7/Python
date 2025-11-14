def f_a(func):
    def wrapper():
        print(f"f_a: {func}")
        func()
        
    return wrapper 
    
def f_b(func):
    def wrapper():
        print(f"f_b: {func}")
        func()
    return wrapper

@f_a
@f_b # bar = f_a(f_b(bar))
def bar():
    print("bar")
    
bar()
    
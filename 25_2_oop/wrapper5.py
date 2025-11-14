from functools import wraps

def test(n):
    def factory(func):
        def wrapper(func):
            func()
    
        return wrapper
    return factory

@test(1)
def bar():
    ...

bar()
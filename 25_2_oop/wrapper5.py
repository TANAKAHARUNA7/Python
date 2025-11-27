from functools import wraps

def test(path):
    def factory(func):
        def wrapper(func):
            func()
        return wrapper
    
    return factory

@test(1) # test(1) -> factory()(bar)
def bar():
    ...

bar()
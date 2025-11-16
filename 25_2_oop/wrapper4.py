
from functools import wraps
def upper_decorator(func):
    # @wraps(func)
    def wrapper(msg:str):
        return func(msg.upper())
    
    # wrapper.__name__ = func.__name__
    
    return wrapper

@upper_decorator
def bar(msg:str):
    return msg

print(bar.__name__)    
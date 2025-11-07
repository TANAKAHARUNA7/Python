from typing import Any, Self

def decorator(func):
    print("decorator")
    
@decorator
def test():
    print("test")
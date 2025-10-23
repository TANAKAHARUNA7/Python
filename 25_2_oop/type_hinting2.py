# a : None = None

def something(a: int, b: float, c:None=None)-> None:
    ...

# Callable(param...) -> return type
def sum(x : int, y : int):
    return x + y    

class Bar:
    # None : 반환형 없다
    def __init__(self, x: int, y: str) -> None:
        self.x:int = x
        self.y:str = y
        
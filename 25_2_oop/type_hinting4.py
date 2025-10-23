x:int = 1

def test(x1: float, x2:int)->float:
    ...
    
test(2, 3)

class Bar:
    def __init__(self, name:str, age:int)->None:
        self.name:str = name
        self.age:int = age
        
from typing import Any
x: int | float | str = 1        

from typing import Union
y: Union[int, float] = 1
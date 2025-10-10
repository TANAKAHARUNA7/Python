

from typing import Union
def sum(a : Union[int, float], b : Union[int, float]) -> int | float:
    return a + b

print(sum(1,1))
print(sum(1,1.0))
print(sum("1","1"))
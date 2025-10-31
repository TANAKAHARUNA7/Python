
from logging.config import valid_ident
from multiprocessing import Value
from typing import Self, Sequence

class Bar:
    def __init__(self, data:Sequence[int]) -> None:
        self.data:Sequence = data
        self.index:int = 0
    
    def __iter__(self):
        return BarIterator(self.data)   

    
class BarIterator:
    def __init__(self, data:Sequence)-> None:
        self.data:Sequence =data
        self.index = 0
        
            
    def __next__(self)->int:
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        
        raise StopIteration
        
    
obj = Bar([1, 2, 3, 4])

for v in obj:
    print(v)
    
print(obj.index)
for v in obj:
    print(v)

# x = [10, 20, 30]
# for _ in x:
#     print(_)

# foo = iter(x)
# while True:
#     try:
#         next(foo)
#     except StopIteration:
#         break 
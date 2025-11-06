

from textwrap import indent


class MyData:
    def __init__(self, data:list)-> None:
        self.data:list = data
        self.index = 0
        
    def __iter__(self):
        return BarInterator(self.data)
    
    # def __next__(self)->int:
    #     if self.index < len(self.data):
    #         value = self.data[self.index]
    #         self.index += 1
    #         return value   
        
    #     raise StopIteration 

class BarInterator:
    def __init__(self,data)-> None:
        self.data = data
        
    def __next__(self) -> int:
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value 
        
        raise StopIteration 


data = MyData([1, 2, 3, 4, 5])

print(f"1th: {data.index}")
for x in data: # data -> __iter__() -> self.__next__() -> 1
    print(x)   # self().__next__() -> 2

print(f"2th: {data.index}")
for x in data: 
    print(x)

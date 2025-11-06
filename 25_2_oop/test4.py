

from typing import ClassVar
class Student:
    
    # インスタンスメンバー変数
    name:str
    id:str
    age:int
    
    count:ClassVar
    
    def __init__(self, name:str, id:str, age:int) -> None:
        self.name:str = name
        self.id:str = id
        self.age:int = age

obj = Student("haruna", "1234", 12)
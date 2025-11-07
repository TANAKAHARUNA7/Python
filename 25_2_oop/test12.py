from typing import Any, Self

from dataclasses import dataclass, field

@dataclass
class Student:# data保存用クラスになる
    age:int #インスタンスメンバー変数
    # list,dic,など初期値に設定することはできない
    data:list
    name:str = field(compare=False, repr=False) #インスタンスメンバー変数
    id:str  #インスタンスメンバー変数
    
std1 = Student("123", "Kim", 20)
std2 = Student("124", "Lee", 30)

print(std1)
print(std2.name, std2.id, std2.age)
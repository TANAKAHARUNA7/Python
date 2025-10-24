# TypedDic =-> 스키마 정의 -> dictionary -> JSON

from typing import TypedDict

class User(TypedDict):
    name:str
    age:int
    gender:str
    
    
x:User = {"name":"haruna", "age":20, "gender":"W"}

x = {"name":"haruna", "age":20, "gender":"W"}



 

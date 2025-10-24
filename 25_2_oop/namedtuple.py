from typing import NamedTuple


class User(NamedTuple):
    name:str
    age:int
    gender:str
    
u1 = User("Haruna", 2, "W")

def create_user(name:str, age:int, gender:str) -> User:
    return User(name, age, gender)

name, age, gemder = create_user("Haruna", 2, "w")
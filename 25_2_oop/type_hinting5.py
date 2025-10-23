

# x: list[int]  = [1, 2, 3, 4]

# x = [2.0]

# # dict
# y:dict[str,str] = {"name":"haruna"}

#########################

from typing import Optional,Union,NoReturn,Literal, Callable

# x:Optional[int] = 2

# def add_user(name:Optional[str])-> Optional[NoReturn]:
#     if name is None:
#         raise ValueError("Nemu must be values")
    
############################

# 자료형과 값까지 알려 준다
def move(direction:Literal["forward", "backward", "left" ,"right"])->None:
        ...
############################

def test(): ...

# 함수를 변수에 저장
x = test

x()

def run(func):
    return func

run(test)



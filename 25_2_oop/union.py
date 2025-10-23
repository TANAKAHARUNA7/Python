# Union -> 집합의 원소 중 하나이면 -> ok,
# 모두 해당 되지 않으면 -> Erro

from queue import Full
from typing import Union
x: Union[int, float, bool]

# 최신 version
x_new:int | float | bool

x = 2
x = 3.0
x = False
x = "2"
##########################

# Optional -> if else -> if [T] else None
from typing import Optional

#  이값이 않으면 'None'로 반환
x_op_int: Optional[int]


#################################
from typing import Literal

#x_lit[] 안에는 1, 2, 3 밖에 들어 갈 수 없다  
x_lit:Literal[1, 2, 3]

gender:Literal["man".]

#######################################

from typing import Any
x: Any
x = 1
x = 2.0
x = "d"

################################

# Callable -> 함수, method

from typing import Callable

def sum(x: float, y: float)-> float:
    return x + y

sum_2 = sum
print(sum_2(2, 3))
                                             # [[메개변수], [반환형]]
def do_something(x: float, y:float, op:Callable[[float, float], float]:
    return op(x, y)

do_something(1, 2, sum)
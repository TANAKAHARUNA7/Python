# Colletion -> Abstract Data Type -> Implementation Set
# Python -> list, tuple, dict, set

# def get_total_avg(x: int, y:int) -> tuple:
#     sum = x + y
#     avg = sum / 2
#     return sum, avg

# x_tuole:tuple = (1, 2, 3)

# x_tuple = [1, 2, 3]

# x_dict:dict = {1:2, 3:4}

# x_set:set = {1, 2, 3}

# x_range:range = range(2)
#######################################

# x_list_int:list[int | float] = [1, 2, 3]
# x_list_int = []

# # 순서와 개수, 자료형까지 맞져야 한다
# x_tuple_int:tuple[int, float, str] = (2, 2.0, "2")

# # 놓는 자료형이 모드 같은 경우에는 ',...'
# y:tuple[int,...]
# y = (1, 2, 3)
# y = (2, 3, 4, 5, 6) 

# x_dic_str_float:dict[str, float] = {"k1":2.0, "k2":3.0}
# x_dic_str_float  = {1:2.0}

# x_set_bool:set[bool] = {True, False}

########################################

from typing import Sequence

# Sequence -> Type hinting -> list, tuple, range
x_seq_int:Sequence[int] = [1, 2, 3]
x_seq_int = (1, 2, 3)
x_seq_int = {1, 2, 3}
x_seq_int = {1:2}

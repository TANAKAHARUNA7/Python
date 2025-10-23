from typing import Sequence

# list: 要素タイプのみ検査
x_list_int: list[int] = [1, 2, 3]
x_list_int = [1, 2.0]

#　Tuple:　．．．は要素数制限なし
#　数と各位置別タイプまで検査
x_tuple_float: tuple[float,...] = (2.0, 7.0, 3.0)
x_tuple_float = ("2.0")

#　Tuple:　要素タイプ、位置、数検査
x_tuple_num: tuple[int, str, float,] = (1, "2.0", 3.0)
x_tuple_num = (1, 2, 3.0)
x_tuple_num = (1, "2.0")

#　dect:　キーと値のタイプを指定
x_dict_str_int:dict[str,int] = {"t":1, "e":3}

#　set:　要素のタイプのみ検査（順序や重複なし）
x_set: set[int] = {1, 2, 3}
y_set: set[int] = {4, 6, 1}

print(x_set | y_set) # {1, 2, 3, 4, 6}
print(x_set - y_set) # {2, 3}
print(x_set ^ y_set) # {2, 3, 4, 6}

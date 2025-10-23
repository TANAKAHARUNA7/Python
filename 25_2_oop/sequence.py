from typing import Sequence

x_list: list = [1, 2, 3]
x_tuple: tuple = (1, 2, 3)
x_dict: dict = {1:10, 2:20}
# set: 順番なし、重複なし、要素のタイプだけ検査する
x_set:set = {1,2,3,4,5}

# Sequence: →位置基盤。list/tuple/range などすべて合わせる
#　”読む専用”Sequenceインターフェース
x_sequence: Sequence = [1, 2, 3]
x_sequence = (1, 2, 3)
x_sequence = range(5)
# setはSequenceではないためエラー表示
x_sequence = {1, 2, 3}
#　dictはMapping，Sequenceではないためエラー表示
x_sequence = {"x": 2, "y": 3} 

class Vector:
    def __init__(self, x:int, y:int) -> None:
        self.x:int = x
        self.y:int = y

    #　__add__()をオーバーライディングする
        # self -> v1 , r_operand -> v2
    def __add__(self, r_operand:"Vector"):
        x = self.x * r_operand.x # (1+3)
        y = self.y * r_operand.y # (2+4)
        return Vector(x,y)  # (4, 6) の新しい Vectorが返る
        
        print(f"__add__ is invoked. {r_operand}")


v1 = Vector(1, 2)
v2 = Vector(3, 4) 

v3 = v1 + v2 # 内部でtype(v1).__add__(v1, v2)を呼び出すが、
             # v1とv2はオブジェクトのため演算できない！ 
print(v3.x, v3.y) # 4 6

# x3 = v1.x + v2.x 
# y3 = v1.y + v2.y

# v3 = Vector(x3, y3)       
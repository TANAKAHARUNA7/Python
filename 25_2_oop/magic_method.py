class Vector:
    def __init__(self, x:int, y:int) -> None:
        self.x:int = x
        self.y:int = y

    def __add__(self, r_operand:"Vector"):
        print(f"__add__ is invoked. {r_operand}")


v1 = Vector(1, 2)
v2 = Vector(3, 4) 

# v3 = v1 + v2
# v4 = v1 + v2
# x3 = v1.x + v2.x 
# y3 = v1.y + v2.y

# v3 = Vector(x3, y3)       
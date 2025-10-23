from typing import Optional

# Optional[T] == T | None
# 該当する型の値を受けとる、または”None”を受けとる
x_opt: Optional[int] = None
print(type(x_opt))

x_opt = 2

def calc(x: int, y: int, op: Optional[str] = None):
    if op is None:
        return x + y
    return x * y

print(calc(2,5,"j")) # 10
print(calc(2,5)) # 7
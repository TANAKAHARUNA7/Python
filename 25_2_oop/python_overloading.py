# 파이썬에서 오버로딩 흉내 내는 방법
# 1) 가변인자 활용
# def add(*args):
#     return sum(args)
    
# print(add(1,2))
# print(add(1,2,3))
# print(add(1,2,3,4))

# 2) 티입 분기 이용
# def to_str(x):
#     # instans()로 런타임 시점에 타입을 확인
#     if isinstance(x, int):
#         return f"int: {x}"
#     elif isinstance(x, float):
#         return f"float: {x}"
#     elif isinstance(x, str):
#         return f"str:{x}"
    
#     # 정의하지 않은 타입이 들어오면 예외 발생
#     raise TypeError("unsupported type")

# # 호출 예시
# print(to_str(1))
# print(to_str(2.0))
# print(to_str("3"))
# print(to_str(add))


# 3) singledispactch 활용
from functools import singledispatch

@singledispatch
def prt(x):
    raise TypeError(f"unsupport type{x}")

@prt.register(int)
def _(x: int):
    return f"int {x}"

@prt.register(float)
def _(x: float):
    return f"float {x}"

print(prt(2.0),type(_(2.0)))
print(prt(2),type(_(2)))
print(prt("2"))

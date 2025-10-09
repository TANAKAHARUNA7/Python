

x = 1.0

if isinstance(x, int):
    print(f"x int: {type(x)}")
elif isinstance(x, float):
    print(f"x float: {type(x)}")
else:
    raise TypeError("unsupported type")
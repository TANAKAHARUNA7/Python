# # def prt(positional, variable prositional, keyword, 
# #       variable keywords):
# #       ....

# def calculate(x, y, op = "+"):
#     if op == "+":
#         print(x + y)
#     elif op == "-":
#         print(x - y)
#     else:
#         print("error")
        
# calculate(2, 3)
# calculate(10, 20, "-")    

# def prt(**arg):
#     for key, value in arg.items():
#         print(f"{key}, {value}")


# def prt(a, *arg):
#     print(a, arg)
    
# prt(1)
# prt(1, 2)
# prt(1, 2, 3)

def prt(a, *b, c = 10, d = 20, **kwargs):
    print(a, b, c, d, kwargs)

prt(1, 2, 3, 4, 5, op = 200, d=100)
# variable parameter : 가변 파라메터
# 1) *
# 2) **
#         # * -> 가변 : Dictionary 로 받겠다
#         #               key : value
def foo(**args):
    print(len(args))
    for h, value in args.items():
        print(value)
        
foo(test = 2, king = 3)  # 1
# foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)  # 12

# def bar(*args):
#     if len(args) == 1:
#         start = end = args[0]
#     elif len(args) == 2:
#         start, end = args
#     else:
#         return
    
#     for dan in range(start, end + 1):
#         for num in range(1, 10):
#             print(f"{dan} X {num} = {dan * num}")
            
# bar(2)
# bar(2, 3)


# def foo(**args):
#     print(len(args))
#     for key , value in args.items():
#         print(f"key: {key}, value: {value}")
        
# foo(test = 2, king = 3)
# foo(test = 2, king = 3, lion = 4)


# def foo(arg_a, arg_b, arg_c, arg_d, arg_e):
#     print(arg_a, arg_b, arg_c, arg_d, arg_e)

# arg_list = [value for value in range(1,6)]   
# arg_list = [1,2,3,4,5]
# foo(arg_list)



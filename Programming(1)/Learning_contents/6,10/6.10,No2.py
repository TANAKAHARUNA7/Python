# 함수 사용의 순서
# 1) 함수를 정의한다.
# 2) 정의된 함수를 호출한다.

# Call-by-value, Call-by-reference

# bar = 3

# def foo(bar):
#     bar = bar + 1
#     print("1: ", bar)
    
# foo(bar)

# print("2: ", bar)

bar = [20, 30, 40]

def foo(argList): # Call-by-reference
    argList[2] = 100
    argList[0] = 300
    
foo(bar)

print(bar)

# Primitive variable : sol, msg
# Reference variable : 

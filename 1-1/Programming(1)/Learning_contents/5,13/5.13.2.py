# # bar = 0

# # bar =+ 1 # -> +1と同じ

# # print(bar)

# # Membership operator
# # in ,not in
# # A in B
# # A 값, B sequential Object
# # 결과 값은 Boolean


# def myInOperator(argValue, argSeqObj):
#     for value in argSeqObj:
#         if value == argValue:
#             return True
        
#     return False
   
# def myInOperator(argValue, argSeqObj):   
#     for value in argSeqObj:
#         if value == argValue:
#             return False
        
#     return True
   
   
# print("a" in "abc")

# bar = [3, 4, 5, 6]

# print(4 in bar)
# print(4 not in bar)
# print(myInOperator(3,[2,3,4]))

# Identity Operator
# is, is not

bar = [2, 3, 4]

foo = [2, 3, 4]
    
if bar == foo:
    print("참")
else:
    print("거짓")

if bar is foo:
    print("참")
else:
    print("거짓")
    

# リスト(list)
list_type = [1, 2, 3, 4, 5]

# タプル(tuple)
tuple_type = (1, 2, 3, 4, 5) # タプルは（）がなくても","でタプル型と認識
# Nested (중첩): 한 개의 흐름제어문 내에 또 다른 흐름제어문 

# for value in range(10):  # 反復文だけを利用することができる
#     print(1)   # 1111111111 ->　1を10回表示
    

# for value in range(5,-20,-5):  
#     print(value)  
    

# for _ in range(8):  
#     print(_, end="")
# print()      

# bar = []
# for value in range(1,21):
#      bar.append(value)
# print(bar)

# # 리스트 내 원소 값들을 for 문을 사용하여 동적으로 생성
# list = [value for value in range(1,21)]
# print(list)


# 7로 초기회된 8개의 원소를 가지는 리스트를 생성
# [ expression for item in item_list if conditional expression ]
# list = [7 for _ in range(8)]
# print(list)

# bar = [ value for value in range(1, 21) if value % 3 == 0 ]
# print(bar)

foo = ["abc", "dcd","ef","gh"]

# for c in foo:
#     if "c" in c:
#         print(c)
        
c = [word for word in foo if "c" in word]
print(c)

#      
cd = [ word for word in foo if len(word) >= 3]
print(cd)   

# 1에서 10사이 정수 중 , 홀수는 10을 곱하고 , 짝수는 20을 곱한 리스트를 생성 
value = [ num * 10 if num % 2 != 0 else num * 20 for num in range(1,11) ]
print(value) 

s_list = [value for value in range(1, 21) if value % 3 == 0 if value % 2 == 0]





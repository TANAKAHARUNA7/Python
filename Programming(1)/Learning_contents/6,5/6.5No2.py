# break 
# continue
# pass(python)
# for k in range(1,5):
#     for i in range(1, 3): # 1 -> 2
#         for j in range(1, 4): # 1 -> 3
#             if i == 2:
#                 break
#             print(i, ":", j)
            
            
# for k in range(1,5):
#     if k == 2:
#         break
#     for i in range(1, 3): # 1 -> 2
#         for j in range(1, 4): # 1 -> 3
#             print(i, ":", j)            
           
           
# for k in range(1,5):    
#     for i in range(1, 3):
#         for j in range(1, 4): 
#             if j == 2:
#                 break
#             print(i, ":", j)          
     
     
# for l in range(1,2):            
#     for k in range(1,5):    
#         for i in range(1, 3):
#             if i == 2:
#                 break
#         for j in range(1, 4): 
#             if j == 2:
#                 break
#             print(i, ":", j)              
            
            
# break 동적 절차.
# 1) 위로 올라간다
# 2) 첫 번재 만나는 반복을 종료한다.

# continue 동적 절차.
# 1) 위로 올라간다
# 2) 다음 반복을 실행한다.


# pass : 흐름제어문, 함수, 클래스
# value = 3

# if value > 3:
#     # 메뉴를 출력하라 -> 추후 구현해야됨
#     pass

# def sum(a, b, c):
#     # 3개의 값을 더한 후 반환
    
# count = 2    

for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)
    
    
# ***
# ***
# ***
# ***
# for row in range(4):
#     for _ in range(3):
#         print("*", end ="") # ***
#     if row != 3:
#         print() # Entar
        
        
    


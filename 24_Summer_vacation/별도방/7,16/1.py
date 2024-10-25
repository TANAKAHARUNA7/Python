# Sorting -> 정렬 -> 
# 1) 오름차순 : 1, 2, 3, 4
# 2) 내림차순 : 4, 3, 2, 1

# 자료구조
# 1차원 자료구조 -> List

# import random
# bar = [ random.randint(10,100) for _ in range(10) ]
# print(bar)
# # [22, 24, 39, 53, 87, 26, 98, 93, 38, 31]


# foo = [(row, item) for row in range(3) for item in range(2)]
# print(foo)

# for row in range(3):
#     for item in range(2):
#         print(row, item)
        
###########################################################

# bar = [22, 24, 39, 53, 87, 26, 98, 93, 38, 31]

# result = sorted(bar, reverse=True)  # 정렬 실행 -> 결과 값은 복사 값이 넘어온다.
# # 소팅 결과가 원본에 영향을 주지 않는다.

# print(bar)
# print(result)

#

bar = [
        [ [13, 8], [55, 85]],
        [ [10, 20], [30, 40]],
        [ [40, 50] , [60, 70]]
            
        ] 

# [ [matrix] ,           [[matrix] ,          [matrix] ]
# [[[40, 50], [60, 70]], [[13, 8], [55, 85]], [[10, 20], [30, 40]]]

# def get_value(bar):
#     return sum([ item for record in bar for item in record])
#     # sum = 0
#     # for record in bar:
#     #     for item in record:
#     #         sum += item
#     # return sum


# result = sorted(bar,  key = get_value , reverse=True) 

# print(result) 


bar = {"a": 10, "b": 20, "f": 1, "d": 9}
for item in bar:
    print(item)
    
result = sorted(bar.values())
print(result)

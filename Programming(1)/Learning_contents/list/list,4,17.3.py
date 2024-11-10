# import random

# # 리스트 생성 : bar(참조변수)
# bar = list()

# for _ in range(0, 5): # 0,1,2,3,4
#     # (random.randint(1 ,100) -> 1이상 100이하의 정수 중 난수를 한게 선택
#     bar.append(random.randint(1 ,100))
    
# print(bar)

# print(bar[-1], bar[4], bar[len(bar)-1]) # 마지막 원수를 출력하기


# bar = [10 ,20 ,30, 40, 50]

# print( bar[0] )
# print( bar[1] )
# print( bar[2] )
# print( bar[3] )
# print( bar[4] )
# # print( bar[5] )

# print( bar[-1] )
# print( bar[-2] )
# print( bar[-3] )
# print( bar[-4] )
# print( bar[-5] )

# bar = [10,20,30]
# foo = [1,2,3]
# pos = [-1,-2,-3]

# kin = pos

# pos = bar

# pos[-1] = 100

# pos = kin
# print(bar[-1],pos[-1])


# bar = [10,20,30,40]

# foo = bar[0:0:1]
# print(foo)

# foo = bar[0:1:1]
# print(foo)

# foo = bar[0:2:1]
# print(foo)

# foo = bar[0:3:1]
# print(foo)

# foo = bar[0:4:1]
# print(foo)

# foo = bar[0:4:-1]
# print(foo)

# bar = [start, stop, step] -> stepは入力しなくてもOK
bar = [10,20,30,40]
foo = bar[:] # 指定していないため元素をすべて表示
print(foo)

foo = bar[2:] # 元素3番目から最後まで
print(foo)

foo = bar[:3] # 元素0から3番目まで
print(foo)

foo = bar[-1:-4:-1] # 穴から順に4つの元素を出力。－1つづつ
print(foo)

foo = bar[-1::-1] #　穴から一番最初の元素まで１つづつ表示　75列目と同じ結果。
print(foo)

# 770225-3983813
# 3개로 구분해서 문자열로 저장
# 첫 번째 : 생녕원일 6 자리 -> 770225
# 두 번째 : 지역 코드값 6 자리 -> 3983813
# 세 번째 : 패리티 체크값 1자리 -> 3

bar = [7,7,0,2,2,5,"-",3,9,8,3,8,1,3]

num1 = bar[:6] # 1‐5番目の元素を出力。
print(num1)

num2 = bar[7:13] # 7‐12番目の元素を出力。
print(num2)

num3 = bar[-1] # 穴から1番目の元素を出力
print(num3)
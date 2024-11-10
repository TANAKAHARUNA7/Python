
bar, foo, kin = 10 ,20, 50
print(f"{bar}, {foo},{kin}")

def getValue():
     return 2, 3, 4, 5  # これもtuple

print(getValue())

print(type(getValue))


bar = [2, 3, 4, 5] # list型
foo = (6, 7, 8, 9) # ( ) <- tuple型
kin = 20, 30, 40, 50 # ( )がなくても "," でtupleと認識する。
                     # 可読性のためにも( )を使うのがいい


# print(bar[0])
# print(foo[0])

# bar[0] = 20
# foo[0] = 60

# bar = [9, 4, 5, 7]

# seo, foo, pos, kin = bar # 左側に","を使うことで、コレクション

# print(f"{seo}, {foo}, {pos}, {kin}")


# bar = foo = kin = 2
# print(bar, foo, kin)


# walrus operator

# bar = "hello"

# for char in bar:
#     print(char, end = "")
    
# print()
    
# for char in (foo := "world"): # 変数宣言と同時に活用もできる
#     print(char, end = "")   


def getCalcValues(argA, argB):
    # argA,B의 +,-,*,/ 값을 반환하는 함수 작성
    # 값 반환 시 tuple 자료형으로 ,,,
    return argA + argB , argA - argB, argA * argB, argA / argB
    

sum, substract, multiply, division, = getCalcValues(2, 3) 

print(f"{sum}, {substract}, {multiply}, {division}")

    
    
def getCalcValues(argA, argB):
    # argA,B의 +,-,*,/ 값을 반환하는 함수 작성
    # 값 반환 시 tuple 자료형으로 ,,,
    return argA + argB , argA - argB, argA * argB, argA / argB
    

kin = getCalcValues(2, 3) 

foo = list(kin) # tuple type 
foo[0] = foo[0] + 1
print(foo[0])



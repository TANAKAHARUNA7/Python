
value = int(input("정수 입력"))

if 1 < value <= 3:
    print("참")
else:
    print("거짓")    


# Lazy evaluation   ⇒　怠惰な評価

def bar(argValue):
    print("Bar is invoked")
    return argValue

if True or bar(2) == 2:
    print("참") 
else:
    print("거짓")
    
    
    
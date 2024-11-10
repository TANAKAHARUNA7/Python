# 変数を　GET　する場合　Scope chainning
#１)全域コード　→　地域変数：根本的に接近不可
#２)地域コード　→　全域変数：　 接近可能、規則に基づく


#1 
def foo():
    msg = "hello"
    print(getattr)
     
getattr = "안녕하세요!"

foo()


#2
def foo():
    nonlocal
    global msg
    msg = "hello"
        
msg = ""

foo()

print(msg)


#3
def foo():
    msg = "hello"
    
    def bar():
        nonlocal msg
        print(msg)
       
foo()


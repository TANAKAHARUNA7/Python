# Over loading
# 함수와 메서드에 적용이 된다
# 사용 목적은? 프로그래머에게 코드 작성이 편리성을 제공하기 위해
# 파이썬에서는 함수 오버로딩을 지원하지 않는다
# 가변 위지를 이용하면 함수 오버로딩 기능을 구현 할 수있다

def bar(*args):
    return sum(args)

print(bar(2, 3, 4, 5))

print(2, 3, 4)
print(2, 3)

def bar(arg_fnc):
    arg_fnc()
    
def foo():
    print("안녕하세요: ")
    
bar(foo)        



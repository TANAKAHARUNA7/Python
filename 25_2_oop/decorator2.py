
from typing import Any, Self

# デコレーターの住所は必ず１つ目の引数にはいる
def login(func):
    def wrapper():
        print("before login")
        func()
        print("after login")
        
    return wrapper

 # インタープリンターがコード解析時関数(メソッド)放出
@login
# 再定義する
def bar():
    print("bar")

bar()
bar()
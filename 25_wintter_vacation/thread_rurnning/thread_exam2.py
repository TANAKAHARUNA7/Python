import threading

# ※出力と入力を分けて管理したい時2つ生成してもいい
# この場合はprintしかないため1つでいい
my_lock = threading.Lock()

def bar():
    for count in range(1,6):
        with my_lock:
            print(f"bar: {count}")
        
def foo():
    for count in range(1,6):
        with my_lock:
            print(f"foo: {count}")
        
thread_1 = threading.Thread (target=bar)
thread_2 = threading.Thread (target=foo)

thread_1.start()
# thread_1の処理が終わるまでメインスレッドはwaiting状態
thread_1.join()

thread_2.start()

thread_2.join()

print("finish")

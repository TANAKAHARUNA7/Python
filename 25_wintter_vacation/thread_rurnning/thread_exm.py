import threading

# lock = threading.Lock()

# Target function
def bar():
    for count in range(10):
        # with lock:
            print(f"bar:{count}")

def foo():
    for count in range(10):
        # with lock:
            print(f"foo:{count}")

"""- Daemon 쓰레드 -> join()
- non-daemon 쓰레드

동기화화"""

# my_thread 객체가 생성되고, 생성된 스레드의 상태는 new        
my_thread1 = threading.Thread(target=bar)
my_thread2 = threading.Thread(target=foo)

my_thread1.start()
my_thread2.start()

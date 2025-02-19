import threading

def my_task():
    # スレッドにはそれぞれ「名前のようなID」が割り当てられる
    print(f"My Thread ID: {threading.get_ident()}")

thread = threading.Thread(target=my_task)
thread.start()

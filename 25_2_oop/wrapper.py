def is_login(func):
    def wrapper(msg:str, int:int):
        print(f"before")
        func(msg, int)
        print("after")
    
    return wrapper


@is_login # do_something = is_login(do_something)
def do_something(msg:str, int:int):
    print(f"do something: {msg}{int}")
    
do_something("h1",1) # wrapper("h1")
do_something("h2",2)


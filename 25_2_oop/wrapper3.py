
def strip(func):
    def wrapper(msg:str):
        return func(msg.strip())
    return wrapper

def upper(func):
    def wrapper(msg:str):
        return func(msg.upper())
    return wrapper


@upper 
def prt_something1(msg:str):
    print(f"prt1: {msg}")

@strip  
def prt_something2(msg:str):
    print(f"prt2: {msg}")

@upper
@strip
    
prt_something1()
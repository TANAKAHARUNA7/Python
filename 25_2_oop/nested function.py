# python -> function -> first-class citizen

# nested function
def out_func():
    name = "out_func"
    
    def in_func(id:int):
        print(f"in_func: id -> {id} at {name}")    
    
    return in_func

my_func_1 = out_func()
my_func_1(1)
my_func_1(2)
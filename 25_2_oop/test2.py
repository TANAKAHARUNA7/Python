class Bar:
    def __str__(self)->str:
        return f"Bar"
    
obj = Bar()
print(obj)

obj2 = object()
print(obj2.__str__())

print(obj.__str__)
# class Parent:
#     def prt_name(self):
#         print(self.name)
    
# class Child(Parent):
#     def __init__(self):
#         self.name = "Child"
        
# obj = Child()
# obj.prt_name()



class Parent:
    def __init__(self):
        self.name = "Parent"
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.name = "Child"
                
obj = Child()
print(obj.name)
print(Child.__mro__)
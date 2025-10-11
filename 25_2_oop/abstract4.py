class Parent:
    def prt(self):
        print("Parent")
        
class Child(Parent):
    def prt(self):
        print("Child")
        super().prt()

obj = Child()
obj.prt()        
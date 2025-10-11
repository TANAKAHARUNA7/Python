class Bar:
    # Constructor
    def __init__(self, id):
        self.id = id
        print(f"Constructor of object {self.id} if invoked")

    def __del__(self):
        print(f"Destructor of object {self.id} if invoked")    

obj1 = Bar(1)
obj2 = Bar(2)
del obj1
print("Program is terminated")
del obj2
class A:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__privace = "private"
        
obj = A()
print(obj.public)
print(obj._protected)
print(obj._A__privace)     



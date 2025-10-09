class A:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"
        # self._클래스 이름___variable name
        
class B(A):
    def prints(self):
        print(self.public) #public
        print(self._protected) # protected
        print(self.__private) # private
        
obj = B()
print(obj.public)
print(obj._protected)
print(obj._A__privace)     



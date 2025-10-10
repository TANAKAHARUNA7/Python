from abc import ABC ,abstractmethod

class A(ABC):
    @abstractmethod
    def instance_method(self):
        pass
    
    @classmethod
    @abstractmethod
    def class_method(cls):
        pass
    
    @staticmethod
    @abstractmethod
    def static_method():
        pass
    
class B(A):
    def instance_method(self):
        print("instance_method")
        
    @classmethod
    def class_method(cls):
        print("class_method")
        
    @staticmethod
    def static_method():
        print("static_method")

obj_b = B()
obj_b.instance_method()
B.class_method()
obj_b.static_method()
B.static_method()
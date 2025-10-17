from abc import ABC ,abstractmethod

class Bar(ABC):
    
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
    
    @property
    @abstractmethod
    def gett(self):
        pass
    
class Foo(Bar):
    
    def instance_method(self):
        print("instance_method")
    
    @classmethod    
    def class_method(cls):
        print("class_method")
    
    @staticmethod   
    def static_method():
        print("static_method")
        
    def gett(self):
        print("gett_instance_method")
        
        
obj_foo = Foo()
obj_foo.instance_method()
Foo.class_method()
Foo.static_method()
obj_foo.gett()
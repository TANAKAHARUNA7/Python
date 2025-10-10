# 추상화 (Abstract) -> oop
# 미완성 + 강제 구현

from abc import ABC, abstractmethod

# ABC -> Abstrac Class
class Bar(ABC):
    @property
    @abstractmethod
    def test(self):
       ... 
       
    @test.setter
    @abstractmethod
    def _(self,value):
        ...
        
class Foo(Bar):
    @property
    def test(self):
        ...

obj = Foo()
# abc모들에서 상속을 받으면 추상 클래스를 만들 수 있다
from abc import ABC, abstractmethod

# 추상 클래스를 전의
# JAVA -> abstract class Bar{ }

# Bar를 추상클래스로 정의
class Bar(ABC): 
    
    #추상 인스턴스 메서드 정의
    @abstractmethod
    def instance_method(self):
        pass

class MyClass(Bar):
    def instance_method(self):
        print("Myclass : instance_method")
        
obj = MyClass()
obj.instance_method()
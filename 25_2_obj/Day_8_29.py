# Member -> variable, method
# Member
# 1) class member -> 객체들 간의 데이터가 공유 될 때
# 2) instance member -> 

class Foo :
    # Member method
    
    # self -> this
    # instance 멤버 변수
    # 매게 변수 0
    def X(self):
        pass
        
    #cls -> class
    @classmethod
    def y(cls):
        pass
    # static member method
    @staticmethod
    def z():
        pass

obj = Foo()
obj.x()
obj.y()


# class Foo:
#     # 클래스 멤버 변수
#     z = 100
    
#     def __init__(self):
#         # 인스턴스 멤버 변수
#         self.x = 20

#     def test(self):
#         self.y = 30

# obj = Foo()
# print(obj.x)

# obj.test()


# class Foo:
#     # 2) class MV
#     age = 20
#     name = "YC Jung"
    
#     # Constructor
#     def __init__(self):    
#         # Member variable
#         # 1) instance MV
#         self.univercity = "YJU"
        


    # Member method
    # 1) instance MM
    # 2) class MM

    # Destructor
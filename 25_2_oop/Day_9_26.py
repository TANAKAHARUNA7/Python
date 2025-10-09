class A:
    def __init__(self):
        self.__age = None
    
    # Getter method
    @property
    def set_age(self):
        return f"나이는 : {self.__age}"    
    
    # Setter method
    @set_age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("음수 값 오류")
        self.__age = age

obj = A()
obj.age = 30
print(obj.age) 
obj.age = -100
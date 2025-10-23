class Foo:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 생성됨")
        
    def __del__(self):
        print(f"{self.name} 소멸됨")

x = Foo("Haruna")

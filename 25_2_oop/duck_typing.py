# Duck 클래스 생성
class Duck:
    # 오리 울음소리 메서드 생성
    def quak(self):
       print("오리입니다.Quak!")
    
# Human 클래스 생성
class Human:
    # 오리 울음소리 따라하는 사람 메서드 생성
    def quak(self):
       print("사람입니다.Quak!")
    
# 인스턴스를 가리키는 참조변수를 매개변수로 하는 함수 생성
def quak_prt(obj):
    obj.quak()

# Duck 클래스에 대한 인스턴스 생성
duck = Duck()

# Human 클래스에 대한 인스턴스 생성
human = Human()

# 함수명을 이용해서 각 클래스에 대한 울음소리 가져오기
quak_prt(duck)
quak_prt(human)

# 클래스속성
#   - count: 생성된 객체(학생)의 수를 저장(클래스변수)
class Student:
    count = 0
    
    # constractor
    def __init__(self, stdId, name, eng, kor, math):
        Student.count += 1
        self.stdId = stdId
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math
        self.id = Student.count
        
    # 합계    
    def calc_total(self):
        
        self.total = self.eng + self.kor + self.math
    
    # 평균
    def calc_average(self):
        self.average = self.total / 3
   
    # Getter 메서드
    def get_eng(self):
        print(self.name, "영어 점수: ",self.eng)
        
    def get_kor(self):
        print(self.name, "국어 점수: ",self.kor)             
    
    def get_math(self):
        print(self.name, "수학 점수: ",self.math)
    
    # Setter 메서드
    def set_eng(self, value):
        self.eng = value
              
    def set_kor(self, value):
        self.kor = value
    
    def set_math(self, value):
        self.math = value
    
    

# 학생 객체 생성
s1 = Student("2025001", "Kim", 90, 80, 85)
s2 = Student("2025002", "Lee", 70, 75, 80)

s1.calc_total()
s1.calc_average()
s2.calc_total()
s2.calc_average()
        
print(s1.id, s1.name, s1.total, s1.average)
print(s2.id, s2.name, s2.total, s2.average)
print("총 학생 수: ", Student.count)


print()
s1.get_eng()
s1.get_kor()
s1.get_math()

print()
s2.get_eng()
s2.get_kor()
s2.get_math()


s1.set_eng(20)
s1.get_eng()

# 학생 객체 개수 확인


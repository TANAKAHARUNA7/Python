class Student:
    # 현재까지 생성된 객체 수를 저장. 초기값 0
    __id_count = 0
    
    # 생성자 
    # 메개 변수:name, id->id_count 값을 부여, gender
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.id = Student.__id_count
        self.gender = gender
        
        # 객체 생성되면 id_count를 1 증가
        Student.__id_count += 1       
    
    # instansmethod
    # 국·영·수 점수를 입력받아 멤버 변수에 저장
    def set_score(self, korea, math, eng):
        self.grade_korea = korea
        self.grade_math = math
        self.grade_english = eng 
        # total과 avg를 계산하여 멤버 변수에 저장
        self.total = self.grade_korea + self.grade_math + self.grade_english
        self.avg = self.total / 3 

    def get_total_avg(self):
        return self.total,self.avg

    # classmethod
    # 현재 생성된 객체 수(__id_count)를 반환
    @classmethod
    def get_id_count(cls):
        return Student.__id_count
    
    # staticmethod
    # 세 과목 점수를 인자로 받아 평균을 반환할 것
    @staticmethod
    def get_avg(arg1, arg2, arg3):
        return (arg1 + arg2 + arg3) / 3 
        
# 객체 생성
s1 = Student("Alice", 15, "F")
s2 = Student("Bob", 25, "M")

# 점수 입력
s1.set_score(90, 85, 92)
s2.set_score(75, 80, 78)

# 총점과 평균 출력
print(s1.get_total_avg())
print(s2.get_total_avg())

# 클래스 메서드 호출 (현재 생성된 객체 수)
print(Student.get_id_count())

# 정적 메서드 호출 (별도의 객체 없이 평균 계산)
print(Student.get_avg(100, 90, 80))
class Student:
    def __init__(self, id:int)-> None:
        # 생성자: 객체가 생성될 때 자동으로 호출됨
        # 학생의 id와 점수를 초기화
        self.id = id
        self.kor = 0
        self.eng = 0
        self.math = 0
        
    def __call__(self, kor:int, eng:int, math:int) -> None:
        # __call__ 매직 메서드:
        # 인스턴스를 '함수처럼 호출'했을 때 자동 실행됨
        # ex) std1(10, 20, 30) -> 이 메서드가 실행
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def __str__(self) -> str:
        # __str__ 매직 메서드:
        # print() 함수나 str() 함수로 출력할 때 자동 실행
        # 객체의 문자열 표현을 정의
        return f"KOR: {self.kor}, ENG: {self.eng}, MATH: {self.math}"
        
    def __eq__(self, value: "Student") -> bool:
        # __eq__ 매직 메서드:
        # '==' 연산자를 사용했을 때 자동 실행
        # 기본 object.__eq__는 메모리 주소 비교 -> 서로 다른 객체는 False
        # 여기서는 'id' 속성 값이 같으면 같은 학생으로 간주
        return self.id == value.id
    

        
std1 = Student(1)
std2 = Student(1)

print(std1 == std2)  # True

std1(10, 20, 30)


# 학생들의 성적을 키보드로부터 입력 받아 리스트에 저장하고 입력 값을 출력한다.

count = 0
student_allscore_avrg = 0.0
student_list = []

def student_information(id, name, national_language, english, math):
    total = math + english + national_language
    average = total / 3
    student_list.append([id, name, national_language, english, math, total, average])
    
    # Calculate the new overall average
    global student_allscore_avrg
    student_allscore_avrg = sum([student[6] for student in student_list]) / len(student_list)
        

while True:
    
    print("=" * 20)
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력 순)")
    print("3. 프로그램 종료")
    print("=" * 20,"\n")

    print(f"현 입력데이터 갯수: {count}")
    print(f"전체 학생 평균 값: {student_allscore_avrg:.2f}","\n")
    
    menu = int(input())
    
    # 학생 성적의 입력을 받는다
    if menu == 1:
        # id = input("학번을 입력하세요\n")
        # name = input("이름을 입력하세요\n")
        # national_language = int(input("국어 성적을 입력하세요\n"))
        # english = int(input("영어 성적을 입력하세요\n"))
        # math = int(input("수학 성적을 입력하세요\n"))
        
        id = 10
        name = "gtthtrh"
        national_language = 70
        english = 90
        math = 80
        # sum = math + english + national_language
        # avrg = sum / 3
        
        # student_list.append([id, name, national_language, english, math, sum, avrg])
        # student_allscore_avrg = ( student_allscore_avrg + avrg ) / len(student_list)
        
        student_information(id,name,national_language,english,math)
        count += 1
        
        
    elif menu == 2:
        for col in student_list:
                print(f"[ id : {col[0]} name : {col[1]} kor : {col[2]} eng : {col[3]} math : {col[4]} sum : {col[5]} avg : {col[6]:.2f}")
                   
    else:
        print("프로그램 종료")
        break
    
    
    
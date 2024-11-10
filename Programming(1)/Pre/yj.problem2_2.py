# 세과목 점수를 입력 받아 평균 점수를 계산하고, 평균에 따른 학점 등급을 부여하는 프로그램
# 학점 등급은 평균 점수에 따라 다음과같이할당됩니다:
# A: 90점 이상
# B: 80점 이상 90점 미만
# C: 70점 이상 80점 미만
# D: 60점 이상 70점 미만
# F: 60점 미만

def calculate_average(math_score, science_score, english_score):
     average = (math_score + science_score + english_score) / 3 
     if average >= 90 :
         level = "A"
     elif 80 <= average < 90:
         level = "B"
     elif  70  <= average < 80:
         level = "C"
     elif 60 <= average < 70:
         level = "D"
     else:
         level = "F"
     print("평균 점수는", average ,"점이고, 학점은 ",level ,"입니다.")
     return

# 사용자로부터수학, 과학, 영어의점수를입력받습니다.
math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("수학 점수를 입력하세요: "))
english_score = float(input("수학 점수를 입력하세요: "))

average = calculate_average(math_score, science_score, english_score)

# 계산된 평균 점수를 사용하여 학점 등급을 결정합니다.
# if average >= 90 :
#     print("평균 점수는", average ,"점이고, 학점은 A 입니다.")

# elif 80 <= average < 90:
#     print("평균 점수는", average ,"점이고, 학점은 B 입니다.")

# elif  70  <= average < 80 :
#     print("평균 점수는", average ,"점이고, 학점은 C 입니다.")
    
# elif 60 <= average < 70:
#     print("평균 점수는", average, "점이고, 학점은 D 입니다.")
    
# else:
#     print("평균 점수는", average ,"점이고, 학점은 F 입니다.")




# 각과목의점수와함께평균점수및해당하는학점등급을출력합니다
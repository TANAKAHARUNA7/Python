# For 문을사용하여 아래 학생들의 성적에 대한 총합,평균,학생수를 출력하는 프로그램

score = [99, 29, 30, 40, 20, 60]
student_num = 0
sum = 0

for score_value in score:
    student_num += 1
    sum += score_value
avg = sum / student_num
    
print("학생 수 : ",student_num, ", 총점 : ",sum, ", 평균 : ", avg)

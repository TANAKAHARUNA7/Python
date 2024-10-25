# 학생들의 점수 리스트
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99]

# 점수를분류
# 90~점: '우수’
# 70~89점: '양호’
# 50~69점: '보통’
# ~49점: '미흡’
scores_avg_1 = [num for num in scores if num >= 90 ]
scores_avg_2 = [num for num in scores if 70 <= num < 90 ]
scores_avg_3 = [num for num in scores if 50 <= num < 70 ]
scores_avg_4 = [num for num in scores if num < 50 ]

# 각 분류에 따른 점수의 평균을 계산하고, 분류된 점수 리스트와 각 분류의 평균 점수를출력
print("우수: ",scores_avg_1 , "평균: ", sum(scores_avg_1) / len(scores_avg_1))
print("양호: ",scores_avg_2 , "평균: ", sum(scores_avg_2) / len(scores_avg_2))
print("보통: ",scores_avg_3 , "평균: ", sum(scores_avg_3) / len(scores_avg_3))
print("미흡: ",scores_avg_4 , "평균: ", sum(scores_avg_4) / len(scores_avg_4))

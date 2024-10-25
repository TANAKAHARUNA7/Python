# 학생들의 점수 리스트
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89]

# 점수를 분류:
scores_avgA = [num for num in scores if num >= 90 ] # 90점 ~ : 'A' 
scores_avgB = [num for num in scores if 80 <= num < 90] # 80 ~ 89점 : 'B' 
scores_avgC = [num for num in scores if 70 <= num < 80] # 70 ~ 79점 : 'C' 
scores_avgD = [num for num in scores if 60 <= num < 70] # 60 ~ 69점 : 'D' 
scores_avgF = [num for num in scores if num < 60 ] # ~ 59점 : 'F' 

# 등급 평균점수를 계산한다.
avgA = (sum(scores_avgA) / len(scores_avgA))
avgB = (sum(scores_avgB) / len(scores_avgB))
avgC = (sum(scores_avgC) / len(scores_avgC))
avgD = (sum(scores_avgD) / len(scores_avgD))
avgF = (sum(scores_avgF) / len(scores_avgF))

star = "*"
# 결과를 출력
print("등급 분포 및 평균 점수: ")
print(f"A 등급: 평균점수 = {avgA:.2f}\n{star * len(scores_avgA)} ({len(scores_avgA)}명)")
print(f"B 등급: 평균점수 = {avgB:.2f}\n{star * len(scores_avgB)} ({len(scores_avgB)}명)")
print(f"C 등급: 평균점수 = {avgC:.2f}\n{star * len(scores_avgC)} ({len(scores_avgC)}명)")
print(f"D 등급: 평균점수 = {avgD:.2f}\n{star * len(scores_avgD)} ({len(scores_avgD)}명)")
print(f"F 등급: 평균점수 = {avgF:.2f}\n{star * len(scores_avgF)} ({len(scores_avgF)}명)")


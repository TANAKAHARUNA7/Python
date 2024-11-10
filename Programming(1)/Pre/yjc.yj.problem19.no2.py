scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89]

li = [[score for score in scores if scores >= 90],
[score for score in scores if 80 <= scores < 90],
[score for score in scores if 70 <= scores < 80],
[score for score in scores if 60 <= scores < 70],
[score for score in scores if scores < 60]]

avg_li = []
for lists in li:
       avg = 0
       for i in lists:
              avg += i
       avg_li.append(avg / len(lists))
       
level = ["A", "B", "C", "D", "F"]

print("등급 분포 및 평균 점수: ")
for i in range(5):
       print(f"{level[i]} 등급: 평균 점수 = {avg_li[i]:.2f}\n{"*" * len(li[i])}({len(li[i])}명)")
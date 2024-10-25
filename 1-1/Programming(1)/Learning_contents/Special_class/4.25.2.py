# 90점 이상이면 A
# 80점 이상이면 B
# 70점 이상이면 C
# 60점 이상이면 D
# 60점 이상이면 F
input_value = int(input("성적 입력: "))

level = ""
if input_value >= 90 :  # 90 <= input_value 
    level = "A"
elif input_value >= 80 : # 80 <= input_value < 90
    level = "B"
elif input_value >= 70 : # 70 <= input_value < 80
    level = "C"
elif input_value >= 60 : # 60 <= input_value < 70
    level = "D"
else :            # 60 > input_value
    print(level)
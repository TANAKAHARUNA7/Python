
def calulate_attendance_score(hours_per_week, absence_hours, tardy_count ):
       #総授業時間        =  時数/週       ×  15
       total_class_hours = hours_per_week * 15
       # 全欠席時間　　＝　　遅刻3回は欠席1時間で処理
       additional_time = (tardy_count // 3 ) + absence_hours
       # 出席スコア =     20点-（20×欠席時間数/総授業時間数）
       attendance_score = 20 - ( 20 * additional_time / total_class_hours)
        # 欠席時数が総授業時数の1/4を超える場合、F処理
       if  additional_time > total_class_hours / 4:
           print("あなたの出席点数はF単位です。")
       else :
           print("あなたの出席点数",round(attendance_score,2) ,"です。") # 小数点をつけて第2まで表示
           
# ユーザーから1）週あたりの授業時間（時数/週）、2）欠席した総時間、3）遅刻回数の入力を受ける
hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))

calulate_attendance_score(hours_per_week, absence_hours, tardy_count )










# 
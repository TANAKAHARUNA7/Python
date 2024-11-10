#  사전 예약 시스템 시뮬레이터
# 1)나이, 2)이벤트코드, 3)날짜,에 따라 예약 가능 여부를 판단하고 그에 따른 결과를 출력한다.
# 사용자로부터 나이,날짜,이벤트코드를 입력을 받는다.
age = int(input("나이를 입력하세요: "))
event_code = (input("예약하려는 이벤트 코드를 입력하세요: "))
dareservation_date = int(input("원하는 예약날짜를 입력하세요: "))

#  'E1' 18세 이상만 예약 가능.
#  'E2' 날짜는 짝수일에만 예약 가능.
#  'E3' 16세 이상만 예약할 수 있으며, 7의 배수인 날짜에만 예약 가능.
if ( 1 <= dareservation_date <= 30 ) and event_code == "E1" or event_code == "E2" or event_code == "E3":
    # 나이 제한
    if  event_code == "E1" and age < 18 or event_code == "E3" and age < 16 :
        print("나이 제한으로 인해 예약할 수 없습니다.")  
    # 날짜 제한            
    elif event_code == "E2" and dareservation_date % 2 != 0 or  event_code == "E3" and dareservation_date % 7 != 0:
        print("선택하신 날짜에는 예약할 수 없습니다.")
    # 예약 완료
    else:
        print("예약이 완료되었습니다!")
    # 오류
else:
    print("잘못된 입력입니다. 프로그램을 종료합니다")
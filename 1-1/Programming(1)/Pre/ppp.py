import random

# data = [["これ", "ここ","こちら","この", "こんな","こう"],\
#     ["それ", "そこ", "そちら", "その", "そんな", "そう"],\
#     ["あれ", "あそこ", "あちら", "あの", "あんな", "ああ"],\
#     ["どれ", "どこ", "どちら", "どの", "どんな", "どう"]]
data = [["이것", "여기","이쪽","이", "이런","이렇게"],
        ["그것", "거기", "그쪽", "그", "그런", "그렇게"],
        ["저것", "저기", "저쪽", "저", "저런", "저렇게"],
        ["어느 것", "어디", "어느 쪽", "어느", "어떤", "어떻게"]]

def test(input_ans):
    
    if data[choice_li][choice_li2] == input_ans:
        return "딩동댕! 정답!!"
    else:
        return "땡!"
    
    # if choice_li == "근칭" :
    #         if choice_li2 == "사물" and input_ans == "これ": # 이것
    #             msg = "딩동댕! 정답!!"    
    #         elif choice_li2 == "장소" and input_ans == "ここ": # 여기
    #             msg = "딩동댕! 정답!!"
    #         else:  
    #             msg = "땡!" 
    # return msg

while True:
    
    li = ["근칭", "중칭", "원칭", "부정칭"]
    li2 = ["사물", "장소", "방향", "연체사", "연체사2","부사"]
    
    # list의 index를 random으로 선택
    choice_li = random.randrange(0, len(li))
    choice_li2 = random.randrange(0, len(li2))
    
    # 리스트의 원소를 index으로 출력
    print(f"컴퓨터는 {li[choice_li]}과 {li2[choice_li2]}를 선택했습니다.")
    
    while True:
        input_ans = input("맞는 답을 입력 하세요: ")
        
        msg = test(input_ans)
        
        # 리벤지 종료 처음부터
        print(msg)
        input_msg = int(input("메뉴를 선택하세요-> 1.리벤지 2.처음부터 3.종료: "))
        if input_msg == 1:
            continue
        elif input_msg == 2:
            break
        elif input_msg == 3:
            break
    
    if input_msg == 3:
        break

print("수고했습니다")
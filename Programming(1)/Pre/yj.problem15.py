
import random 
jyanken_win_count = 0
jyanken_lose_count = 0
jyanken_draw_count = 0
jyanken_count = 0

jyanken_pc = ["가위","바위","보"]

# 사용자로부터 가위,바위,보 중 하나를 입력받는다. 
while jyanken_win_count >= 2 or jyanken_lose_count >=2 :
    
    jyanken_input = input("가위,바위,보 중 하나를 입력하세요: ")
    
    if ( jyanken_input == "가위" ) or ( jyanken_input == "바위" ) or ( jyanken_input == "보" ):
        pc_input = random.choice(jyanken_pc) 
        print("컴퓨터: ",pc_input)
        
        if jyanken_pc == jyanken_input:
            jyanken_draw_count += 1
            jyanken_count += 1
            print("무승부! 현재 전적: ",jyanken_win_count,"승", jyanken_lose_count, "패", jyanken_draw_count, "무")
            
        elif ( jyanken_input == "가위" and pc_input == "바위" ) or ( jyanken_input == "바위" and pc_input == "보" ) or ( jyanken_input == "보" and pc_input == "가위" ):
            jyanken_win_count += 1
            jyanken_count += 1
            print("승리! 현재 전적: ",jyanken_win_count,"승", jyanken_lose_count, "패", jyanken_draw_count, "무")
        elif ( jyanken_input == "바위" and pc_input == "가위" ) or ( jyanken_input == "보" and pc_input == "바위" ) or ( jyanken_input == "가위" and pc_input == "보" ):
            jyanken_draw_count += 1
            jyanken_count += 1
            print("패! 현재 전적: ",jyanken_win_count,"승", jyanken_lose_count, "패", jyanken_draw_count, "무")
        
        else:
            print("가위,바위,보 중에서 선택하세요.")
    print("전적: ",jyanken_win_count,"승", jyanken_lose_count, "패", jyanken_draw_count, "무")       
    
    
# 컴퓨터가 선택한 값과 대결하여 승,패,무를 판단하고 결과를 출력한다.


# 게임은 3판 2선승제로 진행


# 매 게임마다 승, 패, 무의 결과가 출력


# 게임이 종료되면 전체 승, 무, 패의 결과와 최종 승자를 출력


# "가위", "바위", "보" 이외를 입력되면 다시입력
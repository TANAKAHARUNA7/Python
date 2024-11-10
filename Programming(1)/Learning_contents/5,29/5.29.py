maker = input("input model\t")

# M3, M5, M7 -> BMW
# Y, X       -> Tesla
# ES, LS     -> Lexus 
# G80, G90   -> Hyundai
# 이외 모델   -> "알수 없는 모델입니다."

list_BMW = ["M3", "M5", "M7", "M1", "M2", "M6", "M8","M9"]
list_Tesla = ["Y", "X"]
list_Lexus = ["ES", "LS"]
list_Hyundai = ["G80", "G90"]

list_model = [list_BMW ,list_Tesla, list_Lexus, list_Hyundai]
maker_name_list = ["BMW" ,"Tesla", "Lexus", "Hyundai"]
index_count = 0

# 회사 목록을 가지고 온다. 반복 -> 4회 -> BMW, tesla, lexus, hyundai
# 세로 반복
for maker_list in list_model:
    for model_in_list in maker_list:
        if maker == model_in_list:
            break
        
    if maker != "":
        break
    
    index_count += 1




maker = "알수 없는 모델입니다."

for BMW in list_BMW:
    if BMW == model: 
        maker = "BMW"
        break

if maker == "":
    for Tesla in list_Tesla:
        if Tesla == model:
            maker = "Tesla"
            break
        
if maker == "":    
    for Lexus in list_Lexus:
        if Lexus == model:
            maker = "Tesla" 
            break 
         
if maker == "":        
    for Hyundai in list_Hyundai:
        if Lexus == model:
            maker = "Hyundai" 
            break
 
print(maker)



    
if model in list_BMW:
    maker = "BMW"   
    

# maker = ""

# if  car == "M3" or car == "M5" or car == "M7":
#     maker = "BMW"
# elif car == "Y" or car == "X":
#     maker = "Tesla"  
# elif car == "ES" or car == "LS":
#     maker = "Lexus"
# elif car == "G80" or car == "G90":
#     maker = "Hyundai"    
# else:
#     maker = "알수 없는 모델입니다."        
# print(maker)      
    
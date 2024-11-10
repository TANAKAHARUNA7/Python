

import random


trial_count = 1000

dice_list = [0, 0, 0, 0, 0, 0]

# trial_count 만큼 렌덤 숫자를 발생 : 1 ~ 6
for _ in range(trial_count):
    
    rand_num = random.randint(1,6)
    
    dice_list[rand_num - 1] += 1
    
max = -1
for index in dice_list:
    if dice_list[index] > max:
        max = dice_list[index]
        
# 히스토


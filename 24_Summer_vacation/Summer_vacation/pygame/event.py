
import random
import pygame
pygame.init()

# 画面設定
screen = pygame.display.set_mode((640,480))
x = screen.get_width() 
y = screen.get_height()

# 障害物四角形
ob_rect_width = 60
ob_rect_hight = 60
blue = (0, 0, 255)
ob_rect_list = []
for _ in range(random.randint(1,6)):
    while True:
        ob_rect_x = random.randint(10, x)
        ob_rect_y = random.randint(10, y)
        ob_rect = pygame.Rect(ob_rect_x, ob_rect_y, ob_rect_width, ob_rect_hight)
        
        if ob_rect.collidelist(ob_rect_list) == -1:
            ob_rect_list.append(ob_rect)
            break




# 使用者の定義のイベント生成
SPAWN_ENEMY = pygame.USEREVENT + 1

pygame.time.set_timer(SPAWN_ENEMY, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == SPAWN_ENEMY:
            print("Spawn new enemy!")
    screen.fill((255, 255, 255))
    
    for ob_rect in ob_rect_list:     
        pygame.draw.rect(screen, blue, ob_rect)
    
    pygame.display.flip()

pygame.quit


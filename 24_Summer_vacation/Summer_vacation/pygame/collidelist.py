
import pygame
pygame.init()

#　画面設定
screen = pygame.display.set_mode((640,480))
x = screen.get_width()
y = screen.get_height()

# rect作成
rect_list = [
    pygame.Rect(20, 20, 40, 40),
    pygame.Rect(100, 100, 50, 50),  
    pygame.Rect(300, 60, 60, 60)
    ]  

# 速度設定
rect_0_spd = [10, 10]
rect_1_spd = [4, 9]
rect_2_spd = [5, 8]

# 衝突を感知する
big_rect = pygame.Rect(120, 130, 100, 100)

# 色の定義
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

#　fps設定
clock = pygame.time.Clock()
fps = 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(fps) / 1000.0
    
    rect_list[0] = rect_list[0].move(rect_0_spd)
    rect_list[1] = rect_list[1].move(rect_1_spd)
    rect_list[2] = rect_list[2].move(rect_2_spd)
    
    if rect_list[0].left < 0 or rect_list[0].right > x:
        rect_0_spd[0] = -rect_0_spd[0]  
    if rect_list[0].top < 0 or rect_list[0].bottom > y:
        rect_0_spd[1] = -rect_0_spd[1]     
        
    if rect_list[1].left < 0 or rect_list[1].right > x:
        rect_1_spd[0] = -rect_1_spd[0]  
    if rect_list[1].top < 0 or rect_list[1].bottom > y:
        rect_1_spd[1] = -rect_1_spd[1]       
        
    if rect_list[2].left < 0 or rect_list[2].right > x:
        rect_2_spd[0] = -rect_2_spd[0] 
    if rect_list[2].top < 0 or rect_list[2].bottom > y:
        rect_2_spd[1] = -rect_2_spd[1]       
        
    # 衝突を感知
    index = big_rect.collidelist(rect_list)
    # if big_rect.collidelist(rect_list) != -1:
    if index != -1:
        print("衝突を感知")    
        
    
    # 絵を描写
    screen.fill((255,255,255))
    pygame.draw.rect(screen, yellow, rect_list[0])
    pygame.draw.rect(screen, red, rect_list[1])
    pygame.draw.rect(screen, blue, rect_list[2])
    pygame.draw.rect(screen, black, big_rect)
    
    pygame.display.flip()
    
            
pygame.quit()
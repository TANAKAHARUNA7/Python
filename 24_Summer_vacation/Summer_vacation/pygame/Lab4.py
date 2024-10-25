# クリックするたびに新しい場所に円が描画され、円の色がランダムに変化するように設定。
import pygame
pygame.init()
import random

screen = pygame.display.set_mode((800,600))

screen_x = screen.get_width()
screen_y = screen.get_height()

# 色の定義
White = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill(White)
            # 円の大きさ
            radius = random.randint(10,100)
            # 色の定義
            color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            pygame.draw.circle(screen,color,event.pos,radius)
            
            pygame.display.flip()    
    
pygame.quit()
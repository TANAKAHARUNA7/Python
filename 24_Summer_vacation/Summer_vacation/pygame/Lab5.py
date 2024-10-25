import pygame
import random

pygame.init()

# 画面のサイズを設定
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
# 中心点を求める
x = screen_width // 2
y = screen_height // 2

# 色
white = (255, 255, 255)
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
screen.fill(white)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # lineを描く                  # 始点の(x, y)は現在の位置を示す
                pygame.draw.line(screen, color, (x, y), (x, y - 10), 5) # 5 -> 線の太さをピクセル単位であらわす
                y -= 10
            elif event.key == pygame.K_DOWN:
                pygame.draw.line(screen, color, (x, y), (x, y + 10), 5)
                y += 10    
            elif event.key == pygame.K_LEFT:
                pygame.draw.line(screen, color, (x, y), (x - 10, y), 5)
                x -= 10   
            elif event.key == pygame.K_RIGHT:
                pygame.draw.line(screen, color, (x, y), (x + 10, y), 5)
                x += 10  
                
            pygame.display.flip()
    
pygame.quit()
                
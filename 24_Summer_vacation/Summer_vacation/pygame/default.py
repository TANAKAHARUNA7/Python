
import pygame
pygame.init()

# 画面設定
screen = pygame.display.set_mode((640,480))
x = screen.get_width()
y = screen.get_height()

#　fps設定
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #　絵を描写
    screen.fill((255,255,255))
    

    
    pygame.display.flip()
    
            
pygame.quit()
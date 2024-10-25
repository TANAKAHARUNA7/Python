import pygame
import random

pygame.init()

#　スクリーンの大きさ
screen = pygame.display.set_mode((800,600))

#　スクリーンの大きさを変数へ保存
screen_x = screen.get_width()
screen_y = screen.get_height()

clock = pygame.time.Clock()

# 色の定義
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# while文の中に書いてしまうとずーっと絵が回り続ける
# screen.fill(WHITE)

# randam_num = random.randint(5,20)
# for _ in range(randam_num):
#     #3)サークルサイズをランダムに
#     radius = random.randint(10, 100)
#     #2)色をランダムに
#     color_random = (random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))
#     #1)位置をランダムに
#     x_randam = random.randint(0 + radius, screen_x - radius)
#     y_randam = random.randint(0 + radius, screen_y - radius)
#     #3)画面を超えないように
#     pygame.draw.circle(screen,color_random,(x_randam,y_randam),radius)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.display.flip()
    
    screen.fill(WHITE)

    randam_num = random.randint(5,20)
    for _ in range(randam_num):
        #3)サークルサイズをランダムに
        radius = random.randint(10, 100)
        #2)色をランダムに
        color_random = (random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))
        #1)位置をランダムに
        x_randam = random.randint(0 + radius, screen_x - radius)
        y_randam = random.randint(0 + radius, screen_y - radius)
        #3)画面を超えないように
        pygame.draw.circle(screen,color_random,(x_randam,y_randam),radius)
    
    clock.tick(1)
    
pygame.quit()
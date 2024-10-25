import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 画面縦、横の大きさを出力
print(screen.get_width(), screen.get_height())

#　中心点の座標を計算
center_x = int(screen.get_width() / 2)
center_y = int(screen.get_height() / 2)

#　色の定義
     # 赤　緑　青  
RED = (255, 222, 200)
GREEN = (200, 255, 222)
BLUE = (255, 200, 255)

# 点を書く
pygame.draw.circle(screen, RED, (center_x, center_y), 40) 
pygame.draw.circle(screen, GREEN, (0,0), 40)
pygame.draw.circle(screen, BLUE, (799, 599), 40)
pygame.display.flip()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
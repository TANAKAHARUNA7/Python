import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
   
# 円の設定
Red = (255, 0, 0)
radius = 50     
#　円の初期位置
x = 50
y = 240   
# 円の移動速度
speed = 5
    
runnning = True
while runnning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
        
    screen.fill((255, 255, 255))
    
    # 現在のX座標 += speed    
    x += speed
    # x位置はいつもアップデートされ
    if x > 640 - radius or x < radius:
        speed = -speed
            
    pygame.draw.circle(screen, Red, (x, y),radius)
    pygame.display.flip()
        
    clock.tick(60)
        
pygame.quit()    
    
    
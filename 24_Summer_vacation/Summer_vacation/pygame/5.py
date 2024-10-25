
## -----> 初期化
import pygame
pygame.init()
##　←－－－‐‐‐

screen = pygame.display.set_mode((640,480))

# 1秒間に何回while文を実行するのか
clock = pygame.time.Clock()

x = screen.get_width() / 2
y = screen.get_height() / 2


#　1秒に5枚Imgを作成
fps = 5
count = 0
radius = 40

# 1秒にピクセルが動くスピード
speed = 1
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    dt = clock.tick(fps)/1000.0
    screen.fill((255,255,255))        
    pygame.draw.circle(screen,(255,0,0),(x,y),radius)

    x += 10
    
    if  + 
    
    print(count)
    count += 1    
    clock.tick(fps) 
            
pygame.quit()
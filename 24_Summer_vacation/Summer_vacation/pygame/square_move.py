
import pygame
pygame.init()

# 画面設定
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collidelist Example")

# 色の定義
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Rectリスト
obstacles = [
    pygame.Rect(150, 100, 100, 100),
    pygame.Rect(300, 300, 150, 50),
    pygame.Rect(500, 200, 50, 150),
    pygame.Rect(400, 400, 200, 50)
]

# 移動するRect生成
moving_rect = pygame.Rect(50, 50, 50, 50)
# speed 
speed = 100

#　fps設定
clock = pygame.time.Clock()
fps = 60


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(fps) / 1000.0
    
    # 元の位置を保存
    position = moving_rect.topleft
    
    # キー入力保存    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += speed * dt    
    if keys[pygame.K_UP]:
        moving_rect.y -= speed * dt    
    if keys[pygame.K_DOWN]:
        moving_rect.y += speed * dt    
    
    # 障害物感知        
    if moving_rect.collidelist(obstacles) != -1:
        moving_rect.topleft = position   
    
    # 画面の外に出ないように設定    
    moving_rect.x = max(0, min(moving_rect.x , screen_width - moving_rect.width)) 
    moving_rect.y = max(0, min(moving_rect.y , screen_height - moving_rect.height))  
        
    #　絵を描写
    screen.fill((255,255,255))
    # 障害物
    for rect in obstacles:
        pygame.draw.rect(screen, blue, rect)
    # 動く四角形    
    pygame.draw.rect(screen, red, moving_rect)
    
    pygame.display.flip()
    
            
pygame.quit()
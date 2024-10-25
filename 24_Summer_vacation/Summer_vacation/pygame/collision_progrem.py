import pygame

pygame.init()

screen_width, screen_height = (800, 600)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collidelist Example')

WHITE = (255, 255, 255)
Blue = (0, 0 ,255)
Red = (255, 0, 0)

# Rectリスト生成
obstacles = [
    pygame.Rect(150, 100, 100, 100),
    pygame.Rect(300, 300, 150, 50),
    pygame.Rect(500, 200, 50, 150),
    pygame.Rect(400, 400, 200, 50)
    
]

# 移動するRect生成
moving_rect = pygame.Rect(50, 50, 50, 50)

# 移動速度決定
velocity = 300

# Fps 制御のためのClockオブジェクトを生成
clock = pygame.time.Clock()

#　ゲームループ
running = True
while running:
    #　イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
     
    #　以前の位置を保存
    previous_position = moving_rect.topleft
            
    # デルタタイムの計算
    dt = clock.tick(60) / 1000.0
    
    # キーの入力処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= velocity * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += velocity * dt
      
    # 衝突感知    
    collision_index = moving_rect.collidelist(obstacles)
    if collision_index != -1:
        print(f"Collisio with obstacle {collision_index}")
        
        # 衝突が発生した場合以前の位置に戻る
        moving_rect.topleft = previous_position
        
    moving_rect.x = max(0,min(moving_rect.x, screen_width - moving_rect.width))
    moving_rect.y = max(0,min(moving_rect.y, screen_height - moving_rect.height))    
        
    screen.fill(WHITE)
    
    # 障害物生成
    for obs in obstacles:
        pygame.draw.rect(screen,Blue, obs)
        
    # 移動するRectの生成
    pygame.draw.rect(screen, Red, moving_rect)
        
    pygame.display.flip()
    
pygame.quit()   
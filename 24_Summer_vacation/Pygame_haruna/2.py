import random
import pygame

pygame.init()

# バックグラウンド設定
background_music = pygame.mixer.music.load("Yogurt Shake.mp3")
pygame.mixer.music.play(-1)

# スクリーン設定
screen_width = 1800
screen_height = 1200
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# 動く四角形の定義
moving_rect_width = 50
moving_rect_height = 40
mov_rect_x = screen_width // 2 - moving_rect_width // 2
mov_rect_y = screen_height - moving_rect_height - 5
moving_rect = pygame.Rect(mov_rect_x, mov_rect_y, moving_rect_width, moving_rect_height)

# ターゲット設定
# 大きさ
target_width = 80
target_height = 80
# 数
target_value = 20
# 色
blue = (0, 255, 0)
black = (0, 0, 0)

speed = 300
    
# リスト
target_list = []
target_speed_list = []
for _ in range(target_value):
    while True:
        target_x = random.randint(0, screen_width - target_width)
        target_y = random.randint(0, 900)
        target = pygame.Rect(target_x, target_y, target_width, target_height)
        if target.collidelist(target_list) == -1:
            target_list.append(target)
            # ランダムなスピードと方向
            speed_x = random.choice([-1, 1]) * random.randint(600, 600)  # 左右
            speed_y = random.choice([-1, 1]) * random.randint(600, 600)  # 上下
            target_speed_list.append([speed_x, speed_y])
            break

# 銃弾の定義
bubble_image = pygame.image.load("heart3.png")
bubble_rect = bubble_image.get_rect()
bubble_value = 30

# 銃弾のリスト作成
bubble_list = []

# フォント設定
font = pygame.font.SysFont('bizudpminchomediumtruetype', 36) # 他のフォントを使用したい場合

# timer開始時間
start_time = pygame.time.get_ticks()

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_bubble_rect = bubble_image.get_rect()
                new_bubble_rect.midtop = moving_rect.midtop
                # 銃弾をリストに追加
                bubble_list.append(new_bubble_rect)
                    
    dt = clock.tick(60) / 1000                 
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 # 秒単位で返還  
    
    # 画面を白に
    screen.fill((255, 255, 255))
    
    # タイマーを画面に表示  
    timer_text = font.render(f"Time: {elapsed_time:.2f} seconds", True, black)
    screen.blit(timer_text, (10, 10))

    # ターゲットの移動
    for i, target_rect in enumerate(target_list):
        # ターゲットを動かす
        target_rect.x += target_speed_list[i][0] * dt
        target_rect.y += target_speed_list[i][1] * dt

        # 画面の端でバウンドする
        if target_rect.left <= 0 or target_rect.right >= screen_width:
            target_speed_list[i][0] *= -1  # 横方向のスピードを反転
        if target_rect.top <= 0 or target_rect.bottom >= screen_height - 100:
            target_speed_list[i][1] *= -1  # 縦方向のスピードを反転
    
    # 弾丸の処理
    for bubble in bubble_list[:]:
        bubble.y -= speed * dt
        if bubble.y < 0:  
            bubble_list.remove(bubble)
        
    # プレイヤーの動きを処理
    keys = pygame.key.get_pressed()
    
    # 左方向キーを押したとき
    if keys[pygame.K_LEFT]:
        moving_rect.x -= speed * dt      

    # 右方向キーを押したとき
    if keys[pygame.K_RIGHT]:
        moving_rect.x += speed * dt 
            
    # 衝突感知
    for fire_rect in bubble_list[:]:
        is_collision = False
        for i, target in enumerate(target_list[:]):
            if fire_rect.colliderect(target):
                target_list.remove(target)
                target_speed_list.pop(i)
                is_collision = True
        if is_collision:
            bubble_list.remove(fire_rect)
    
    # ゲームオーバーの定義
    if elapsed_time > 30:
        print("30秒経過、ゲーム終了")
        running = False
    if len(bubble_list) == 20:
        print("弾切れ、終了")   
        running = False 
    
    # ターゲットの描画
    for target_rect in target_list:    
        pygame.draw.rect(screen, (0, 0, 255), target_rect)

    # プレイヤーの描画
    moving_rect.x = max(0,min(moving_rect.x, screen.get_width() - moving_rect_width))
    pygame.draw.rect(screen, (255, 0, 0), moving_rect)
    
    # 弾丸の描画
    for bubble_rect in bubble_list:
        screen.blit(bubble_image, bubble_rect) 
         
    pygame.display.flip()
            
pygame.quit()
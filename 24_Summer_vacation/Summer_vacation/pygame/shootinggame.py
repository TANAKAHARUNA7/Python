import random
import pygame

pygame.init()

# バックグラウンド設定
background_music = pygame.mixer.music.load("kick it.mp3")
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
# ターゲットのスピー
target_speed = [random.randint(10, 200),random.randint(10, 200)]

# リスト
target_list = []

for _ in range(target_value):
    while True:
        target_x = random.randint(0, screen_width - target_width)
        target_y = random.randint(0, 700)
        target = pygame.Rect(target_x, target_y, target_width, target_height)
        if target.collidelist(target_list) == -1:
            target_list.append(target)
            break

# 객체 이동 속도
speed = 200 # 100 pixel / second


# 銃弾の定義
f_rect_width = 10
f_rect_height = 10
# 銃弾のリスト作成
f_rect_list = []

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_rect = pygame.Rect(0, 0, f_rect_width, f_rect_height)
                # 生成された四角形をプレイアーの四角形のTop中間に位置
                fire_rect.bottom = moving_rect.top
                fire_rect.x = moving_rect.centerx - f_rect_width // 2
                # 生成された銃弾をリストに追加
                f_rect_list.append(fire_rect)

    dt = clock.tick(60) / 1000  
    
    
    
    for target in target_list:
        pygame.draw.rect(screen, blue, target)
        target = target.move(target_speed)
        if target.left < 0 or target.right > screen_width:
            target_speed[0] = -target_speed[0]
        if target.top < 0 or target.bottom > screen_height:
            target_speed[1] = -target_speed[1]
   
        
    # 弾丸の処理
    for f_rect in f_rect_list[:]:
        f_rect.y -= speed * dt
        if f_rect.y < 0:  
            f_rect_list.remove(f_rect)
        
    # プレイヤーの動きを処理
    keys = pygame.key.get_pressed()
    
    # 왼쪽 방향키가 눌러졌을 때
    if keys[pygame.K_LEFT]:
        moving_rect.x -= speed * dt      

    # 오른쪽 방향키가 눌러졌을 때
    if keys[pygame.K_RIGHT]:
        moving_rect.x += speed * dt 
            
   
    # 충돌 감지
    # 모든 총알을 검사
    # f_rect_list[:]  -> リストをコピーすることでループ中にリストを変更してもエラーが発生しない
    for fire_rect in f_rect_list[:]:
        # 弾 (fire_rect) が敵の四角形と衝突したかどうかを追跡する。
        is_collision = False
        # 敵の四角形と現在の弾 (fire_rect) との衝突をチェック。
        for target in target_list[:]:
            # もし衝突発生したら
            if fire_rect.colliderect(target):
                #　リストから敵の四角形を削除
                target_list.remove(target)
                is_collision = True
        # 弾もリストから削除
        if is_collision:
            f_rect_list.remove(fire_rect)
    
    if moving_rect.collidelist(target_list) != -1:
        print("충돌 발생, 게임 종료")
        running = False
        
    # 떨어지는 사각형이 화면 아래에 위치하면 리스트에서 삭제
    for rect in target_list[:]:
        if rect.y > screen_height:
            target_list.remove(rect)
    
    # 화면 그리기
    screen.fill((255, 255, 255))
    
    # 떨어지는 사각형
    for rect in target_list:    
        pygame.draw.rect(screen, (0, 0, 255), rect)
        
    # 플레이어 사각형

    moving_rect.x = max(0,min(moving_rect.x, screen.get_width() - moving_rect_width))
    pygame.draw.rect(screen, (255, 0, 0), moving_rect)
    
    # 총알 그리기
    for f_rect in f_rect_list:
        pygame.draw.rect(screen, (0, 255, 0), f_rect) 
        
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
            
pygame.quit()
 
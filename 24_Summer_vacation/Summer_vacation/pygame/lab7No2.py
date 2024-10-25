
import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("haechan and mark")

# 写真をダウンロード
haechan_img = pygame.image.load("haechan.png")
mark_img = pygame.image.load("mark.png")

# ".get_rect" -> ImgをRect客体で管理するためのもの
haechan_rect = haechan_img.get_rect()
mark_rect = mark_img.get_rect()

# イメージの初期位置を設定
# haechanの位置を画面の左上から (100, 100) に設定する
haechan_rect.topleft = (100, 100)
# markの位置を画面の左上から (200, 200) に設定する
mark_rect.topleft = (200, 200)

# 速度
speed = 200
fps = 30
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    dt = clock.tick(fps) / 1000.0
    
    # 仮の移動位置を保存
    new_haechan_rect = haechan_rect.copy()
    new_mark_rect = mark_rect.copy()
  
    # キー入力処理
    keys = pygame.key.get_pressed()
    # haechan キー設定
    if keys[pygame.K_LEFT]:
        new_haechan_rect.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        new_haechan_rect.x += speed * dt
    if keys[pygame.K_UP]:
        new_haechan_rect.y -= speed * dt    
    if keys[pygame.K_DOWN]:
        new_haechan_rect.y += speed * dt
        
    # mark キー設定
    if keys[pygame.K_a]:
        new_mark_rect.x -= speed * dt
    if keys[pygame.K_d]:
        new_mark_rect.x += speed * dt
    if keys[pygame.K_w]:
        new_mark_rect.y -= speed * dt    
    if keys[pygame.K_x]:
        new_mark_rect.y += speed * dt    
            
    # 衝突判定と位置更新
    if not new_haechan_rect.colliderect(mark_rect) and \
       not new_mark_rect.colliderect(haechan_rect):
        haechan_rect = new_haechan_rect
        mark_rect = new_mark_rect
        
    # スクリーンに描写
    screen.fill((255,255,255))
    screen.blit(haechan_img, haechan_rect)
    screen.blit(mark_img, mark_rect)

    # スクリーンの外に出ないように設定
    haechan_rect.x = max(0, (min(haechan_rect.x , screen.get_width() - haechan_rect.width)))
    haechan_rect.y = max(0, (min(haechan_rect.y , screen.get_height() - haechan_rect.height)))
    mark_rect.x = max(0, (min(mark_rect.x , screen.get_width() - mark_rect.width)))     
    mark_rect.y = max(0, (min(mark_rect.y , screen.get_height() - mark_rect.height)))
    
    pygame.display.flip()
    
pygame.quit()
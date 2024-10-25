
import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("해찬과 마크의 술래 잡기")

#　色の定義
white = (255, 255, 255)

#　イメージロード
mark_image = pygame.image.load("mark.png")
haechan_image = pygame.image.load("haechan.png")

#　イメージの初期位置設定
# get_rect() -> 画像の位置とサイズを取得し、topleft属性で初期位置を設定する。
haechan_rect = haechan_image.get_rect()
haechan_rect.topleft = (100, 100)

mark_rect = mark_image.get_rect()
mark_rect.topleft = (200, 200)

# 移動速度
speed = 10
delta_speed = 0

clock = pygame.time.Clock()
fps = 30

#　ゲームループ

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    delta_speed = speed * (clock.tick(fps) / 1000.0)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mark_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        mark_rect.x += speed    
    if keys[pygame.K_UP]:
        mark_rect.y -= speed
    if keys[pygame.K_DOWN]:
        mark_rect.y += speed
    if keys[pygame.K_a]:
        haechan_rect.x -= speed
    if keys[pygame.K_d]:
        haechan_rect.x += speed
    if keys[pygame.K_w]:
        haechan_rect.y -= speed
    if keys[pygame.K_s]:
        haechan_rect.y += speed
    
    mark_rect.x = max(0, min(mark_rect.x, screen.get_width() - mark_rect.width))
    mark_rect.y = max(0, min(mark_rect.y, screen.get_height() - mark_rect.height))
    haechan_rect.x = max(0, min(haechan_rect.x, screen.get_width() - haechan_rect.width))
    haechan_rect.y = max(0, min(haechan_rect.y, screen.get_height() - haechan_rect.height))
    
    
    screen.fill(white)
    
    screen.blit(mark_image, mark_rect)
    screen.blit(haechan_image, haechan_rect)

    pygame.display.flip()    
            
pygame.quit()
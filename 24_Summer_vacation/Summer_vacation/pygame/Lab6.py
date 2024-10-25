import pygame
pygame.init()
import random

screen = pygame.display.set_mode((800, 600))

# x, y座標を変数に保存 
x = screen.get_width() // 2
y = screen.get_height() // 2

# 円の設定
radius = 50
# 色のリストを作成
          #　赤　　　　 #　黒　　　 #　黄色　　　　　#　緑　　　　#　青
color = [(255, 0, 0), (0, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]
# リストの中からランダムに色を選択
current_color = random.choice(color)

# 速度
speed = 300
clock = pygame.time.Clock()
fps = 30

running = True
while running:
    
    dt = clock.tick(fps) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #　マウスの左クリックを押すと色が変わる    
        elif event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 1: # 左クリック　# 右クリック -> 3
                new_color = random.choice(color)
                while new_color == current_color:  # 選ばれた色が現在の色 current_color と同じかをチェック　#　違えばwhile文終了
                    new_color = random.choice(color) #　現在の色と同じ場合は再選択
                current_color = new_color
            
    #　キーを押している間連続的に動きつづける        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
            x -= speed * dt
    if keys[pygame.K_RIGHT]:
            x += speed * dt    
    if keys[pygame.K_UP]:
            y -= speed * dt    
    if keys[pygame.K_DOWN]:
            y += speed * dt             
                             
    screen.fill((255, 255, 255))
    
    # 円を描く
    pygame.draw.circle(screen,current_color,(x,y),radius)
    
    # 境界線を超えないよう処理
    if x - radius < 0:
        x = radius
    if screen.get_width() < radius + x:
        x = screen.get_width() - radius 
    if y - radius < 0:
        y = radius
    if screen.get_height() - radius < y :
        y = screen.get_height() - radius
    
    
    pygame.display.flip()
    
pygame.quit()    

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
   
x = screen.get_width() // 2
y = screen.get_height() // 2

# 円の設定
radius = 40

# 円の移動速度：1秒に100ピクセル   
speed = 100
  
runnning = True
while runnning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
    # 各フレーム間の時間差でゲームの全ての時間ベースの計算に使用
    dt = clock.tick(30) / 1000.0  # FPSを30に固定、結果は秒単位

    # 画面を消す：全体の画面を黒に塗りつぶす
    screen.fill((0, 0, 0))
    
    # 円を描く：画面に赤い円を現在の x, y の位置に描く
    pygame.draw.circle(screen, ((255, 0, 0)), (x, y), radius)
    
    #　円の位置をアップデート：速度とデルタタイムを掛けて移動距離を計算
    x += speed * dt
    
    #　境界処理
    if x - radius < 0 or x + radius > screen.get_width():
        speed = -speed
    
    pygame.display.flip()
    
pygame.quit()
    
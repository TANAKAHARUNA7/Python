import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Rectangle Collision Example")

black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0 ,0)

# 四角形初期化（x，y、width, height）
rect1 = pygame.Rect(300, 220, 60, 60)
rect2 = pygame.Rect(100, 100, 60, 60)
rect1_speed = [10, 10]
rect2_speed = [5, 5]

# FPS設定
fps = 30
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    clock.tick(fps)#設定されたFPSによってループ進行
    
    rect1 = rect1.move(rect1_speed) # 設定速度の分だけ移動
    rect2 = rect2.move(rect2_speed)

    if rect1.left < 0 or rect1.right > 640:
        rect1_speed[0] = -rect1_speed[0]
    if rect1.top < 0 or rect1.bottom > 480:
        rect1_speed[1] = -rect1_speed[1]
        
    if rect2.left < 0 or rect2.right > 640:
        rect2_speed[0] = -rect2_speed[0]
    if rect2.top < 0 or rect2.bottom > 480:
        rect2_speed[1] = -rect2_speed[1]

    # 衝突感知
    if rect1.colliderect(rect2):#rect1とRect2が衝突したら
        print("Collision Detected!")#メッセージを出力
        
    screen.fill(black)
    pygame.draw.rect(screen, blue, rect1)#Rect1を青で描く
    pygame.draw.rect(screen, red, rect2)#Rect2を赤で描く
    pygame.display.flip()

pygame.quit()






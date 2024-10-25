
import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))

# タイトル
pygame.display.set_caption("四角形衝突例")

#　x、y座標を変数に保存
x = screen.get_width()
y = screen.get_height()

#　四角形の定義
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(200, 200, 100, 100)
# rect1,2の速度　[x,y方向]
rect1_speed = [10, 5]
rect2_speed = [5, 10]

# 色の定義
Red = (255, 0, 0)
blue = (0, 0, 255)

# fps設定
clock = pygame.time.Clock()
fps = 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    clock.tick(fps)
    
    # 四角形の動き
    rect1 = rect1.move(rect1_speed)
    rect2 = rect2.move(rect2_speed)
    
    #　画面境界の衝突処理（rect1）
    if rect1.left < 0 or rect1.right > x:
        rect1_speed[0] = -rect1_speed[0]
    if rect1.top < 0 or rect1.bottom > y:
        rect1_speed[1] = -rect1_speed[1]
    #　画面境界の衝突処理（rect2）
    if rect2.left < 0 or rect2.right > x:
        rect2_speed[0] = -rect2_speed[0]
    if rect2.top < 0 or rect2.bottom > y:
        rect2_speed[1] = -rect2_speed[1]
    
    #　二つの四角形が衝突した際にコメントを出力    
    if rect1.colliderect(rect2):
        print("衝突発生")
        
    # 絵を描く       
    screen.fill((255,255,255))
    pygame.draw.rect(screen, Red,rect1)
    pygame.draw.rect(screen, blue, rect2)
       
    pygame.display.flip()
              
pygame.quit()
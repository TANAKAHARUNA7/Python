import pygame
pygame.init()

# 画面設定
screen = pygame.display.set_mode((800, 600))
# タイトルを設定
pygame.display.set_caption("Rectangular Drawing")

# 色の定義
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# 四角形の定義 
# オブジェクトを使用し四角形の情報を保存   
rect1 = pygame.Rect(100, 100, 100, 50) # x,y 大きさ

# 画面を白に
screen.fill(white)
pygame.draw.rect(screen,red,rect1,width=2)
pygame.draw.rect(screen, blue, (400, 300, 100, 50), width= 2)   

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
    
pygame.quit()

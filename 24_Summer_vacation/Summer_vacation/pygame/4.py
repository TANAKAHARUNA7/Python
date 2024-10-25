
## -----> 初期化
import pygame
pygame.init()
##　←－－－‐‐‐

screen = pygame.display.set_mode((640,480))

running = True

#　while文が1回回るたびに画像が生成され、その作業が続くことで動く絵が作られる
#　white内にあるアルゴリズムが絵を描く順序となり、
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # イベントが発生するとき
        screen.fill((255,255,255))
        pygame.display.flip()
            
    # イベント処理が終わった後    
    screen.fill((255,255,255))
    pygame.display.flip()
            
pygame.quit()
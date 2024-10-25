import pygame
import random
pygame.init()

# ←－－－－スクリーンの大きさ設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# ---------------->

# ←－－－－色を定義
Yellow = (0, 255, 255)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
# ---------------->

# ＜‐‐‐‐‐‐‐‐物体の設定
#障害物の大きさ(横,縦)
rect_width = 70
rect_height = 70
# 障害物の個数
rect_value = 8

#アイテムの大きさ
item_width = 20
item_height = 20
# itemの個数
item_value = 20

#動く四角形
move_rect_width = 30
move_rect_height = 30
#　－－－－－－－＞

# 速さ
speed = 3
clock = pygame.time.Clock()
fps = 60

#＜‐‐‐‐‐‐‐‐障害物を生成 
rect_list = []
for _ in range(rect_value):
    while True:
    # x座標をランダムに生成
        rect_x = random.randint(0,screen_width - rect_width)
        # y座標をランダムに生成
        rect_y = random.randint(0,screen_height - rect_height)
        rect = pygame.Rect(rect_x,rect_y,rect_width,rect_height)
        
        #　障害物同士が衝突しないように設定
        if rect.collidelist(rect_list) == -1:
            rect_list.append(rect)
            break   
# ---------------->


# ＜‐‐‐‐‐‐‐‐アイテムを生成 
item_list = []
for _ in range(item_value):
    while True:
    # x座標をランダムに生成
        item_x = random.randint(0,screen_width - item_width)
        # y座標をランダムに生成
        item_y = random.randint(0,screen_height - item_height)
        item = pygame.Rect(item_x,item_y,item_width,item_height)
        
        #　障害物とアイテムが衝突しないように設定
        if item.collidelist(rect_list) == -1 and item.collidelist(item_list) == -1:
            item_list.append(item)
            break


# ＜‐‐‐‐‐‐‐‐　動く四角形を生成
while True:
    move_rect_x = random.randint(0,screen_width - move_rect_width)
            # y座標をランダムに生成
    move_rect_y = random.randint(0,screen_height - move_rect_height)
    move_rect = pygame.Rect(move_rect_x,move_rect_y,move_rect_width,move_rect_height)
            
        #　障害物と衝突しないように設定
    if move_rect.collidelist(rect_list) == -1 and move_rect.collidelist(item_list) == -1:
        break
# ---------------->

# ＜‐‐‐‐‐‐‐‐　ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    dt = clock.tick(fps) / 1000 
    
    # キーボードを入力する前に四角形の座標を保存
    # 座標は動くたびに変わりアップグレードする
    previous_pos = move_rect.topleft
    
    # 動く四角形のキー設定        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_rect.x -= speed 
    if keys[pygame.K_RIGHT]:
        move_rect.x += speed 
    if keys[pygame.K_UP]:
        move_rect.y -= speed 
    if keys[pygame.K_DOWN]:
        move_rect.y += speed 
        
    #　動く四角形が画面の外に出ないように設定
    #                      現在のmove_rectがいる位置, move_rectの横幅 - move_rectの縦幅
    move_rect.x = max(0,min(move_rect.x , (screen_width -  move_rect_width)))
    move_rect.y = max(0,min(move_rect.y , (screen_height -  move_rect_height)))
    
    # 動く四角形が障害物とぶつからないように設定
    if move_rect.collidelist(rect_list) != -1:
        move_rect.topleft = previous_pos
            
    screen.fill((0,0,0))
    
    for rect in rect_list:
        pygame.draw.rect(screen,Blue,rect)
    
    for item in item_list:
        pygame.draw.rect(screen,Yellow,item)
    
    # 衝突したアイテムの順序を保存する変数
    col_index = move_rect.collidelist(item_list)
    #　衝突しなかったとき -1 , 衝突したときindex　
    if col_index != -1:
        del item_list[col_index]
    if len(item_list) == 0:
        running = False
    pygame.draw.rect(screen,Red,move_rect)   
    
    pygame.display.flip()
    
pygame.quit()    
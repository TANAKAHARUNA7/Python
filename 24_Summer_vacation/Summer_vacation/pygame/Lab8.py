 
import pygame
pygame.init()
import random

# 画面設定
screen_x = 800
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))

# 障害物Rect
rect_width = 60
rect_height = 60
rect_value = 7
ob_rect_list = []
blue = (0, 0, 255)
# 複数生成
for ob_rect in range(rect_value):
    while True:
        rect_x = random.randint(0, screen_x - rect_width)
        rect_y = random.randint(0, screen_y - rect_height)
        obstacles_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        #　障害物同士がぶつからないように
        if obstacles_rect.collidelist(ob_rect_list) == -1:
            ob_rect_list.append(obstacles_rect)
            break

# item
item_width = 10
item_height = 10
item_value = 20
item_list = []
sky_blue = (0, 255, 255)
item = pygame.Rect(300, 300, item_width, item_height)
# item 複数生成
for item in range(item_value):
    while True:
        item_x = random.randint(0, screen_x - item_width)
        item_y = random.randint(0, screen_y - item_height)
        item = pygame.Rect(item_x, item_y, item_width, item_height)
        # アイテム同士または障害物がぶつからないように
        if item.collidelist(item_list) == -1 and item.collidelist(ob_rect_list) == -1:
            item_list.append(item)
            break
  
    
# 動く四角形
mv_rect_width = 60
mv_rect_height = 60
red = (255, 255, 0)
speed = 300
# 位置をランダムに配置
while True:
    mv_rect_x = random.randint(0, screen_x - mv_rect_width)
    mv_rect_y = random.randint(0, screen_y - mv_rect_height)
    mv_rect = pygame.Rect(mv_rect_x, mv_rect_y, mv_rect_width, mv_rect_height)
    if mv_rect.collidelist(item_list) == -1 and mv_rect.collidelist(ob_rect_list) == -1:
        break


#　fps設定
clock = pygame.time.Clock()
fps = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(fps) / 1000.0
    
    position = mv_rect.topleft
         
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_LEFT]:
        mv_rect.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        mv_rect.x += speed * dt    
    if keys[pygame.K_UP]:
        mv_rect.y -= speed * dt    
    if keys[pygame.K_DOWN]:
        mv_rect.y += speed * dt    
    
    # 衝突感知　動く四角形が障害物を超えないように    
    collision_mv = mv_rect.collidelist(ob_rect_list)
    if collision_mv != -1:
        mv_rect.topleft = position
    
    # item収集
    collision_item = mv_rect.collidelist(item_list)
    if collision_item != -1:
        del item_list[collision_item]
    if len(item_list) == 0:
        running = False 
    
    # 境界線を設定
    mv_rect.x = max(0, min(mv_rect.x , screen_x - mv_rect_width))
    mv_rect.y = max(0, min(mv_rect.y , screen_y - mv_rect_height))
        
    #　絵を描写
    screen.fill((255,255,255))
    # 障害物
    for ob_rect in ob_rect_list:
        pygame.draw.rect(screen, blue, ob_rect)
    #　アイテム
    for item in item_list:
        pygame.draw.rect(screen, sky_blue, item)
    #　動く四角形
    pygame.draw.rect(screen, red, mv_rect)
    
    pygame.display.flip()
    
            
pygame.quit()
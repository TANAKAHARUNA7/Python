
# import pygame
# pygame.init()

# screen = pygame.display.set_mode((640,480))
# pygame.display.set_caption("Rectangle Collision Example")

# # 3つのRectのオブジェクトを生成
# # (x, y, width, height)
# rects = [
#     pygame.Rect(20, 20, 40, 40),     # 1つ目　Rect：（20,20）位置,　40ｘ40大きさ
#     pygame.Rect(100, 100, 50, 50),   # 2つ目　Rect：（100,100）位置,　50ｘ50大きさ
#     pygame.Rect(200, 200, 60, 60)]   # 3つ目　Rect：（200,200）位置,　60ｘ60大きさ

# # 衝突感知を実行する対象Rectオブジェクト生成:　青の四角形
# moving_rect = pygame.Rect(120, 130, 100, 100)  # （120,130）位置,　100ｘ100大きさ

# # moving_rectがrectsリストのどんなRectと衝突するのか確認
# # collidelist メソッドは衝突したRectのインデックスを返還。衝突がなければｰ1を返還する
# index = moving_rect.collidelist(rects)

# #　色の定義
# black = (0, 0, 0)
# blue = (0, 0, 255)
# red = (255, 0, 0)

# rects_speed = [10, 10]
# rects[0].x += rects_speed[0]
# rects[0].y += rects_speed[1]


# fps = 30
# clock =pygame.time.Clock()

# #　ゲームループ

# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     clock.tick(fps)

#     rects = rects.move(rects_speed)
    
#     if rects[0].left < 0 or rects[0].right > 640:
#         rects_speed[0] = -rects_speed[0]
#     if rects[0].top < 0 or rects[0].bottom > 480:
#         rects_speed[1] = -rects_speed[1] 
    
    
#     index = moving_rect.collidelist(rects)
#     if index != -1:
#         print(f"moving_rectがrects[{index}]と衝突しました")
#     else:
#         print("衝突がありません")
        
#     screen.fill(black)
#     pygame.draw.rect(screen, blue, moving_rect)
#     pygame.draw.rect(screen, blue, rects[0])
#     pygame.draw.rect(screen, red, rects[1])
#     pygame.draw.rect(screen, red, rects[2])
#     pygame.display.flip()        
            
# pygame.quit()


##################################################

import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Rectangle Collision Example")

# 3つのRectのオブジェクトを生成
rects = [
    pygame.Rect(20, 20, 40, 40),     # 1つ目のRect
    pygame.Rect(100, 100, 50, 50),   # 2つ目のRect
    pygame.Rect(200, 200, 60, 60)    # 3つ目のRect
]

# 衝突感知を実行する対象Rectオブジェクト生成: 青の四角形
moving_rect = pygame.Rect(120, 130, 100, 100)  # （120,130）位置, 100ｘ100大きさ

# 色の定義
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

rects_speed = [10, 10]

fps = 30
clock = pygame.time.Clock()

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rectの移動
    rects[0].x += rects_speed[0]
    rects[0].y += rects_speed[1]

    # 境界衝突の処理
    if rects[0].left < 0 or rects[0].right > 640:
        rects_speed[0] = -rects_speed[0]
    if rects[0].top < 0 or rects[0].bottom > 480:
        rects_speed[1] = -rects_speed[1]

    # 衝突感知
    index = moving_rect.collidelist(rects)
    if index != -1:
        print(f"moving_rectがrects[{index}]と衝突しました")
    else:
        print("衝突がありません")

    # 描画
    screen.fill(black)
    pygame.draw.rect(screen, blue, moving_rect)
    pygame.draw.rect(screen, red, rects[0])
    pygame.draw.rect(screen, red, rects[1])
    pygame.draw.rect(screen, green, rects[2])
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()


# rect.x += speed * dt  # speed * 1/fps
# rect1.x += speed  # 
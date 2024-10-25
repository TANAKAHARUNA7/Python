import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Rectangle Collision Example")

# 複数のRectのオブジェクトを生成
rects = [
    pygame.Rect(350, 150, 100, 100),     # 1つ目のRect
    pygame.Rect(300, 300, 150, 50),   # 2つ目のRect
    pygame.Rect(500, 200, 50, 150),
    pygame.Rect(400, 400, 200, 50)# 3つ目のRect
]

# 衝突感知を実行する対象Rectオブジェクト生成: 青の四角形
moving_rect = pygame.Rect(420, 220, 100, 100)  # （120,130）位置, 100ｘ100大きさ

collision_indices = moving_rect.collidelistall(rects)


# 色の定義
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

rects_speed = [10, 7, 5, 3]

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
    rects[0].y += rects_speed[0]
    rects[1].x += rects_speed[1]
    rects[1].y += rects_speed[1]
    rects[2].x += rects_speed[2]
    rects[2].y += rects_speed[2]
    rects[3].x += rects_speed[3]
    rects[3].y += rects_speed[3]

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
    pygame.draw.rect(screen, red, rects[2])
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
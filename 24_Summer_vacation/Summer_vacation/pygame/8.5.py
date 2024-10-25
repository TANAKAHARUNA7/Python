import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

# 폰트 설정 (크기 36)
font = pygame.font.Font(None, 36)
count = 0

# whileが回るたびに1枚の絵が作成される
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    # 텍스트 생성 및 화면 출력                          # True -> アンチエイリアス（テキストのギザギザを滑らかにする処理）の有無を示す。
                                                        # True に設定すると、アンチエイリアスが有効になる。
    count_text = font.render(f"count: {count/ 60:.2f}", True,(0,0,0)) # フォントの色
    screen.blit(count_text, (10, 10))
    count += 1
    
                             # 色　　　　# 位置     # 大きさ
    pygame.draw.rect(screen, (255,0,0),(200, 120, 100, 100))
    
         
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    # 1秒間にwhile文を60回回す　※ 数値が高いほど絵が滑らかに動くが数値が高いほど負担がかかる
    # 1/60 시간 만큼 프로그램을 stop
    clock.tick(60)  # clok.tick(fps number) -> 1sec / fps number -> delta time

pygame.quit()

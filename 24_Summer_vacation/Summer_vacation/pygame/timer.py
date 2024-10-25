
import pygame
pygame.init()

# 画面設定
screen = pygame.display.set_mode((640,480))
x = screen.get_width()
y = screen.get_height()
pygame.display.set_caption("Timer Diolay Example")

# 色定義
white = (255, 255, 255)
black = (0, 0, 0)

# フォント設定
# font -> オブジェクトpygame.font.Font(None, フォントサイズ)
font = pygame.font.Font(None, 36) # Noneは基本のシステムフォントを意味
font = pygame.font.SysFont('bizudpminchomediumtruetype', 36) # 他のフォントを使用したい場合

available_fonts = pygame.font.get_fonts()
print(available_fonts)


#　timer開始時間
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 経過時間を計算
    # pygame.time.get_ticks()を呼び出して、現在の時間を取得する。そこからstart_timeを引くことで、プログラムの開始から
    # 何ミリ秒経過したかを計算する。/ 1000を行うことで、ミリ秒から秒に変換している。
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 # 秒単位で返還  
    
    #　絵を描写
    screen.fill((255,255,255))      
    # timerテキスト生成
    # font.render() -> 経過時間を表示するためのテキストを生成。
    # f"Time: {elapsed_time:.2f} seconds" -> 経過時間を小数点以下2桁まで表示するフォーマット。
    # True -> アンチエイリアス（文字を滑らかに描画する処理）を有効にするためのオプション。
    # black -> テキストの色
    timer_text = font.render(f"Time: {elapsed_time:.2f} seconds", True, black)
    #　timerテキストを画面に出力
    screen.blit(timer_text, (10, 10))        

    pygame.display.flip()
    
            
pygame.quit()
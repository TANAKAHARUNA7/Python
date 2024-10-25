import pygame

# ゲーム初期化
pygame.init()
#　画面スクリーンサイズ設定
screen = pygame.display.set_mode((1200,700))

#　スクリーンサイズを変数に保存
x = screen.get_width() 
y = screen.get_height()

#　座標【中心点】を決定
x_first = 0
y_first = 0

#　背景と円の色を設定
back_color = (255, 200, 240)
pink = (255, 90, 200)

# 円の半径
radius = 50

# 
speed_x = 1
speed_y = 0.5


#　反復文を使用しゲーム終了するまで画面を出力するためのコード
running = True

while running:
    for event in pygame.event.get():
        #　使用者が×を押すと終了
        if event.type == pygame.QUIT:
            running = False
    
    #　背景色
    screen.fill(back_color)
    #　円を描く
    pygame.draw.circle(screen,pink,(x_first,y_first),radius)
    
    # # 円を縦に動かす
    # if y_center + radius >= screen.get_height() or y_center - radius <= 0:
    #     speed = - speed
        
    # y_center += speed   
    
    
    # 対角線に円を動かす
    x_first += speed_x
    y_first += speed_y  
            
   
               
    pygame.display.flip()        
            
pygame.quit()
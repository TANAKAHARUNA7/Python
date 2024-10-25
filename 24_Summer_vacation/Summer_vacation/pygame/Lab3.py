import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # キーを押したときに発生するevent
        elif event.type == pygame.KEYDOWN:
                                     # 押したキーの名前を出力
            print((f"押したキー: {pygame.key.name(event.key)}"))
        #　マウスボタンをクリックしたら発生するイベント    
        elif event.type == pygame.MOUSEBUTTONDOWN:
                                    # クリックされた位置             # ボタン番号を出力
                print(f"マウスボタン {event.button} クリックポジション {event.pos} ")
            
    
pygame.quit()
                
    
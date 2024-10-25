import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 게임 변수
screen_x = screen.get_width()
screen_y = screen.get_height()
fall_rect_width = 80
fall_rect_height = 40
moving_rect_width = 50



# 떨어지는 사각형
rect_list = []
def generate_fall_rects():
    for _ in range(random.randint(3,8)):
        while True:
            rect_x = random.randint(0,(screen.get_width() - fall_rect_width))
            rect = pygame.Rect(rect_x, 0, fall_rect_width, fall_rect_height)
            
            # 충돌이 발생하지 않았을 경우
            if rect.collidelist(rect_list) == -1:
                # 사각형을 list에 추가
                rect_list.append(rect)
                break
            
        
# 객체 이동 속도
speed = 100 # 300 pixel / second

# 
MY_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(MY_EVENT, 2000) # 2000ms -> 2秒

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MY_EVENT:
            generate_fall_rects()    


    dt = clock.tick(60) / 1000  

    # 떨어지는 사각형의 y값 증가
    for rect in rect_list:
        rect.y += speed * dt
        
    # 화면 아래이면 리스트에 삭제
    for rect in rect_list[:]:
        if rect.y > screen_y:
            rect_list.remove(rect)
    
    # 화면 그리기
    screen.fill((255, 255, 255))
    
    for rect in rect_list:        
        pygame.draw.rect(screen, (0, 0, 255), rect) 
    
    # 플레이어 사각형
    pygame.draw.rect(screen, (0, 0, 255), rect)
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
pygame.quit()


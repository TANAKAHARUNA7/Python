import pygame

pygame.init()

# 화면 설정
screen = pygame.display.set_mode((640, 480))  # 640x480 크기의 창을 생성
pygame.display.set_caption("Rectangle Collision Example")  # 창의 제목 설정

# 색상 정의
black = (0, 0 ,0)  # 검정색
blue = (0, 0 , 255)  # 파란색
red = (255, 0, 0)  # 빨간색
white = (255, 255, 255)  # 흰색
yellow = (255, 255, 0)  # 노란색
green = (0, 255, 0)  # 초록색

# 여러 개의 Rect 객체를 생성
# (x, y, width, height)
obstacles = [
    pygame.Rect(350, 150, 100, 100),  # 첫 번째 장애물: (350, 150) 위치, 100x100 크기
    pygame.Rect(300, 300, 150, 50),  # 두 번째 장애물: (300, 300) 위치, 150x50 크기
    pygame.Rect(500, 200, 50, 150),  # 세 번째 장애물: (500, 200) 위치, 50x150 크기
    pygame.Rect(400, 400, 200, 50)  # 네 번째 장애물: (400, 400) 위치, 200x50 크기
]
obstacles1_speed = [10, 10]  # obstacles1의 속도 (x 방향, y 방향)
obstacles2_speed = [7, 7]  # obstacles2의 속도 (x 방향, y 방향)
obstacles3_speed = [5, 5]  # obstacles3의 속도 (x 방향, y 방향)
obstacles4_speed = [3, 3]  # obstacles4의 속도 (x 방향, y 방향)

# FPS 설정
fps = 30
clock = pygame.time.Clock()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    clock.tick(fps)
    
    # 사각형 움직임
    obstacles[0] = obstacles[0].move(obstacles1_speed)  # obstacles1을 속도만큼 이동
    obstacles[1] = obstacles[1].move(obstacles2_speed)  # obstacles2을 속도만큼 이동
    obstacles[2] = obstacles[2].move(obstacles3_speed)  # obstacles3을 속도만큼 이동
    obstacles[3] = obstacles[3].move(obstacles4_speed)  # obstacles4을 속도만큼 이동
    
    # 화면 경계에 충돌 처리 (obstacles1)
    if obstacles[0].left < 0 or obstacles[0].right > 640:  # 화면 좌우 경계에 충돌하면
        obstacles1_speed[0] = -obstacles1_speed[0]  # x 방향 속도 반전
    if obstacles[0].top < 0 or obstacles[0].bottom > 480:  # 화면 상하 경계에 충돌하면
        obstacles1_speed[1] = -obstacles1_speed[1]  # y 방향 속도 반전
        
    # 화면 경계에 충돌 처리 (obstacles2)
    if obstacles[1].left < 0 or obstacles[1].right > 640:  # 화면 좌우 경계에 충돌하면
        obstacles2_speed[0] = -obstacles2_speed[0]  # x 방향 속도 반전
    if obstacles[1].top < 0 or obstacles[1].bottom > 480:  # 화면 상하 경계에 충돌하면
        obstacles2_speed[1] = -obstacles2_speed[1]  # y 방향 속도 반전
        
    # 화면 경계에 충돌 처리 (obstacles3)
    if obstacles[2].left < 0 or obstacles[2].right > 640:  # 화면 좌우 경계에 충돌하면
        obstacles3_speed[0] = -obstacles3_speed[0]  # x 방향 속도 반전
    if obstacles[2].top < 0 or obstacles[2].bottom > 480:  # 화면 상하 경계에 충돌하면
        obstacles3_speed[1] = -obstacles3_speed[1]  # y 방향 속도 반전
        
    # 화면 경계에 충돌 처리 (obstacles4)
    if obstacles[3].left < 0 or obstacles[3].right > 640:  # 화면 좌우 경계에 충돌하면
        obstacles4_speed[0] = -obstacles4_speed[0]  # x 방향 속도 반전
    if obstacles[3].top < 0 or obstacles[3].bottom > 480:  # 화면 상하 경계에 충돌하면
        obstacles4_speed[1] = -obstacles4_speed[1]  # y 방향 속도 반전

    # 충돌 감지를 수행할 대상 Rect 객체 생성: 파란색 사각형
    moving_rect = pygame.Rect(420, 220, 100, 100)  # (120, 130) 위치, 100x100 크기

    # moving_rect가 obstacles 리스트의 어떤 Rect와 충돌하는지 확인
    # collidelist 메서드는 충돌한 Rect의 인덱스를 반환. 충돌이 없으면 -1을 반환한다.
    index = moving_rect.collidelist(obstacles)

    if index != -1:
        # 충돌이 발생한 경우, 충돌한 Rect의 인덱스를 출력
        print(f"moving_rect가 obstacles[{index}]와 충돌했습니다.")
    else:
        # 충돌이 발생하지 않은 경우, 해당 메시지를 출력
        print("충돌이 없습니다.")
        
    # 화면 그리기
    screen.fill(white)  # 화면을 검정색으로 채움
    pygame.draw.rect(screen, black, obstacles[0])  # rect1을 검정색으로 그리기
    pygame.draw.rect(screen, red, obstacles[1])  # rect2을 파란색으로 그리기
    pygame.draw.rect(screen, yellow, obstacles[2])  # rect2을 파란색으로 그리기
    pygame.draw.rect(screen, blue, moving_rect)
    pygame.display.flip()  # 화면 업데이트
    
pygame.quit()  # Pygame 종료
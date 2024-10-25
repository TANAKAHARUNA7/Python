import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))

screen_x = screen.get_width()
screen_y = screen.get_height()

# 色
red = (255, 0, 0)

screen.fill((255,255,255))
pygame.draw.line(screen,red,(0, 0), (screen_x - 1, screen_y - 1))
pygame.draw.line(screen,red, (screen_x - 1, 0), (0, screen_y - 1))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
pygame.quit()
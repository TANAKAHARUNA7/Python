import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("NCT DREAM")

back_color = (255, 255, 255)
screen.fill(back_color)

pygame.display.flip

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Event Listener and Handler Example")
running = True


while running:
    for event in pygame.event.get():
        print(event)
        
pygame.quit()
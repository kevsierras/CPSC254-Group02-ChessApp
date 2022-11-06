import pygame

pygame.init()
width, height = 800, 600
backgroundColor = 255, 0, 0

screen = pygame.display.set_mode((width, height))


while True:
    pygame.event.get()
    screen.fill(backgroundColor)
    pygame.display.flip()

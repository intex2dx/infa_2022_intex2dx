import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400),)
screen.set_colorkey((100,100,100))
screen.fill((255,255,255))
color = (255,255,0)
circle(screen, color,  (200,200), 100)
circle(screen, (0,0,0), (200, 200), 100, 1)
polygon(screen, (0,0,0), [(200-28, 200-29.25), (200-60, 200-56.24), (200-51, 200-68.25),(200-17.56, 200-43.17)])
polygon(screen, (0,0,0), [(200+28, 200-29.25), (200+60, 200-56.24), (200+51, 200-68.25),(200+17.56, 200-43.17)])
rect(screen, (0,0,0), (155, 250, 90, 20))
circle(screen, (255, 0,0), (155, 180), 20)
circle(screen, (0,0,0), (155, 180), 20, 1)
circle(screen, (0, 0,0), (155, 180), 10)
circle(screen, (255,0,0), (245, 180), 20)
circle(screen, (0,0,0), (245, 180), 20, 1)
circle(screen, (0,0,0), (245, 180), 10)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
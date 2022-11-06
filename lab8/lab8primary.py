import pygame
from pygame.draw import *
from random import randint

pygame.init()


class NewBall():
    '''класс нового созданного шарика'''

    def __init__(self):
        '''рисует новый шарик'''
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]
        circle(screen, self.color, (self.x, self.y), self.r)


def check(x, y, ball_obj):
    '''проверяет принадлежность точки с координатами (x, y) шарику ball_obj'''
    x0, y0, r0 = ball_obj.x, ball_obj.y, ball_obj.r
    return (x-x0)**2 + (y-y0)**2 <= r0**2

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


pygame.display.update()
clock = pygame.time.Clock()
finished = False
cnt = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for i in range(n_balls):
                cnt += check(mouse_x, mouse_y, balls[i])


    n_balls = randint(1, 4)
    balls = [NewBall() for i in range(n_balls)]
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
print(f'ЧИСЛО ОЧКОВ: {cnt}')
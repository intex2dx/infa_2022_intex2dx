import pygame
from pygame.draw import *
from random import randint

pygame.init()


class NewBall():
    '''класс нового созданного шарика'''

    def __init__(self):
        '''рисует новый шарик'''
        self.x = randint(100, 700)
        self.y = randint(100, 700)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]
        self.speed = [randint(-10, 10), randint(-10, 10)]
        circle(screen, self.color, (self.x, self.y), self.r)
        self.t_alive = randint(100, 1000)
        self.t_current = 0

    def check(self, x, y):
        '''проверяет принадлежность точки с координатами (x, y) шарику ball_obj'''
        x0, y0, r0 = self.x, self.y, self.r
        return (x - x0) ** 2 + (y - y0) ** 2 <= r0 ** 2

    def move(self):
        '''перемещает шарик по полю и отражает его от стенок если это необходимо'''
        self.in_field()
        self.x += self.speed[0]
        self.y += self.speed[1]

    def in_field(self):
        '''проверяет, что шарик не касается стенок. В противном случае меняет его скорость так, чтобы
                он случайным образом отразился от стенки.'''
        x = self.x + self.speed[0]
        y = self.y + self.speed[1]
        r = self.r
        condition1 = (x + r) <= 800
        condition2 = (x - r) >= 0
        condition3 = (y + r) <= 800
        condition4 = (y - r) >= 0
        if not condition1 or not condition2:
            self.speed[0] = -self.speed[0] * randint(1, 40) / 10 if abs(self.speed[0]) < 100 else 10
        if not condition3 or not condition4:
            self.speed[1] = -self.speed[1] * randint(1, 40) / 10 if abs(self.speed[1]) < 100 else 10


def record(player_name, cnt):
    f = open("player_list.txt", "r", encoding="UTF-8")
    list_of_best_players = f.readlines()
    f.close()
    new_list_of_best_players = change(player_name, cnt, list_of_best_players)
    f = open("player_list.txt", "w", encoding="UTF-8")
    print("\n".join(new_list_of_best_players), file=f)
    f.close()


def change(player_name, cnt, list_of_best_players):
    results = {player_line.split()[0]: int(player_line.split()[1]) for player_line in list_of_best_players}
    players_names = list(results.keys())
    players_names.append(player_name)
    results[player_name] = cnt
    players_names.sort(key=lambda x: -results[x])
    new_list_of_best_players = [f"{name} {results[name]}" for name in players_names[:5]]
    return new_list_of_best_players


FPS = 60
screen = pygame.display.set_mode((800, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

pygame.display.update()
clock = pygame.time.Clock()
finished = False
print("Введите своё имя")
player_name = input()
n_balls = randint(1, 10)
balls = [NewBall() for i in range(n_balls)]
cnt = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for i in range(n_balls):
                cnt += balls[i].check(mouse_x, mouse_y)
    screen.fill(WHITE)
    for i in range(n_balls):
        if balls[i].t_current < balls[i].t_alive:
            balls[i].move()
        else:
            balls[i] = NewBall()
        circle(screen, balls[i].color, (balls[i].x, balls[i].y), balls[i].r)
        balls[i].t_current += 1
    pygame.display.update()
pygame.quit()
record(player_name, cnt)
print(f"ЧИСЛО ОЧКОВ: {cnt}")

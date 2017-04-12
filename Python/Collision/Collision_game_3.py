import pygame
from pygame.locals import *

def axis_overlap(p1, length1, p2, length2):
    collided = False
    if p1 < p2:
        if p2+length2-p1 < length1+length2:
            collided = True
    elif p1 > p2:
        if p1+length1-p2 < length1+length2:
            collided = True
    elif p1 == p2:
        collided = True
    return collided

pygame.init()
width, height = (50,50)
SCREEN_SIZE = (600, 400)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
x,y = (500,200)
x2,y2,width2,height2 = (150,150,150,100)
background = pygame.surface.Surface(SCREEN_SIZE).convert()
background.fill((0,0,0))
direction = 'LEFT'

while True:
    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if key_pressed[K_UP]:
        y -= 3
        direction = 'UP'
    elif key_pressed[K_DOWN]:
        y += 3
        direction = 'DOWN'
    elif key_pressed[K_LEFT]:
        x -= 3
        direction = 'LEFT'
    elif key_pressed[K_RIGHT]:
        x += 3
        direction = 'RIGHT'

    xycollide = False
    xcollide = axis_overlap(x,width,x2,width2)
    ycollide = axis_overlap(y,height,y2,height2)
    xycollide = xcollide & ycollide
    if xycollide:
        if direction is 'UP':
            y = y2+height2
        elif direction is 'DOWN':
            y = y2-height
        elif direction is 'LEFT':
            x = x2+width2
        elif direction is 'RIGHT':
            x = x2-width

    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (255,0,0),[x2,y2,width2,height2])
    pygame.draw.rect(screen, (255,255,0),[x,y,width,height])
    pygame.display.update()

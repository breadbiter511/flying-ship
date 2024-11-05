import pygame
from pygame.locals import *
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
objectrocket = pygame.image.load("rocket in space\spaceship.png")
bg = pygame.image.load("rocket in space\spacebg.png")
rocketx = 300
rockety = 300

keys = [False,False,False,False]



run = True
while run:
    screen.blit(bg,(0,0))
    screen.blit(objectrocket,(rocketx,rockety))
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.KEYDOWN:
            if i.key == K_UP:
                keys[0] = True
            elif i.key == K_LEFT:
                keys[1] = True
            elif i.key == K_RIGHT:
                keys[2] = True
            elif i.key == K_DOWN:
                keys[3] = True
        if i.type == pygame.KEYUP:
            if i.key == K_UP:
                keys[0] = False
            elif i.key == K_LEFT:
                keys[1] = False
            elif i.key == K_RIGHT:
                keys[2] = False
            elif i.key == K_DOWN:
                keys[3] = False
    if keys [0]:
        rockety -= 0.1
    elif keys [1]:
        rocketx -= 0.1
    elif keys [2]:
        rocketx += 0.1
    elif keys [3]:
        rockety += 0.1
    rockety += 0.05
        



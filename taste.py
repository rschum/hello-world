#! /C/Python27/python

import sys, pygame
pygame.init()

size = width, height = 800, 400
vector = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(vector)
    if ballrect.left < 0 or ballrect.right > width:
        vector[0] = -vector[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        vector[1] = -vector[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

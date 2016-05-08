import pygame
import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *
screen_width = 1280
screen_height = 720

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))

BLACK = (0,0,0)

ballImg = pygame.image.load("ball.png")
ballPosition = [0,0]
speed = 10

clock = pygame.time.Clock()

def game_loop():
    while 1:
    	clock.tick(60)
        for event in pygame.event.get():
           if event.type == KEYDOWN:
				if event.key == K_q:
					exit()

        #get all the keys being pressed
        keys = pygame.key.get_pressed()


        #depending on what key the user presses, update ball x and y position accordingly
        if keys[pygame.K_UP]:
            ballPosition[1] -= speed
        if keys[pygame.K_DOWN]:
            ballPosition[1] += speed
        if keys[pygame.K_LEFT]:
            ballPosition[0] -= speed
        if keys[pygame.K_RIGHT]:
            ballPosition[0] += speed


        screen.fill(BLACK) #fill the screen with black
        screen.blit(ballImg, ballPosition) #draw the ball
        pygame.display.update() #update the screen

game_loop()
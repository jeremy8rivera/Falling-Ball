import pygame
import time
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
red = (255,0,0)
white = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Fall down')

BLACK = (0,0,0)
green = (0,255,0)

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 100)

score_font = pygame.font.SysFont(None, 25)

platforms = [] #list to hold the platforms



def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [450, screen_height/2])
    pygame.display.update() #update the screen

def score_to_screen(time, color):
    screen_text = score_font.render("Score:" + time, True, color)
    screen.blit(screen_text, [1280, screen_height/2])
    pygame.display.update() #update the screen

def timerScore():
    for i in range(0, 99999999): # 3.1709791983764584961 years
        score_to_screen(str(i), green)
        time.sleep(1)

class Ball(object):
    def __init__(self):
        self.position = [0,0]
        self.img = pygame.image.load('ball.png')
        self.speed = 10
        self.radius = 10

class Platform(object):
    
    def __init__(self, pos):
        platforms.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 500, 10)
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if ball.position[0] > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = platform.rect.left
                if ball.position[0] < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = platform.rect.right
                if ball.position[1] > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = platform.rect.top
                if ball.position[1] < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = platform.rect.bottom

ball = Ball()
platform = Platform([500,500])

def game_loop():
   
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
           if event.type == KEYDOWN:
                if event.key == K_q:
                    exit()

        #get all the keys being pressed
        keys = pygame.key.get_pressed()

        #timerScore() FIGURE OUT WHERE TO PUT THIS SO IT
        
        #depending on what key the user presses, update ball x and y position accordingly
        if keys[pygame.K_UP]:
            ball.position[1] -= ball.speed
        if keys[pygame.K_DOWN]:
            ball.position[1] += ball.speed
        if keys[pygame.K_LEFT]:
            ball.position[0] -= ball.speed
        if keys[pygame.K_RIGHT]:
            ball.position[0] += ball.speed

        #creates boundaries
        if ball.position[0] > 1280:
            #message_to_screen("GAME OVER", red)
            exit()
        if ball.position[0] < 0:
            #message_to_screen("GAME OVER", red)
            exit()
        if ball.position[1] < 0: #hit the top
            message_to_screen("GAME OVER!", red)
            time.sleep(1)
            exit()
        #deal with game over screen later
        ''' 
            for event in pygame.event.get(): 
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        exit()
                    elif event.key == K_p:
                        game_loop()
                #time.sleep(1)
            
            #exit()
            '''
       # platform

        screen.fill(BLACK) #fill the screen with black
        screen.blit(ball.img, ball.position) #draw the ball
        pygame.draw.rect(screen, white, platform.rect)
        pygame.display.update() #update the screen

game_loop()
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

gravity = 3


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [200, screen_height/2])
    pygame.display.update() #update the screen


def timerScore():
   # while time.time()

    '''for i in range(0, 99999999): # 3.1709791983764584961 years
                    score_to_screen(str(i), green)
                    time.sleep(1)'''

class Ball(object):
    def __init__(self):
        self.position = [0,0]
        self.img = pygame.image.load('ball.png')
        self.speed = 10
        self.radius = 50
        self.rect = pygame.Rect(self.position[0], self.position[1], self.radius, self.radius)

    def move_both_axis(self, dx, dy):
        
        # Move the rect
        self.position[0] += dx
        self.position[1] += dy
        self.rect = pygame.Rect(self.position[0], self.position[1], self.radius, self.radius)
        # If you collide with a wall, move out based on velocity
        for platform in platforms:
            if platform.rect.colliderect(self.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.position[0] = platform.rect.left - self.radius
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.position[0] = platform.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.position[1] = platform.rect.top - self.radius
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.position[1] = platform.rect.bottom

class Platform(object):
    
    def __init__(self, pos):
        platforms.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 500, 10)
        self.x = pos[0]
        self.y = pos[1]

    def moveaxis(self, dx, dy):
        
        # Move the rect
        self.x += dx
        self.y += dy
        self.rect = pygame.Rect(self.x, self.y, 500, 10)

ball = Ball()

GamePlatList = []




def game_loop():
    timer = 60*3
   
    x = time.time()
    while 1:
        clock.tick(60)
        
        ball.move_both_axis(0, gravity)
        for event in pygame.event.get():
           if event.type == KEYDOWN:
                if event.key == K_q:
                    exit()
                    
        #platform list
        if(timer%(60*1) == 0):
            platformList = []
            while len(platformList) < 13:
                platformList.append(Platform([100*(len(platformList)), 500]))
            GamePlatList.append(platformList)
        timer +=.75

        #get all the keys being pressed
        keys = pygame.key.get_pressed()

        #timerScore() FIGURE OUT WHERE TO PUT THIS SO IT
        
        #depending on what key the user presses, update ball x and y position accordingly
        if keys[pygame.K_UP]:
            ball.move_both_axis(0, -ball.speed)
        if keys[pygame.K_DOWN]:
            ball.move_both_axis(0, ball.speed)
        if keys[pygame.K_LEFT]:
            ball.move_both_axis(-ball.speed, 0)
        if keys[pygame.K_RIGHT]:
            ball.move_both_axis(ball.speed,0)

        #creates boundaries
        if ball.position[0] > 1280:
            #message_to_screen("GAME OVER", red)
            pygame.display.quit()
            pygame.quit()
            exit()
        if ball.position[0] < 0:
            #message_to_screen("GAME OVER", red)
            pygame.display.quit()
            pygame.quit()
            exit()
        if ball.position[1] < 0: #hit the top
            x= time.time()-x
            #message_to_screen("GAME OVER! Score: " + str(x), red)
            message_to_screen("GAME OVER! Score: {:.1f}".format(x), red)
            time.sleep(3)
            pygame.display.quit()
            pygame.quit()
            exit()
        #deal with game over screen later

        for lst in GamePlatList:
            for i in range(len(lst)):
                lst[i].moveaxis(0, -1.25)

        screen.fill(BLACK) #fill the screen with black
        #pygame.draw.rect(screen, white, ball.rect)
        screen.blit(ball.img, ball.position) #draw the ball

        for lst in GamePlatList:
            for i in range(len(lst)):
                pygame.draw.rect(screen, white, lst[i].rect)
        
        pygame.display.update() #update the screen

game_loop()

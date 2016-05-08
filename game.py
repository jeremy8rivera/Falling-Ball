try:
        import sys
        import random
        import math
        import os
        import getopt
        import pygame
        from socket import *
        from pygame.locals import *
except ImportError, err:
        print "couldn't load module. %s" % (err)
        sys.exit(2)

def load_png(name):
	""" Load image and return image object"""
	fullname = name
	try:
		image = pygame.image.load(fullname)
		if image.get_alpha() is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error, message:
        	print 'Cannot load image:', fullname
        	raise SystemExit, message
	return image, image.get_rect()

class Ball(pygame.sprite.Sprite):
	def __init__(self, (xy)):
		pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.hit = 0
        self.speed = 10
        self.state = "still"
	
	def reinit(self):
		self.state = "still"
		self.movepos = [0,0]
		if self.side == "left":
			self.rect.midleft = self.area.midleft
    
	def update(self):
		newpos = self.rect.move(self.movepos)
		if self.area.contains(newpos):
			self.rect = newpos
		pygame.event.pump()
	
	def moveleft(self):
		self.movepos[1] = self.movepos[1] - (self.speed)
		self.state = "moveleft"

	def moveright(self):
		self.movepos[1] = self.movepos[1] + (self.speed)
		self.state = "moveright"

def main():
	running = True
	pygame.init()
	(width, height) = (800, 600)
	screen = pygame.display.set_mode((width, height))

	# Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))
	screen.blit(background, (0, 0))
	pygame.display.flip()


	global player
	player = Ball("left")
	playersprite = pygame.sprite.RenderPlain(player)

	playersprite.draw(screen)
	player.update()
	while running:
		
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_q:
					running = False
				if event.key == K_LEFT:
					player.moveleft()
				if event.key == K_RIGHT:
					player.moveright()
			elif event.type == KEYUP:
				if event.key == K_UP or event.key == K_DOWN:
					player.movepos = [0,0]
					player.state = "still"
		#screen.blit(background, ball.rect, ball.rect)
		screen.blit(background, player.rect, player.rect)
		#screen.blit(background, player2.rect, player2.rect)
		#ballsprite.update()
		playersprite.update()
		#ballsprite.draw(screen)
		playersprite.draw(screen)
       


if __name__ == '__main__': main()
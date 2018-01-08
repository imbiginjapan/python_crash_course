import sys
import pygame

class Mario():
	
	def __init__(self,screen):
		""" Initialize the ship and starting position """
		self.screen = screen
		
		# Load the ship image and get its rect
		self.image = pygame.image.load('mario.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start each ship at bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
	def blitme(self):
		""" Draw the ship at its current location """
		self.screen.blit(self.image,self.rect)
		
pygame.init()
screen = pygame.display.set_mode(
		(880,600))
screen.fill((255,255,255))
mario = Mario(screen)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	screen.fill((255,255,255))
	print(mario.rect.centery)
	mario.blitme()
	pygame.display.flip()
	



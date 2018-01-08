import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	""" A class that represents a single Alien. """
	
	def __init__(self, ai_settings, screen):
		""" Initialize the alien and its starting position. """
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		# Load the alien image and set its rect.
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		# Store the alien's position.
		self.x = float(self.rect.x)
		
	def blitme(self):
		""" Draw the alien at its current location """
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		self.x += (self.ai_settings.alien_speed_factor * 
				   self.ai_settings.fleet_direction)
		self.rect.x = self.x
		
	def check_edges(self):
		""" Return True if an alien is at the edge of the screen """
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
			
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" Class Manages bullets fired from ship """
	def __init__(self, ai_settings, screen, ship):
		""" Create a bullet at the ship position """
		super(Bullet, self).__init__()
		self.screen = screen
	
	# Create a bullet rect at (0,0) and set correct position.
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
			ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
	
	# Store the bullet's position.
		self.y = float(self.rect.y)
	
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
	
	
	def update(self):	
		# Update the position of the bullet.
		self.y -= self.speed_factor
		# Update the rect position.
		self.rect.y = self.y
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)


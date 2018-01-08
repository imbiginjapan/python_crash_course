import pygame

class Ship():
	
	def __init__(self, ai_settings, screen):
		""" Initialize the ship and starting position """
		self.screen = screen
		self.ai_settings = ai_settings
		
		# Load the ship image and get its rect
		self.rect = pygame.Rect(0, 0, ai_settings.ship_width,
			ai_settings.bullet_height)
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.color = ai_settings.bullet_color
		
		# Mark Ship Center
		self.center = float(self.rect.centerx)
		
		# Movement Flags
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		""" Update the ship's position based on the movement flag. """
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		self.rect.centerx = self.center
			
	def blitme(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

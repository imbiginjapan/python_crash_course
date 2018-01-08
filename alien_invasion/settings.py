class Settings():
	""" Stores all settings for game """
	
	def __init__(self):
		""" Initialize Settings """
		# Screen Settings
		self.screen_width = 1600
		self.screen_height = 900
		self.bg_color = (230, 230, 230)
		
		# Ship Settings
		self.ship_limit = 3

		# Shot Settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
		
		# Alien Settings
		self.fleet_drop_speed = 10
		
		# Speedup Settings
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		""" Initialize speed settings that change throughout the game """
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		""" 1 is right, -1 is left """
		self.fleet_direction = 1
		self.alien_points = 50
	
	def increase_speed(self):
		""" Increase the speed settings """
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		self.alien_points = int(self.alien_points * self.score_scale)
		

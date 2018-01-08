class Settings():
	""" Stores all settings for game """
	
	def __init__(self):
		""" Initialize Settings """
		# Screen Settings
		self.screen_width = 1600
		self.screen_height = 900
		self.bg_color = (230, 230, 230)
		
		# Ship Settings
		self.ship_speed_factor = 1.5
		self.ship_width = 30
		
		# Shot Settings
		self.bullet_speed_factor = 3.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
		
		# Alien Settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		""" 1 is right, -1 is left """
		self.fleet_direction = 1

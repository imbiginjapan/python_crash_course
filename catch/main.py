import sys

import pygame

import game_functions as gf
from alien import Alien
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
	# Initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	
	# Set the background color
	bg_color = ai_settings.bg_color
	
	# Create a ship
	ship = Ship(ai_settings,screen)
	# Container for bullets
	bullets = Group()
	aliens = Group()
	
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	
	# Main Loop for the game
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
			
run_game()

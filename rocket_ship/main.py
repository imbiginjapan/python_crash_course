import sys

import pygame
import inspect

import game_functions as gf
from settings import Settings
from ship import Ship

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
	
	# Main Loop for the game
	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)
			
run_game()

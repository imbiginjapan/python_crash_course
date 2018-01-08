import sys

import pygame

import game_functions as gf
from alien import Alien
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	# Initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	play_button = Button(ai_settings, screen, "Play")
	
	#Create an instance to store game statistics.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
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
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
			
run_game()

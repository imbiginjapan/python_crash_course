import sys

import pygame
from pygame.sprite import Group
from /alien_invasion/settings import Settings

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
			(ai_settings.screen_width,ai_settings.screen_height))


run_game()

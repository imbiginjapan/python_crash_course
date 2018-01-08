import sys

import pygame

def check_events(ship):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		
def check_keydown_events(event, ship):
	if event.key == pygame.K_RIGHT:
		# move ship right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	if event.key == pygame.K_UP:
		# move ship up
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
			

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		# stop moving right
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	if event.key == pygame.K_UP:
		# move ship up
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
	
		
def update_screen(ai_settings, screen, ship):
	""" Update images and flip to the new screen """
	# Redraw the screen through each pass in the loop
	screen.fill(ai_settings.bg_color)
	ship.blitme()
		
	# Make the most recently drawn screen visible
	pygame.display.flip()
		

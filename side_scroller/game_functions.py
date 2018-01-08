import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_UP:
		# move ship UP
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		# Create a new bullet and add it to bullets group.
		if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)
	elif event.key == pygame.K_q:
		sys.exit()
			
def check_keyup_events(event, ship):
	if event.key == pygame.K_UP:
		# stop moving up
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
		
def update_screen(ai_settings, screen, ship, bullets):
	""" Update images and flip to the new screen """
	# Redraw the screen through each pass in the loop
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
		
	# Make the most recently drawn screen visible
	pygame.display.flip()
	
def update_bullets(bullets,screen):
	bullets.update()
		
	# Remove bullets that reach right side of screen.
	for bullet in bullets.copy():
		if bullet.rect.left >= bullet.screen_rect.right:
			bullets.remove(bullet)

def create_fleet(ai_settings, screen, aliens):
	# Spacing between aliens = 1 alien width
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	
	# First row of aliens.
	for alien_number in range(number_aliens_x):
		# Create an alien and add to row.
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		aliens.add(alien)
	
	


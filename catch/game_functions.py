import sys

import pygame

from bullet import Bullet
from alien import Alien
from random import randint

def check_events(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		# move ship right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_q:
		sys.exit()
			
def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		# stop moving right
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
		
def update_screen(ai_settings, screen, ship, aliens, bullets):
	""" Update images and flip to the new screen """
	# Redraw the screen through each pass in the loop
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
		
	# Make the most recently drawn screen visible
	pygame.display.flip()
	
def update_bullets(ai_settings, screen, ship, aliens, bullets):
	bullets.update()
		
	# Remove bullets that reach top of screen.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)


	check_alien_bullet_collisions(ai_settings, screen, ship, aliens, bullets)

def check_alien_bullet_collisions(ai_settings, screen, ship, aliens, bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	
	if len(aliens) == 0:
		# Destroy existing bullets and create new fleet.
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)
	
	
def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
		
	
def get_number_aliens_x(ai_settings, alien_width):	
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x
	
	
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	# Create an alien and add to row.
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
	
def get_number_rows(ai_settings, ship_height, alien_height):
	available_space_y = (ai_settings.screen_height - (3 * alien_height)
						- ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows


def create_fleet(ai_settings, screen, ship, aliens):
	# Spacing between aliens = 1 alien width
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	number_aliens_x = 1
	number_rows = 1
	create_alien(ai_settings, screen, aliens)

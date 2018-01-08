import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

while True:
	screen.fill((255,255,255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN: 
			print(event.key)
		
	# Make the most recently drawn screen visible
	pygame.display.flip()
	

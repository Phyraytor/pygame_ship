import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#Inicialize game and create object screen
	pygame.init()
	ai_settings = Settings()

	screen = pygame.display.set_mode( 
		(ai_settings.screen_width, ai_settings.screen_height) )
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(ai_settings, screen)
	bullets = Group()
	#play main loop game
	while True:
		# Отслеживание событий клавиатуры и мыши
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		print( len(bullets) )
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()

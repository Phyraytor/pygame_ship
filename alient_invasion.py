import sys
import pygame
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

	ship = Ship(screen)

	bg_color = (230, 230, 230)
	#play main loop game
	while True:
		# Отслеживание событий клавиатуры и мыши
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)

run_game()

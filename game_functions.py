import sys
import pygame

def check_events(ship):
	"""обрабатывает нажатия клавиш и события мыши"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				#Переместить корабль вправо
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				#Переместить корабль вправо
				ship.moving_left = True

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			if event.key == pygame.K_LEFT:
				ship.moving_left = False

def update_screen(ai_settings, screen, ship):
	"""Обновляет изображения на экране и отображает 
	новый экран"""
	# При каждом обходе цикла перерисовывается экран
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	# Отображение  Последнего прорисованного экрана
	pygame.display.flip()


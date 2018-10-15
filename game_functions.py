import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	"""обрабатывает нажатия клавиш и события мыши"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
	"""Обновляет изображения на экране и отображает 
	новый экран"""
	# При каждом обходе цикла перерисовывается экран
	screen.fill(ai_settings.bg_color)
	#all bullets output back image ship and enemy
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	# Отображение  Последнего прорисованного экрана
	pygame.display.flip()

def update_bullets(bullets):
	"""Upload position bullet and remove old bullet"""
	bullets.update()

	# delete old bullet, outside for top screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
	"""create bullet, if bullents count < limit"""
	#Create new Bullet and on his in group Bullets."""
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)	
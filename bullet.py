import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" Класс для упраления пулями, выпущенными кораблём"""
	def __init__(self, ai_settings, screen, ship):
		"""Create object bullet in this position ship"""
		super().__init__()
		self.screen = screen

		# Create bullet in position (0,0) and accepted position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
			ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#Position bullet store float format
		self.y = float(self.rect.top)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		""" move bullet in top for screen"""
		# upload position bullet float format
		self.y -= self.speed_factor
		#rect = прямоугольник
		#upload position rect
		self.rect.y = self.y

	def draw_bullet(self):
		"""Output bullet for screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)

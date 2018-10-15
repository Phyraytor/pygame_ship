import pygame

class Ship():
	def __init__(self, screen):
		"""Create ship and setup begin coordinat"""
		self.screen = screen

		# Downloads image sip and senf square
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#new ship show bottom in screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Обновляет позицию корабля с учётом флага"""
		if self.moving_right:
			self.rect.centerx += 1

		if self.moving_left:
			self.rect.centerx -= 1

	def blitme(self):
		""" picture ship in this position """
		self.screen.blit(self.image, self.rect)
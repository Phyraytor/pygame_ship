import pygame

class Ship():
	def __init__(self, ai_settings, screen):
		"""Create ship and setup begin coordinat"""
		self.screen = screen
		self.ai_settings = ai_settings
		
		# Downloads image sip and senf square
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#new ship show bottom in screen
		self.rect.centerx = float(self.screen_rect.centerx)
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Обновляет позицию корабля с учётом флага"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.ai_settings.ship_speed_factor

		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= self.ai_settings.ship_speed_factor

	def blitme(self):
		""" picture ship in this position """
		self.screen.blit(self.image, self.rect)
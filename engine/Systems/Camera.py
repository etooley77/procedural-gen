import pygame

class CameraGroup(pygame.sprite.Group):
	def __init__(self, screen):
		super().__init__(self)
		self.screen = screen
		self.display_surface = pygame.display.get_surface()

	def _draw(self, entity):
		self.screen.blit(entity.image, entity.rect)
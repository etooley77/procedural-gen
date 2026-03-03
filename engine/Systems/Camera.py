import pygame

class CameraGroup(pygame.sprite.Group):
	def __init__(self, screen):
		super().__init__(self)
		self.screen = screen
		self.display_surface = pygame.display.get_surface()

		# camera offset
		self.offset = pygame.math.Vector2(0, 0)


	def _draw(self, entities, player):
		for entity in entities:
			pygame.draw.rect(self.display_surface, entity.color, entity.rect)

		offset_pos = player.rect.topleft + self.offset
		self.screen.blit(player.image, offset_pos)
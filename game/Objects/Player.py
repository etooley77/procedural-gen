import pygame

from game.constants import TILE_WIDTH, TILE_HEIGHT

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		# super().__init__(group)
		self.image = pygame.image.load('game/assets/player/player2.png').convert_alpha()
		self.scale_image_to_tilesize()

		self.rect = self.image.get_rect(topleft = pos)

	def scale_image_to_tilesize(self):
		original_width = self.image.get_rect().width
		original_height = self.image.get_rect().height

		width_scale = TILE_WIDTH / original_width
		height_scale = TILE_HEIGHT / original_height

		self.image = pygame.transform.scale(self.image, (original_width * width_scale, original_height * height_scale))

	def input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pass

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.k_w:
					print("w pressed")
					self.move(pygame.math.Vector2(0, -1))
				if event.key == pygame.k_a:
					self.move(pygame.math.Vector2(-1, 0))
				if event.key == pygame.k_s:
					self.move(pygame.math.Vector2(0, 1))
				if event.key == pygame.k_d:
					self.move(pygame.math.Vector2(1, 0))

	def move(self, dir):
		self.rect.x += dir.x * TILE_WIDTH
		self.rect.y += dir.y * TILE_HEIGHT
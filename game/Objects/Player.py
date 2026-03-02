import pygame

from game.constants import TILE_WIDTH, TILE_HEIGHT

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)
		self.image = pygame.image.load('game/assets/player/player2.png').convert_alpha()
		self.scale_image_to_tilesize()

		self.rect = self.image.get_rect(topleft = pos)
		self.vector_directions = {"up": (0, -1), "left": (-1, 0), "down": (0, 1), "right": (1, 0)}

	def scale_image_to_tilesize(self):
		original_width = self.image.get_rect().width
		original_height = self.image.get_rect().height

		width_scale = TILE_WIDTH / original_width
		height_scale = TILE_HEIGHT / original_height

		self.image = pygame.transform.scale(self.image, (original_width * width_scale, original_height * height_scale))

	# 

	def transform(self, vec_dir):
		self.rect.x += TILE_WIDTH * vec_dir[0]
		self.rect.y += TILE_HEIGHT * vec_dir[1]

	# 

	def handle_action(self, action: str):
		try:
			self.transform(self.vector_directions[action])
		except KeyError:
			print("The Player action could not be resolved.")
import pygame, sys
from random import choice

from tile import Tile
# from player import Player

from constants import *

# 

class Game():
	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Procedural Map Generation")

		# self.player = Player()

		self.tiles = pygame.sprite.Group()
		self.tiles_list = []
		self.dirty_tiles = []

		self.generating = True
		self.available_tiles = set()

		self.game_time = 0
		self.accumulator = 0

		self.init_board()
		self.init_first_tile(MEADOW)

	def init_board(self):
		# Create all tiles
		id = 1

		for i in range(int(HEIGHT / TILE_HEIGHT)):
			for j in range(int(WIDTH / TILE_WIDTH)):
				tile = Tile(id, j * TILE_WIDTH, i * TILE_HEIGHT, BLACK)

				self.tiles.add(tile)
				self.tiles_list.append(tile)

				id += 1

		# Compute neighbors
		rows = HEIGHT // TILE_HEIGHT
		cols = WIDTH // TILE_WIDTH

		for row in range(rows):
			for col in range(cols):
				index = row * cols + col
				tile = self.tiles_list[index]

				for dy in (-1, 0, 1):
					for dx in (-1, 0, 1):
						if dx == 0 and dy == 0:
							continue

						new_row = row + dy
						new_col = col + dx

						if 0 <= new_row < rows and 0 <= new_col < cols:
							neighbor_index = new_row * cols + new_col
							tile.neighbors.append(neighbor_index)
	
	def init_first_tile(self, color):
		self.update_tile((len(self.tiles_list) // 2 + ((WIDTH // 2) // TILE_WIDTH)), color)

	def is_generating(self):
		return bool(self.available_tiles)

	# 

	def get_next_tile(self):
		if self.available_tiles:
			choice_index = min(self.available_tiles, key=lambda i: len(self.tiles_list[i].options))
			choice_tile = self.tiles_list[choice_index]

			if choice_tile.options:
				choice_color = choice(tuple(choice_tile.options))

				self.update_tile(choice_index, choice_color)

	def update_tile(self, index, color):
		tile = self.tiles_list[index]

		if tile.color != color:
			tile.color = color
			tile.collapse()

		self.update_neighbors(tile.neighbors, color)

		self.available_tiles.discard(index)
		self.dirty_tiles.append(tile)

	def update_neighbors(self, neighbors, color):
		for n in neighbors:
			neighbor = self.tiles_list[n]

			if neighbor.collapsed:
				continue

			if color == FOREST:
				neighbor.options.discard(WATER)
				neighbor.options.discard(SAND)
			elif color == MEADOW:
				neighbor.options.discard(WATER)
			elif color == SAND:
				neighbor.options.discard(FOREST)
			elif color == WATER:
				neighbor.options.discard(FOREST)
				neighbor.options.discard(MEADOW)

			self.available_tiles.add(n)

	# 

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN and not self.is_generating():
					pass

			# Calculate game time
			delta_time = self.clock.tick()
			self.accumulator += delta_time

			if self.accumulator >= 1000:
				self.accumulator -= 1000
				self.game_time += 1

			if self.is_generating():
				self.get_next_tile()

			for tile in self.dirty_tiles:
				pygame.draw.rect(self.screen, tile.color, tile.rect)
				
			self.dirty_tiles.clear()

			# pygame.draw.rect(self.screen, self.player.color, self.player.rect)

			pygame.display.flip()
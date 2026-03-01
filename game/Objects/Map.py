import heapq
from pygame import sprite
from random import choice

from game.Objects.Tile import Tile

from game.constants import *

class Map():
	def __init__(self, render_system):
		self.render_system = render_system

		self.tiles = sprite.Group()
		self.tiles_list = []
		self.dirty_tiles = []

		self.available_heap = []

		self.init_map()
		self.render()

	def init_map(self):
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

						if dx == -1 and dy == -1 or dx == -1 and dy == 1:
							continue
						if dx == 1 and dy == -1 or dx == 1 and dy == 1:
							continue

						new_row = row + dy
						new_col = col + dx

						if 0 <= new_row < rows and 0 <= new_col < cols:
							neighbor_index = new_row * cols + new_col
							tile.neighbors.append(neighbor_index)

		self.init_first_tile()

	def init_first_tile(self):
		self.update_tile((len(self.tiles_list) // 2 + ((WIDTH // 2) // TILE_WIDTH)), choice([WATER, SAND, MEADOW, FOREST]))
		self.update_all_tiles()

	def update_all_tiles(self):
		while self.available_heap:
			choice_entropy, choice_index = heapq.heappop(self.available_heap)
			choice_tile = self.tiles_list[choice_index]

			if choice_tile.collapsed:
				continue

			if len(choice_tile.options) != choice_entropy:
				continue

			if choice_tile.options:
				choice_color = choice(tuple(choice_tile.options))

				self.update_tile(choice_index, choice_color)

	def update_tile(self, index, color):
		tile = self.tiles_list[index]

		if tile.color != color:
			tile.color = color
			tile.collapse()

		self.update_neighbors(tile.neighbors, color)

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

			entropy = len(neighbor.options)
			heapq.heappush(self.available_heap, (entropy, n))

	# Main callables
	def update_changes(self):
		self.render_system.draw(self.dirty_tiles)

	def render(self):
		self.render_system.draw(self.tiles)
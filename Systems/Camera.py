from constants import TILE_WIDTH, TILE_HEIGHT

class Camera():
	def __init__(self, zoom):
		self.zoom = zoom

		self.pos = (0, 0)

	def scale(self, entities):
		entity_group = []

		for entity in entities:
			if entity.rect.width < TILE_WIDTH * self.zoom and entity.rect.height < TILE_HEIGHT * self.zoom:
				entity.rect.x *= self.zoom
				entity.rect.y *= self.zoom
				entity.rect.width *= self.zoom
				entity.rect.height *= self.zoom

			entity_group.append(entity)

		return entity_group
	
	def transform(self, dir):
		pass
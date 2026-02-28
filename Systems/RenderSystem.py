from pygame import draw

class RenderSystem():
	def __init__(self, screen):
		self.screen = screen

	def update(self, entities):
		for entity in entities:
			draw.rect(self.screen, entity.color, entity.rect)
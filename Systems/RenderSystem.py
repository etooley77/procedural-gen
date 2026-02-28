from pygame import draw
import pygame

from constants import BLACK

class RenderSystem():
	def __init__(self, screen):
		self.screen = screen

	# Does not get called every frame (triggered by events)
	def draw(self, entity_group):
		for entity in entity_group:
			draw.rect(self.screen, entity.color, entity.rect)

	def undraw(self, entity_group):
		print("s")
		entity_group.clear(self.screen, BLACK)

	# Updated every frame (animation, movement)
	def render(self, entities):
		pass
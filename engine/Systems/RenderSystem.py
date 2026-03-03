from pygame import draw
import pygame

from game.constants import BLACK

class RenderSystem:
	def __init__(self, screen):
		self.screen = screen

	# Does not get called every frame (triggered by events)
	def draw(self, entity_group):
		pass
		# for entity in entity_group:
		# 	draw.rect(self.screen, entity.color, entity.rect)

	def undraw(self, entity_group):
		self.screen.fill(BLACK)

	# Updated every frame (animation)
	def render(self, entities):
		pass
from pygame import draw
import pygame

from Systems.Camera import Camera

from constants import BLACK

class RenderSystem():
	def __init__(self, screen):
		self.screen = screen

		self.camera = Camera(2)

	# Does not get called every frame (triggered by events)
	def draw(self, entity_group):
		for entity in self.camera.scale(entity_group):
			draw.rect(self.screen, entity.color, entity.rect)

	def undraw(self, entity_group):
		self.screen.fill(BLACK)

	# Updated every frame (animation, movement)
	def render(self, entities):
		pass
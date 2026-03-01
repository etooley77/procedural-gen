import pygame

class InputManager:
	def __init__(self):
		pass

	def process(self, queue):
		for event in queue:
			match event:
				case pygame.K_w:
					print("w was pressed")
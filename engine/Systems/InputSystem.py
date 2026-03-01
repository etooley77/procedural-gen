import pygame, sys

class InputSystem:
	def __init__(self):
		self.input_queue = []
		print("Input System initialized!")

	def keybind(self):
		pass

	def monitor_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				self.input_queue.append(event.key)

		return self.input_queue
	
	def clear_queue(self):
		self.input_queue.clear()
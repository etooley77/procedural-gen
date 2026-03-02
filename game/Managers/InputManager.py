import pygame
import json

class InputManager:
	def __init__(self):
		self.keybinds = {}

		self.register_keybinds()

	def register_keybinds(self):
		with open("game/config.json", 'r', encoding='utf-8') as f:
			config = json.load(f)
			self.keybinds = config['keybinds']['player']

	def process(self, queue):
		actions = []
		for event in queue:
			for key, value in self.keybinds.items():
				if event.dict['unicode'] == value:
					actions.append(key)

		return actions
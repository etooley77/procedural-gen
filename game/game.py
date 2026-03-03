import pygame, sys
from random import choice
import heapq

from engine.Systems.RenderSystem import RenderSystem
from engine.Systems.InputSystem import InputSystem
from engine.Systems.Camera import CameraGroup

from game.Managers.InputManager import InputManager

from game.Objects.Map import Map
from game.Objects.Player import Player

# from player import Player

from game.constants import *

# 

class Game():
	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Procedural Map Generation")

		# Systems
		self.render_system = RenderSystem(self.screen)
		self.input_system = InputSystem()

		# Managers
		self.input_manager = InputManager()

		# Game Objects
		self.map = Map(self.render_system)
		self.camera_group = CameraGroup(self.screen)
		self.player = Player((WIDTH // 2, HEIGHT // 2), self.camera_group)

		self.game_time = 0
		self.accumulator = 0

	# 

	def handle_actions(self, actions: list[str]):
		for action in actions:
			_action = action.split('-')
			match _action[0]:
				case "player":
					self.player.handle_action(_action[1])
				case _:
					print("No valid action could be found!")
	
	# 

	def run(self):
		while True:
			input_list = self.input_system.monitor_input()
			actions = self.input_manager.process(input_list)
			self.handle_actions(actions)

			# Calculate game time
			delta_time = self.clock.tick()
			self.accumulator += delta_time

			if self.accumulator >= 1000:
				self.accumulator -= 1000
				self.game_time += 1

			self.screen.fill(BLACK)

			# Draw the camera group things
			self.camera_group.update()
			self.camera_group.draw(self.map.tiles, self.player)

			# Clear the input queue for the next frame
			self.input_system.clear_queue()

			pygame.display.flip()
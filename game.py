import pygame, sys
from random import choice
import heapq

from Systems.RenderSystem import RenderSystem
from GameObjects.Map import Map

# from player import Player

from constants import *

# 

class Game():
	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Procedural Map Generation")

		# Systems
		self.render_system = RenderSystem(self.screen)

		# Game Objects
		self.map = Map(self.render_system)

		self.game_time = 0
		self.accumulator = 0
	
	# 

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.map.render()
					if event.key == pygame.K_e:
						self.map.unrender()

			# Calculate game time
			delta_time = self.clock.tick()
			self.accumulator += delta_time

			if self.accumulator >= 1000:
				self.accumulator -= 1000
				self.game_time += 1

			pygame.display.flip()
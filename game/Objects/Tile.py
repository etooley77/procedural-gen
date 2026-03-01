import pygame
from pygame import sprite

from game.constants import *

class Tile(sprite.Sprite):
    def __init__(self, id, x, y, color):
        super().__init__()
        self.id = id
        self.collapsed = False

        self.x = x
        self.y = y

        self.color = color
        self.options = {WATER, SAND, MEADOW, FOREST}
        self.neighbors = []

        self.rect = self.create_rect()

    def create_rect(self):
        return pygame.Rect(self.x, self.y, TILE_WIDTH, TILE_HEIGHT)
    
    def collapse(self):
        self.collapsed = True
        self.options.clear()
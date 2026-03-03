import pygame

class CameraGroup(pygame.sprite.Group):
	def __init__(self, screen):
		super().__init__()
		self.screen = screen
		self.display_surface = pygame.display.get_surface()

		# camera offset
		self.offset = pygame.math.Vector2(0, 0)

		self.half_w = self.display_surface.get_size()[0] // 2
		self.half_h = self.display_surface.get_size()[1] // 2

		# box camera setup
		self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
		l = self.camera_borders['left']
		t = self.camera_borders['top']
		w = self.display_surface.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
		h = self.display_surface.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
		self.camera_rect = pygame.Rect(l, t, w, h)

		# zoom setup
		self.zoom_scale = 5
		self.internal_surface_size = (self.display_surface.get_width() + 200, self.display_surface.get_height() + 200)
		self.internal_surface = pygame.Surface(self.internal_surface_size, pygame.SRCALPHA)
		self.internal_rect = self.internal_surface.get_rect(center = (self.half_w, self.half_h))
		self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surface_size)
		self.internal_surface_offset = pygame.math.Vector2(0, 0)
		self.internal_surface_offset.x = self.internal_surface_size[0] // 2 - self.half_w
		self.internal_surface_offset.y = self.internal_surface_size[1] // 2 - self.half_h

	def center_target_camera(self, target):
		self.offset.x = target.rect.x - self.half_w
		self.offset.y = target.rect.y - self.half_h

	def box_camera(self, target):
		if target.rect.left < self.camera_rect.left:
			self.camera_rect.left = target.rect.left
		if target.rect.right > self.camera_rect.right:
			self.camera_rect.right = target.rect.right
		if target.rect.top < self.camera_rect.top:
			self.camera_rect.top = target.rect.top
		if target.rect.bottom > self.camera_rect.bottom:
			self.camera_rect.bottom = target.rect.bottom

		self.offset.x = self.camera_rect.left - self.camera_borders['left']
		self.offset.y = self.camera_rect.top - self.camera_borders['top']

	def draw(self, entities, player):
		self.box_camera(player)
		# self.center_target_camera(player)

		self.internal_surface.fill((0, 0, 0))

		for entity in entities:
			entity_offset = pygame.math.Vector2(entity.rect.x, entity.rect.y) - self.offset + self.internal_surface_offset
				
			if entity.rect.colliderect(self.internal_rect):
				pygame.draw.rect(self.internal_surface, entity.color, (entity_offset.x, entity_offset.y, entity.rect.width, entity.rect.height))

		offset_pos = player.rect.topleft - self.offset + self.internal_surface_offset
		self.internal_surface.blit(player.image, offset_pos)

		scaled_surface = pygame.transform.scale(self.internal_surface, self.internal_surface_size_vector * self.zoom_scale)
		scaled_rect = scaled_surface.get_rect(center = (self.half_w, self.half_h))

		self.display_surface.blit(scaled_surface, scaled_rect)

		pygame.draw.rect(self.display_surface, 'yellow', self.camera_rect, 2)
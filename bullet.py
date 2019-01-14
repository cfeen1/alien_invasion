import pygame
from pygame.sprite import Sprite
""" Sprites are useful because you can group related elements in the 
game and act on all the grouped elements at once.  In order to create
a bullet instance, __init__() needs the ai_settings, screen, and ship 
instances and we call super() to inherit them properly from Sprite"""

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship"""
	def __init__(self, ai_settings, screen, ship):
		"""Create a bullet object at the ship's current position"""
		"""the super function can be used to gain access to inherited
		methods – from a parent or sibling class – that has been
		overwritten in a class object"""
		
		super(Bullet, self).__init__()
		self.screen = screen
		
		# Create a bullet rect at (0,0) and then set correct position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
			ai_settings.bullet_height)
		# sets the bullet position to the ship position
		self.rect.centerx = ship.rect.centerx
		# set the bullet to the top of ship 
		self.rect.top = ship.rect.top
		
		# Store the bullet's position as a decimal value
		# so that we can make fine adjustments to the speed
		self.y = float(self.rect.y)
		
		# storing the bullet's color and speed settings
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""Move the bullet up the screen, manages bullets position"""
		# Update the decimal position of the bullet
		# moves up the screen corresponding to a decreasing y-value
		self.y -= self.speed_factor
		#update the rect position
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""Draw the bullet to the screen"""
		# this requires three arguments, the screen its being drawn to
		# The color and position of the bullet
		pygame.draw.rect(self.screen, self.color, self.rect)

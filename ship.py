import pygame
from pygame.sprite import Sprite

# creating a class, called ship, to store all the information about the ship
class Ship(Sprite):
	
	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position"""
		super(Ship, self).__init__()
		# setting the argument screen to the general screen
		# same for the ai_settings, so each time this function is called
		# it sets its to the updated screen and ai_settings
		self.screen = screen
		self.ai_settings = ai_settings
		
		# Load the ship image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		# image was too large, needed to control the size
		self.image = pygame.transform.scale(self.image, (40, 40))
		# pygame uses rectangles, get the rectangle info from the image
		self.rect = self.image.get_rect()
		# and also from the screen
		self.screen_rect = screen.get_rect()
		
		# Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# store a decimal value for the ship's center
		self.center = float(self.rect.centerx)
		
		# Movement flags, default to False so nothing happens
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update the ship's position based on the movement flag"""
		# update the ship's center value, not the rect
		# the script after the and is to ensure the ship stays infield
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		# update rect object from self.center
		self.rect.centerx = self.center
		
	def blitme(self):
		"""Draw the ship at its current location"""
		# draws the image to the screen at the position specified by self.rect
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		"""Center the ship on the screen"""
		self.center = self.screen_rect.centerx

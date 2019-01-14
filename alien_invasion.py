import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button 
from ship import Ship
import game_functions as gf

def run_game():
	# Initialize game and create a screen object.
	pygame.init() # initializes background settings that pygame needs to work 
	# asking python to use the Settings class from settings.py to determine the
	# games settings and storing it as ai_settings
	ai_settings = Settings()
	# setting the display to the height and width from the settings.py module 
	# and storing it as screen
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	# creates the display window, 800 pixels by 400 pixels, defined in a tuple
	# creates a caption at the top of the window
	pygame.display.set_caption("Alien Invasion")
	
	# Make the Play button
	play_button = Button(ai_settings, screen, "Play")
	
	# Create an instance to store game statistics
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	# Make a ship
	# using the Ship class from ship.py to determine what ship to use 
	ship = Ship(ai_settings, screen)
	
	# Make a group to store the bullets in
	# this is stored outside the while loop so a new group of bullets
	# isn't created everytime the loop cycles
	bullets = Group()
	
	# Make an empty group to hold all the aliens in the game
	aliens = Group()
	
	# Create the fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# Start the main loop for the game
	# we make a while loop so that the game is constanly being refreshed
	# as elements of the game change
	while True:
		# looking for changes to the ship within the game_functions module
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
			aliens, bullets)
		# updating the position of the ship using the update function within 
		# the ship module
		# the parts of the game within the if block should only run
		# while game is active
		if stats.game_active:
			ship.update()	
			gf.update_bullets(ai_settings, screen, stats, sb, ship,
				aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		# updating the display of the game using the update_screen function
		#within the game_functions module
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
			play_button)

# calls the function to run the game	
run_game()

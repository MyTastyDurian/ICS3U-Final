'''
Richard Feng
ICS3U
June 2022
Ground sprite (terrain that the player walks on) file of the rpg game
'''

# importing pygame library to access pygame graphics
import pygame

# import the code from my own files; seperated in different files for organization purposes
from constants import *

# the class 'Ground' is defined and will embody all the code for the ground sprite
class Ground(pygame.sprite.Sprite):
    '''
    This is a class for obtaining a block sprite that serves as a border

    Attributes:
        game (any): Access all the variables in the game class
        x (int): The x-coordinate to set where the ground will appear on the screen
        y (int): The y-coordiante to set where the ground will appear on the screen
    '''

    def __init__(self, game, x, y):
        '''
        The constructor for Ground class.

        Parameters:
            game (any): Access all the variables in the game class
            x (int): The x-coordinate to set where the ground will appear on the screen
            y (int): The y-coordiante to set where the ground will appear on the screen

        '''

        self.game = game
        # sets the layer on the screen where the ground will appear
        self._layer = ground_layer
        # block sprites are now a part of the the all_sprites group
        self.groups = self.game.all_sprites
        # call the init method for the inherited class
        pygame.sprite.Sprite.__init__(self, self.groups)

        # tile based game where each tile is 32 x 32 pixels; the coordinates will need scaling
        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize

        # sets the image for the ground class by obtaining the top left coordinate of a pixel in reference to the inherited spritesheet
        self.image = self.game.terrain_spritesheet.get_sprite(0, 0, self.width, self.height)

        # every sprite has a rect which is its positioning; often referred to as the hitbox
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 

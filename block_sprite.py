'''
Richard Feng
ICS3U
June 2022
Block sprite (walls that pervents player from walking off the map) file of the rpg game
'''

# importing pygame library to access pygame graphics
import pygame

# import the code from my own files; seperated in different files for organization purposes
from constants import *

# the class 'Block' is defined and will embody all the code for the block sprite
class Block(pygame.sprite.Sprite):
    '''
    This is a class for obtaining a block sprite that serves as a border

    Attributes:
        game (any): Access all the variables in the game class
        x (int): The x-coordinate to set where the block will appear on the screen
        y (int): The y-coordiante to set where the block will appear on the screen
    '''

    def __init__(self, game, x, y):
        '''
        The constructor for Block class.

        Parameters:
            game (any): Access all the variables in the game class
            x (int): The x-coordinate to set where the block will appear on the screen
            y (int): The y-coordiante to set where the block will appear on the screen

        '''

        # game class inheritance
        self.game = game

        # sets the layer on the screen where the blocks will appear
        self._layer = block_layer

        # block sprites are now a part of the the all_sprites and blocks groups
        self.groups = self.game.all_sprites, self.game.blocks
        # call the init method for the inherited class
        pygame.sprite.Sprite.__init__(self, self.groups)

        # tile based game where each tile is 32 x 32 pixels; the coordinates will need scaling
        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize

        # sets the image for the block class by obtaining the top left coordinate of a pixel in reference to the inherited spritesheet
        self.image = self.game.terrain_spritesheet.get_sprite(0, 1152, self.width, self.height)

        # every sprite has a rect which is its positioning; often referred to as the hitbox
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
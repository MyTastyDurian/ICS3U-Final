'''
Richard Feng
ICS3U
June 2022
Tree sprite (decoration) file of the rpg game
'''

# importing pygame library to access pygame graphics
import pygame

# import the code from my own files; seperated in different files for organization purposes
from constants import *

# the class 'trees' is defined and will embody all the code for the tree sprite
class trees(pygame.sprite.Sprite):
    '''
    This is a class for obtaining a tree sprite that serves as decor

    Attributes:
        game (any): Access all the variables in the game class
        x (int): The x-coordinate to set where the block will appear on the screen
        y (int): The y-coordinate to set where the block will appear on the screen
        counter_x (int): Used to access a different x-coordinate on the spritesheet
        counter_y (int): Use to access a different y-coordinate on the spritesheet
    '''
    def __init__(self, game, x, y, counter_x, counter_y):
        '''
        The constructor for trees class

        Parameters:
            game (any): Access all the variables in the game class
            x (int): The x-coordinate to set where the block will appear on the screen
            y (int): The y-coordinate to set where the block will appear on the screen
            counter_x (int): Used to access a different x-coordinate on the spritesheet
            counter_y (int): Use to access a different y-coordinate on the spritesheet
        '''

        # game class variable
        self.game = game

        # changes the coordinate accessed on spritesheet to acess 4 different pixels (4 parts of the tree)
        self.counter_x = counter_x * 32
        self.counter_y = counter_y * 32
        # sets the layer on the screen where the trees will appear
        self._layer = tree_layer
        # tree sprites are now a part of the the all_sprites group
        self.groups = self.game.all_sprites
        # call the init method for the inherited class
        pygame.sprite.Sprite.__init__(self, self.groups)

        # tile based game where each tile is 32 x 32 pixels; the coordinates will need scaling
        self.x = x * tilesize 
        self.y = y * tilesize 
        self.width = tilesize
        self.height = tilesize

        # sets the image for the tree class by obtaining the top left coordinate of a pixel in reference to the inherited spritesheet 
        self.image = self.game.terrain_spritesheet.get_sprite(self.counter_x, self.counter_y, self.width, self.height)

        # every sprite has a rect which is its positioning; often referred to as the hitbox
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

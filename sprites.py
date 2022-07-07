'''
Richard Feng
ICS3U
June 2022
Spritesheet (access spritesheet file) file of the rpg game
'''

# importing pygame library to access pygame graphics
import pygame

# import the code from my own files; seperated in different files for organization purposes
from constants import *

# used [1] to obtain specific sprites from a spritesheet
class Spritesheet:
    '''
    This is a class for getting individual images from a spritesheet

    Attributes:
        file (png): the image file of the spritesheet

    Returns:
        the individual sprite obtained from the spritesheet
    '''

    def __init__(self, file):
        '''
        The constructor for Spritesheet class

        Parameters:
            file (png): the image file of the spritesheet

        '''

        # converting the spritesheet file to an image that pygame can work with
        self.sheet = pygame.image.load(file).convert()
 
    def get_sprite(self, x, y, width, height):
        '''
        The get_sprite method of the that actually gets the individual iamges from a spritesheet

        Parameters:
            x (int): x-coordinate on the spritesheet
            y (int): y-coordinate on the sprite sheet
            width (int): tilesize scaling
            height (int): tilesize scaling
        
        Returns:
            the individual sprite obtained from the spritesheet
        '''

        # getting the individual sprite 
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)

        return sprite
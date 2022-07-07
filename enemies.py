'''
Richard Feng
ICS3U
June 2022
Enemy sprite file of the rpg game
'''

# importing pygame library to access pygame graphics
import pygame as pg

# importing random library to access random types
import random as rd

# importing math library to access mathematical functions 
import math

# import the code from my own files; seperated in different files for organization purposes
from constants import *

class enemy(pg.sprite.Sprite):
    '''
    This is a class for creating the enemy sprite that will be what the user fights against
    
    Attributes:
        game (any): Access all the variables in the game class
        x (int): The x-coordinate to set where the enemy will appear on the screen
        y (int): The y-coordiante to set where the enemy will appear on the screen
    '''

    def __init__(self, game, x, y):
        '''
        The constructor for enemy class
        
        Attributes:
            game (any): Access all the variables in the game class
            x (int): The x-coordinate to set where the enemy will appear on the screen
            y (int): The y-coordiante to set where the enemy will appear on the screen
        '''

        # game class variable
        self.game = game

        # assign the player sprite to its respective layer
        self._layer = ENEMY_LAYER
        # player sprites are now a part of all_sprites and player groups
        self.groups = self.game.all_sprites, self.game.enemies
        # call the init method for the inherited class
        pg.sprite.Sprite.__init__(self, self.groups)

        # tile based game where each tile is 32 x 32 pixels; the coordinates will need scaling
        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize

        self.x_change = 0
        self.y_change = 0

        # sets the image for the enemy class by obtaining the top left coordinate of a pixel in reference to the inherited spritesheet
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height)
        
        # num variable gets assigned a random integer between 0 and 1 inclusive
        num = rd.randint(0,1)

        # gets assigned a random direction for where the player is facing
        self.facing = enemy_facing[num]
        self.animation_loop = 1
        self.movement_loop = 0

        # gets assigned a random integer between 3 and 6 inclusive
        self.max_travel = rd.randint(3,6)

        # every sprite has a rect which is its positioning; often referred to as the hitbox
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        '''
        The update method for enemy class that will continue to run in a while loop while the game runs

        Parameters:
            None
        ''' 

        # calling the movement and animate function
        self.movement()
        self.animate()

        # changing the hitbox positioning of the player
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0
    
    # used [1] for systematic movement
    def movement(self):
        '''
        The movement method that controls the systematic movement of the enemy class

        Parameters:
            None
        '''

        # checks the direction the npc is facing
        # if it is already facing up, the randomized movement will be vertical
        if(self.facing == "up"):
            # the npc will continue to move up until its reached the max travel distance which was predetermined
            self.y_change += enemy_speed
            self.movement_loop += 1
            if(self.movement_loop >= self.max_travel):
                # once its reached the max travel distance, it will make a 180 turn and switch the direction in which it faces
                self.facing = "down"
        
        if(self.facing == "down"):
            # the npc will continue to move up until its reached the max travel distance which was predetermined
            self.y_change -= enemy_speed
            self.movement_loop -= 1
            if(self.movement_loop <= -self.max_travel):
                # once its reached the max travel distance, it will make a 180 turn and switch the direction in which it faces
                self.facing = "up"

    # used [1] for animation
    def animate(self):
        '''
        The animate method that actually animates the enemy's movement to look more natural 

        Paramater:
            None
        '''

        # based on the coordinates of the spritesheet, accessing the specific frame for each corresponding animation
        down_animations = [self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(32, 0, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(64, 0, self.width, self.height)]

        left_animations = [self.game.enemy_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(32, 32, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(64, 32, self.width, self.height)]

        right_animations = [self.game.enemy_spritesheet.get_sprite(0, 64, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(32, 64, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(64, 64, self.width, self.height)]

        up_animations = [self.game.enemy_spritesheet.get_sprite(0, 98, self.width, self.height),
                         self.game.enemy_spritesheet.get_sprite(32, 98, self.width, self.height),
                         self.game.enemy_spritesheet.get_sprite(64, 98, self.width, self.height)]
        
        # actually taking the images collected from the spritesheet and actually animating it
        # not too sure how it works; I implemented the code from the tutorial
        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
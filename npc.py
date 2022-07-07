'''
Richard Feng
ICS3U
June 2022
Non-player character (player sprite interacts with to gain information) sprite file of the rpg game
'''

# importing pygame library to access pygame graphics
import pygame

# importing random library to access random types
import random

# importing math library to access mathematical functions
import math

# import the code from my own files; seperated in different files for organization purposes
from constants import *
from sprites import *

# the class 'npc' is defined and will embody all the code for the npc sprite
class npc(pygame.sprite.Sprite):
    '''
    This is a class for creating the npc sprite

    Attributes:
        game (any): Access all the variables in the game class
        x (int): The x-coordinate to set where the npc will appear on the screen
        y (int): The y-coordiante to set where the npc will appear on the screen
    '''

    def __init__(self, game, x, y):
        '''
        The constructor for npc class

        Parameters:
            game (any): Access all the variables in the game class
            x (int): The x-coordinate to set where the npc will appear on the screen
            y (int): The y-coordiante to set where the npc will appear on the screen
        '''

        # game class inheritance
        self.game = game

        
        # sets the layer on the screen where the npc will appear
        self._layer = npc_layer
        # npc sprites are now a part of the all_sprites and npc groups
        self.groups = self.game.all_sprites, self.game.npc
        # call the init method for the inherited class
        pygame.sprite.Sprite.__init__(self, self.groups)

        # tile based game where each tile is 32 x 32 pixels; the coordinates will need scaling
        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize

        self.x_change = 0
        self.y_change = 0

        # sets the image for the npc class by obtaining the top left coordinate of a pixel in reference to the inherited spritesheet
        self.image = self.game.npc_spritesheet.get_sprite(32, 0, self.width, self.height)

        # generates a random integer between 0 and 3 inclusive gets assigned to variable num
        num = random.randint(0,3)

        # gets assigned a random direction for where the npc is facing
        self.facing = npc_facing[num]
        # initialization
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = 64

        # every sprite has a rect which is its positioning; often referred to as the hitbox
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 

    def update(self):
        '''
        The update method for npc class

        Parameters:
            None
        '''

        # checks if the npc and player sprite have not collided
        if not(self.player_collision()):
            # call the movement and animate function
            self.movement()
            self.animate()

        # changing the hitbox positioning of the npc 
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    # used [1] for movement
    def movement(self):
        '''
        The movement method that controls the randomized movement of the npc class

        Parameters:
            None
        '''

        # checks the direction the npc is facing
        # if it is already facing up, the randomized movement will be vertical
        if(self.facing == "up"):
            # the npc will continue to move up until its reached the max travel distance which was predetermined
            self.y_change += npc_speed
            self.movement_loop += 1
            if(self.movement_loop >= self.max_travel):
                # once its reached the max travel distance, it will make a 180 turn and switch the direction in which it faces
                self.facing = "down"
        
        # if it is already facing down, the randomized movement will be vertical
        if(self.facing == "down"):
            # the npc will continue to move down until its reached the max travel distance which was predetermined
            self.y_change -= npc_speed
            self.movement_loop -= 1
            if(self.movement_loop <= -self.max_travel):
                # once its reached the max travel distance, it will make a 180 turn and switch the direction in which it faces
                self.facing = "up"
        
        # if it is already facing left, the randomized movement will be horizantal
        if(self.facing == "left"):
            # the npc will continue to move left until its reached the max travel distance which was predetermined
            self.x_change -= npc_speed
            self.movement_loop -= 1
            if(self.movement_loop <= -self.max_travel):
                # once its reached the max travel distance, it will make a 180 turn and switch the direction in which it faces
                self.facing = "right"
        
        # if it is already facing right, the randomized movement will be horizantal
        if(self.facing == "right"):
            # the npc will continue to move right until its reached the max travel distance which was predetermined
            self.x_change += npc_speed
            self.movement_loop += 1
            if(self.movement_loop >= self.max_travel):
                # once its reached the max travel distance, it will make a 180 turn and switch the direction in which it faces
                self.facing = "left"
    
    # used [1] for animation
    def animate(self):
        '''
        The animate method that actually animates the npc's movement to look more natural 

        Paramater:
            None
        '''

        # based on the coordinates of the spritesheet, accessing the specific frame for each corresponding animation
        up_animations = [self.game.npc_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.npc_spritesheet.get_sprite(32, 0, self.width, self.height),
                           self.game.npc_spritesheet.get_sprite(64, 0, self.width, self.height)]

        left_animations = [self.game.npc_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.npc_spritesheet.get_sprite(32, 32, self.width, self.height),
                           self.game.npc_spritesheet.get_sprite(64, 32, self.width, self.height)]

        right_animations = [self.game.npc_spritesheet.get_sprite(0, 64, self.width, self.height),
                            self.game.npc_spritesheet.get_sprite(32, 64, self.width, self.height),
                            self.game.npc_spritesheet.get_sprite(64, 64, self.width, self.height)]

        down_animations = [self.game.npc_spritesheet.get_sprite(0, 98, self.width, self.height),
                         self.game.npc_spritesheet.get_sprite(32, 98, self.width, self.height),
                         self.game.npc_spritesheet.get_sprite(64, 98, self.width, self.height)]
        
        # actually taking the images collected from the spritesheet and actually animating it
        # not too sure how it works; I implemented the code from the tutorial
        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.npc_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.npc_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.npc_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.npc_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

    def player_collision(self):
        '''
        Checking for if the npc collides with the player sprite

        Paramaters:
            None

        Returns:
            boolean value of True when the player collides
        '''

        # assigns a boolean value to 'hits' based on whether or not the two sprites collided
        hits = pygame.sprite.spritecollide(self, self.game.player_1, False)
        # if they did collide
        if hits:
            '''
            # blit the dialogue image onto the game screen
            self.game.screen.blit(self.game.dialogue, (20, 20))
            # python function to update the screen
            pygame.display.update()
            '''
            
            return hits
    

                    
                    


                    


        



            
        
        
            
            
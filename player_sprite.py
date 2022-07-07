'''
Richard Feng
ICS3U
June 2022
Player sprite (character the user plays as) file of the rpg game
'''

# importing pygame library to access pygame graphics
import pygame

# importing system library to access system types
import sys

# importing math library to access mathematical functions
import math

# import the code from my own files; seperated in different files for organization purposes
from constants import *

# the class 'Player' is defined and will embody all the code for the Player sprite
class Player(pygame.sprite.Sprite):
    '''
    This is a class for creating the Player sprite that will be what the user controls on the screen
    
    Attributes:
        game (any): Access all the variables in the game class
        x (int): The x-coordinate to set where the Player will appear on the screen
        y (int): The y-coordiante to set where the Player will appear on the screen
    '''

    def __init__(self, game, x, y):
        '''
        The constructor for Player class

        Parameters:
            game (any): Access all the variables in the game class
            x (int): The x-coordinate to set where the Player will appear on the screen
            y (int): The y-coordiante to set where the Player will appear on the screen
        '''

        # game class variable
        self.game = game

        # assign the player sprite to its respective layer
        self._layer = PLAYER_LAYER
        # player sprites are now a part of all_sprites and player groups
        self.groups = self.game.all_sprites, self.game.player_1
        # call the init method for the inherited class
        pygame.sprite.Sprite.__init__(self, self.groups)

        # tile based game where each tile is 32 x 32 pixels; the coordinates will need scaling
        self.x = x * tilesize
        self.y = y * tilesize 
        self.width = tilesize
        self.height = tilesize

        self.x_change = 0
        self.y_change = 0

        # gets assigned a direction for where the player is facing
        self.facing = 'down'
        self.animation_loop = 1

        # sets the image for the player class by obtaining the top left coordinate of a pixel in reference to the inherited spritesheet
        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
        
        # every sprite has a rect which is its positioning; often referred to as the hitbox
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        '''
        The update method for player class that will continue to run in a while loop while the game runs

        Parameters:
            None
        '''

        # calling the movement, animate, enemy_collision, portal_colision, and collid_blocks function
        self.movement()
        self.animate()
        self.enemy_collision()
        self.portal_collision()
        # changing the hitbox positioning of the player
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0

    # used [1] for movement and centering the camera on player
    def movement(self):
        '''
        The movement method that controls the controlled movement of the player class

        Parameters:
            None
        '''

        # assigning the variable keys to the key that was pressed on the keyboard
        keys = pygame.key.get_pressed()

        # checks which direction the user desires to move and make the move accoringly
        # along with the movement of the player sprite, all sprites move with the player sprite for a camera centered on the player
        if keys[pygame.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += player_speed
            self.x_change -= player_speed
            self.facing = 'left'

        if keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= player_speed

            self.x_change += player_speed
            self.facing = 'right'

        if keys[pygame.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += player_speed
            self.y_change -= player_speed
            self.facing = 'up'

        if keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= player_speed

            self.y_change += player_speed
            self.facing = 'down'
    
    # used [1] for block collision
    def collide_blocks(self, direction):
        '''
        The collide_blocks method that determines whether or not the player collided with blocks that aren't meant to be passed through

        Parameter:
            direction (char): x or y axis 
        '''

        # if the player sprite is traveling along the x-axis
        if direction == "x":
            # assigns a boolean value to 'hits' based on whether or not the two sprites collided 
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            # if they did collide
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += player_speed
                
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= player_speed

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += player_speed

                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= player_speed
    
    def enemy_collision(self):
        '''
        The enemy_collision method that checks whether or not the enemy collided with the player

        Parameters:
            None
        '''

        # assigns a boolean value to 'hits' based on whether or not the two sprites collided
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        # if they did collide
        if hits:
            # if they collide, the player will be killed and will exit the system
            self.kill()
            self.game.game_over()
            pygame.quit()
       
    def portal_collision(self):
        '''
        The portal_collision method that checks whether or not the player and portal collided

        Parameters:
            None
        '''

        # assigns a boolean value to 'hits' based on whether or not the two sprites collided 
        hits = pygame.sprite.spritecollide(self, self.game.portal, False)
        # if they did collide
        if hits:
            # teleport the player sprite to the following coordinate
            self.rect.topleft = (800, 200)

    # used [1] to animate a moving sprite
    def animate(self):
        '''
        The animate method that actually animates the npc's movement to look more natural 

        Paramater:
            None
        '''

        # based on the coordinates of the spritesheet, accessing the specific frame for each corresponding animation
        down_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 0, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 32, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 32, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(32, 64, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(64, 64, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(0, 98, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(32, 98, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(64, 98, self.width, self.height)]
        
        # actually taking the images collected from the spritesheet and actually animating it
        # not too sure how it works; I implemented the code from the tutorial
        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

# used [1] to create an attack class      
class Attack(pygame.sprite.Sprite):
    '''
    This is a class for creating the player sprite's ability to attack

    Attributes:
        game (any): Access all the variables in the game class
        x (int): The x-coordinate to set where the attack will appear on the screen
        y (int): The y-coordiante to set where the attack will appear on the screen
    '''

    def __init__(self, game, x, y):
        '''
        The constructor for the attack class

        Parameter:
            game (any): Access all the variables in the game class
            x (int): The x-coordinate to set where the attack will appear on the screen
            y (int): The y-coordiante to set where the attack will appear on the screen
        '''

        # game class inheritance
        self.game = game
        # sets the layer on the screen where the player will appear
        self._layer = PLAYER_LAYER
        # player sprites are now a part of all_sprites and player groups
        self.groups = self.game.all_sprites, self.game.attacks
        # call the init method for the inherited class
        pygame.sprite.Sprite.__init__(self, self.groups)

        # tile based game where each tile is 32 x 32 pixels; the coordinates will need scaling
        self.x = x
        self.y = y
        self.width = tilesize
        self.height = tilesize

        self.animation_loop = 0
        # sets the image for the player class by obtaining the top left coordinate of a pixel in reference to the inherited spritesheet
        self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height)

        # every sprite has a rect which is its positioning; often referred to as the hitbox
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        '''
        The update method for player class 

        Parameters:
            None
        '''

        # call the animate and enemy_collision function
        self.animate()
        self.enemy_collision()

    def enemy_collision(self):
        '''
        The enemy_collision method to see if the player and the enemy collided

        Parameters:
            None
        
        Returns:
            None
        '''

        # assigns a boolean value to 'hits' based on whether or not the two sprites collided 
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
    
    def animate(self):
        '''
        The animate method that actually animates the npc's movement to look more natural 

        Paramater:
            None
        
        Returns:
            None
        '''

        # assigns the direction the player is facing
        direction = self.game.player.facing

        # based on the coordinates of the spritesheet, accessing the specific frame for each corresponding animation
        right_animations = [self.game.attack_spritesheet.get_sprite(0, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 64, self.width, self.height)]

        down_animations = [self.game.attack_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 32, self.width, self.height)]

        left_animations = [self.game.attack_spritesheet.get_sprite(0, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 96, self.width, self.height)]

        up_animations = [self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height)]
        
        # actually taking the images collected from the spritesheet and actually animating it
        # not too sure how it works; I implemented the code from the tutorial
        if(direction == 'up'):
            self.image = up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        
        if(direction == 'down'):
            self.image = down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()

        if(direction == 'left'):
            self.image = left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()

        if(direction == 'right'):
            self.image = right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
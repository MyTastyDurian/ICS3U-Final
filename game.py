'''
Richard Feng
ICS3U
May 2022
Main file of the rpg game
'''

# importing pygame library to access pygame graphics
import pygame

# initializing pygame font
pygame.font.init()

# import the code from my own files; seperated in different files for organization purposes
from sprites import *
from constants import *
from player_sprite import *
from block_sprite import *
from ground_sprite import *
from enemies import *
from portal import *
from npc import *
from tree import *
from npc_2 import *

# the class 'Game' is defined and will emobdy all the code
# for setting up the pygame system, I used [1] and [2]
class Game:
    '''
    This is a class for creating the game that will embody all the code
    
    Attributes:
        None
    '''

    def __init__(self):
        '''
        The constructor for Player class

        Parameters:
            None
        '''
        # initializing a function in pygame that allows use of pygame
        pygame.init()

        # creating the game window screen with dimensions (in pixels) found in constants
        self.screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('ICS3U Final')

        # creating a blackbackground
        self.background = pygame.display.set_mode((1280, 960))

        # assigning font
        self.main_font = pygame.font.SysFont("comicsans", 50)
        self.text_font = pygame.font.SysFont("comicsans", 20)     

        # a clock object that allows frame rate setup
        self.clock = pygame.time.Clock()

        # ensures code is running and can only be closed manually
        self.running = True

        # assigning to global variable
        self.attacks_used = attacks_used

        # creates chracter spritesheet to access a wide variety of graphics
        # otherwise, loading each individual image would slow the program down significantly
        self.character_spritesheet = Spritesheet('ICS3U - Final/images/pipo-nekonin015.png')
        self.terrain_spritesheet = Spritesheet('ICS3U - Final/images/ground.png')
        self.enemy_spritesheet = Spritesheet('ICS3U - Final/images/pipo-nekonin020.png')
        self.portal_spritesheet = Spritesheet('ICS3U - Final/images/portal_2.png')
        self.npc_spritesheet = Spritesheet('ICS3U - Final/images/pipo-nekonin018.png')
        self.npc_2_spritesheet = Spritesheet('ICS3U - Final/Images/pipo-nekonin019.png')
        self.attack_spritesheet = Spritesheet('ICS3U - Final/images/attack.png')

        self.dialogue = pygame.image.load('ICS3U - Final/images/dialoguebox.png')
    
    # for creating the tilemap I used [1]
    def createTilemap(self):
        '''
        createTilemap method goes through the tilemap made manually on constants file; the enumerate for loop allows access to the count and the value (essentially having counter for each iterable)

        Parameters:
            None
        
        Returns:
            None
        '''

        # initializing counter variables
        self.counter = 0
        self.counter_2 = 0

        # going through each row and column of the tile map row by row; enumerate essentially obtains a counter and the variable itself
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):

                # goes through each column in the map (entire map), calls the ground function—replaces each character with a grass tile for the ground
                Ground(self, j, i)

                # when manually creating the tile map, B is intentially used to represent walls that possess collision detection

                if column == "B":
                    # Block class when the letter B is present
                    Block(self, j, i)

                # P represents the player spawn location
                if column == "P":
                    # Player class spawning the player—replacing the character P
                    self.player = Player(self, j, i)

                if column == "E":
                    # an enemy class
                    enemy(self, j, i)
                
                # portal class
                # manually adjusting coordinates of the spritesheet
                if column == "X":
                    if(self.counter == 0):
                        portal(self, j, i, 0, 0)
                    elif(self.counter == 1):
                        portal(self, j, i, 1, 0)                   
                    elif(self.counter == 2):
                        portal(self, j, i, 0, 1)                  
                    elif(self.counter == 3):
                        portal(self, j, i, 1, 1)                   
                    elif(self.counter == 4):
                        portal(self, j, i, 0, 2)                  
                    elif(self.counter == 5):
                        portal(self, j, i, 1, 2)

                    # counter increment to switch to different tiles               
                    self.counter += 1
                
                # tree class
                # manually adjusting coordinates of the spritesheet
                if column == "T":
                    if(self.counter_2 > 3):
                        self.counter_2 -= 4
                    if(self.counter_2 == 0):
                        trees(self, j, i, 0, 1)
                    elif(self.counter_2 == 1):
                        trees(self, j, i, 1, 1)                   
                    elif(self.counter_2 == 2):
                        trees(self, j, i, 0, 2)                  
                    elif(self.counter_2 == 3):
                        trees(self, j, i, 1, 2) 
                    
                     # counter increment to switch to different tiles 
                    self.counter_2 += 1
                
                # npc class
                if column == "N":
                    npc(self, j, i)
                
                # npc class #2
                if column == "O":
                    npc_2(self, j, i)
    
    def new(self):
        '''
        The new method is created for when a new game starts

        Parameters:
            None
        
        Return:
            None
        '''

        # check the status of the player (died or quit)
        self.playing = True

        # setup for a group of sprites
        # object that will contain all the sprites in the game
        self.all_sprites = pygame.sprite.LayeredUpdates()

        # storage of all the blocks includign terrain
        self.blocks = pygame.sprite.LayeredUpdates()

        # storage of all the enemies in the game
        self.enemies = pygame.sprite.LayeredUpdates()

        # storage of the portal in the game
        self.portal = pygame.sprite.LayeredUpdates()

        # storage of all the attack sprites 
        self.attacks = pygame.sprite.LayeredUpdates()

        # storage of the first npc
        self.npc = pygame.sprite.LayeredUpdates()

        # storage of the second npc
        self.npc_2 = pygame.sprite.LayeredUpdates()

        # storage of the player sprite
        self.player_1 = pygame.sprite.LayeredUpdates()

        # calling the tilemap to create it
        self.createTilemap()
        
    def events(self):
        '''
        The events method that contains all keyboard interacton by the user

        Parameters:
            None
        
        Returns:
            None
        ''' 

        # for loop to iterate through all the events in pygame 
        for event in pygame.event.get():

            # if user ever closes the program at the top right
            if event.type == pygame.QUIT:

                # then program will stop playing and running
                self.playing = False
                self.running = False
            
            # checks if the user pressed their mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # depending on which way their facing, adjust the attack accordingly
                # attacks_used increment updates on screen
                if self.player.facing == 'up':
                    Attack(self, self.player.rect.x, self.player.rect.y - tilesize)
                    self.attacks_used += 1


                if self.player.facing == 'down':
                    Attack(self, self.player.rect.x, self.player.rect.y + tilesize)
                    self.attacks_used += 1


                if self.player.facing == 'left':
                    Attack(self, self.player.rect.x - tilesize, self.player.rect.y ) 
                    self.attacks_used += 1

                if self.player.facing == 'right':
                    Attack(self, self.player.rect.x + tilesize, self.player.rect.y - tilesize) 
                    self.attacks_used += 1
                                    
    def update(self):
        '''
        The update method constantly updates the game so it is not a static image

        Parameters:
            None
        
        Returns:
            None
        '''

        # sprite group containing all the sprites then find the update method in every single sprite and run the update method
        self.all_sprites.update()
            
    
    def draw(self):
        '''
        The draw method will display all the sprites onto the screen

        Parameters:
            None
        
        Returns:
            None
        '''

        # black background
        self.screen.fill("Black")
        # goes through every single sprite in the group, finds the image, and subequently finds the rectangle that is created for each sprite then draws it 
        self.all_sprites.draw(self.screen)

        # update attacks used
        self.attacks_label = self.main_font.render(f"Attacks used: {self.attacks_used}", 1, (255, 255, 255))

        # blit all the text dialogues at the bottom
        self.screen.blit(self.attacks_label, (10, 10))
        self.screen.blit(self.dialogue, (250, 520))
        self.screen.blit(self.dialogue, (250, 660))
        self.screen.blit(self.dialogue, (250, 800))

        # blit all the image sprites for visual aid
        self.screen.blit(self.character_spritesheet.get_sprite(0, 0, 32, 32), (990, 600))
        self.screen.blit(self.enemy_spritesheet.get_sprite(0, 0, 32, 32), (990, 650))
        self.screen.blit(self.attack_spritesheet.get_sprite(0, 0, 32, 32), (990, 700))
        self.screen.blit(self.npc_spritesheet.get_sprite(32, 0, 32, 32), (990, 750))
        self.screen.blit(self.portal_spritesheet.get_sprite(0, 0, 64, 96), (970, 800))
        self.screen.blit(self.npc_2_spritesheet.get_sprite(32, 0, 32, 32), (930, 850))
        
        # blit the game instructions
        self.instructions_label = self.text_font.render("1. Move player character using W[forward], A[left], S[right], D[down].", 1, (0, 0, 0))
        self.screen.blit(self.instructions_label, (275, 600))

        self.instructions_2_label = self.text_font.render("2. If you collide with enemy characters, you die.", 1, (0, 0, 0))
        self.screen.blit(self.instructions_2_label, (275, 650))

        self.instructions_3_label = self.text_font.render("3. Approach enemy characters and left-click with mouse to kill.", 1, (0, 0, 0))
        self.screen.blit(self.instructions_3_label, (275, 700))

        self.instructions_4_label = self.text_font.render("4. NPC collision will stop movement and dialogue will appear (commented out).", 1, (0, 0, 0))
        self.screen.blit(self.instructions_4_label, (275, 750))

        self.instructions_5_label = self.text_font.render("5. Use teleporter to move to the next stage.", 1, (0, 0, 0))
        self.screen.blit(self.instructions_5_label, (275, 800))

        self.instructions_6_label = self.text_font.render("6. Collide/interact with this specific NPC to win the game.", 1, (0, 0, 0))
        self.screen.blit(self.instructions_6_label, (275, 850))

        self.instructions_7_label = self.text_font.render("Good Luck!", 1, (0, 0, 0))
        self.screen.blit(self.instructions_7_label, (window_width/2 - self.instructions_7_label.get_width()/2, 900))

        self.instructions_8_label = self.text_font.render("Game Instructions:", 1, (0, 0, 0))
        self.screen.blit(self.instructions_8_label, (window_width/2 - self.instructions_7_label.get_width()/2, 550))
        
        # pass in the constant FPS which is at 60 frames per second
        self.clock.tick(FPS)

        # pygame function to update the screen
        pygame.display.update()
    
    def main(self):
        '''
        The main method is a game loop will be executed when user is still playing

        Parameters:
            None
        
        Return:
            None
        '''

        # while user is playing
        while self.playing:
            # events method will be called, then update, then draw
            self.events()
            self.update()
            self.draw()

        # once the user stops playing, it will stop running
        self.running = False
    
    # used [2] for the intro and outro screens
    def main_menu(self):
        '''
        The main_menu method creates the intro screen

        Parameters:
            None
        
        Return:
            None
        '''

        # assigning font
        title_font = pygame.font.SysFont("corbel", 70)
        run = True

        # runs until they exit out
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False 

            self.screen.blit(self.background, (0,0))
            # creating the text labels
            title_label = title_font.render("Welcome to Ubiquitous Sprites!", 1, (255, 255, 255))
            title_label_2 = title_font.render("A RPG Game", 1, (255, 255, 255))
            title_label_3 = title_font.render("ICS3U Final by Richard F.", 1, (255, 255, 255))
            title_label_4 = title_font.render("Click Anywhere on the Screen to Start...", 1, (255, 255, 255))
            # blit the introduction text, centering each one
            self.screen.blit(title_label, (window_width/2 - title_label.get_width()/2, 150))
            self.screen.blit(title_label_2, (window_width/2 - title_label_2.get_width()/2, 300))
            self.screen.blit(title_label_3, (window_width/2 - title_label_3.get_width()/2, 450))
            self.screen.blit(title_label_4, (window_width/2 - title_label_4.get_width()/2, 600))
            # pygame function to update the screen
            pygame.display.update()
    
    def game_over(self):
        '''
        The game_over method that is the end screen when the user dies

        Parameters:
            None
        
        Returns:
            None
        '''

        # assigning font
        title_font = pygame.font.SysFont("corbel", 70)
        run = True

        # runs until user leaves
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                    self.running = False

            # black background
            self.screen.fill("Black")
            self.screen.blit(self.background, (0,0))
            # creating the text, then bliting in the center of the screen
            title_label = title_font.render("Game Over!", 1, (255, 255, 255))
            self.screen.blit(title_label, (window_width/2 - title_label.get_width()/2, 300))
            title_label_2 = title_font.render("The Enemy Killed You!", 1, (255, 255, 255))
            self.screen.blit(title_label_2, (window_width/2 - title_label_2.get_width()/2, 450))
            # pygame function to update the screen
            pygame.display.update()
    
    def congratulations(self):
        '''
        The congratulations method that is the end screen when the user wins

        Parameters:
            None
        
        Returns:
            None
        '''

        title_font = pygame.font.SysFont("corbel", 70)
        run = True
        # runs until user leaves
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                    self.running = False

            # black background
            self.screen.fill("Black")
            self.screen.blit(self.background, (0,0))
             # creating the text, then bliting in the center of the screen
            title_label = title_font.render("Congratulations!", 1, (255, 255, 255))
            self.screen.blit(title_label, (window_width/2 - title_label.get_width()/2, 300))
            title_label_2 = title_font.render("You Won!", 1, (255, 255, 255))
            self.screen.blit(title_label_2, (window_width/2 - title_label_2.get_width()/2, 450))
            # pygame function to update the screen
            pygame.display.update()
'''
Richard Feng
ICS3U
May 2022
Driver code of the rpg game
'''

# importing pygame library to access pygame graphics
import pygame

# importing system library to access system typesdd
import sys

# import the code from my own files; seperated in different files for organization purposes
from sprites import *
from constants import *
from game import *
from enemies import *
from npc import *

# main driver code to call the class instance
if __name__ == "__main__": 
    # creating class instance
    rpg_game = Game()
    
    # calling intro screen
    rpg_game.main_menu()
    # new function is called everytime a new game starts
    rpg_game.new()

    # while the game is running
    while rpg_game.running:
        # execute the main function
        rpg_game.main()
    
    # quits pygame and exists the system
    pygame.quit()
    sys.exit()

'''
Reference List:
[1] Pygame RPG Tutorials. YouTube, 2021. Available: https://youtube.com/playlist?list=PLkkm3wcQHjT7gn81Wn-e78cAyhwBW3FIc [Accessed: 06-June-2022]
[2] Pygame Tutorial - Creating Space Invaders. YouTube, 2020. Available: https://www.youtube.com/watch?v=Q-__8Xw9KTM&t=1585s [Accessed: 06-June-2022]
'''
'''
Richard Feng
ICS3U
May 2022
Constants file to store all the constants or global variables used to allow easier change
'''

# game window screen denoted in pixels
window_width = 1280
window_height = 1000

# each tile is 32 x 32 pixels (scale)
tilesize = 32

width = 32
height = 32

# each individual layer of sprites (terrain, blocks, and player itself)
ground_layer = 1 
block_layer = 2
portal_layer = 2
tree_layer = 2
ENEMY_LAYER = 3
npc_layer = 3
PLAYER_LAYER = 4

# sprite facing direction 
# npc moving direction is randomized by choosing on of these options in the list
enemy_facing = ['up', 'down']
npc_facing = ['up', 'down', 'left', 'right']

# sprite speed
player_speed = 5
enemy_speed = 2
npc_speed = 1

# light shade of the button
color_light = (170,170,170)

# RGB colour of black
BLACK = (0, 0, 0)


# tilemap made manually in constants as tiled map editor was taking too long to figure how to implement
# B represents walls or blocks that possess collision detection
# . represents the terrain or ground
# P represents the players spawn location
# T represents the trees 
# X represents the portal
# N nad O represents non-player characters
# E represents enemies
tilemap = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B..TT......................................................B',
    'B..TT......................................................B',
    'BTT...........O............................................B',
    'BTT........................................................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB..BBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'BTT...............................................E........B',
    'BTT...........................EE.....................E.....B',
    'B..TT.............................................E..E.....B',
    'B..TT........N.......................................E.....B',
    'BTT...............................................EE.......B',
    'BTT.................................................E......B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'BTT...........P......E.......XX............................B',
    'BTT.................E..E.....XX............................B',
    'B..TT....N...................XX............................B',
    'B..TT...........E.........E..E...E.......E.................B',
    'BTT..................E..............E......................B',
    'BTT........................................................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]


# frame rate 
FPS = 60

# the number of enemies will be displayed on the screen
attacks_used = 0




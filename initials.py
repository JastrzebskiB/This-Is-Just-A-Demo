import pygame
import os
from pygame.locals import *

#start pygame
pygame.init()

#declare display variables
screen_width = 800
screen_height = 600
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Just A Demo (not the best game in the world)")
icon = pygame.image.load(os.path.join("png", "icon_32.png")).convert()
pygame.display.set_icon(icon)

#declare colour constants
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SUBTITLE_YELLOW = (250, 250, 60)
UGRAY = (160, 160, 100)
URED = (255, 0, 55)

#miscellaneous
smallfont = pygame.font.SysFont("Courier", 14, True, True)
font = pygame.font.SysFont("Courier", 16, True, True)
largefont = pygame.font.SysFont("Courier", 24, True, True)

#units and armies initialised in character.py
#map and hero initialised in map.py

"""A proof of concept for the future mobile/mulitplatform game with the combat
system similar to the one in Disciples series.
Blazej Jastrzebski"""

#general imports
import pygame
from pygame.locals import *
from sys import *
from random import *

#game specific libraries
from tile import *
from text import *
from map import *
from battle import *
from showonce import *
from character import *
from charsheet import *
from initials import *


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit("Closed in main.")

        firstmap.play_map(hero)

intro(screen)
tutorial(screen, army, tutarmy, hero, "bg_tutorial.png")
main()

#battle(screen, army, testarmy, hero, "bg_beach.png", BLACK)

#we"re IDLE friendly
pygame.quit()

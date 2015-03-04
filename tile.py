#imports
from sys import *
import pygame
from text import *
from battle import *
from pygame.locals import *
from initials import *

#declare tile characteristics
tile_width = 40
tile_height = 40

class Tile(pygame.sprite.Sprite):


    """Main class for everything that will be displayed on the map module."""    
    # str, int, int, [int, int], bool, bool, image
    def __init__(self, name, width, height, pos, block, action, image):
        self.name = name
        self.width = width
        self.height = height
        self.pos = pos
        self.block = block
        self.action = action
        self.image = pygame.image.load(os.path.join("png", image))
        self.rect = self.image.get_rect()
        
        self.rect.left = pos[0]
        self.rect.right = pos[0] + tile_width
        self.rect.top = pos[1]
        self.rect.bottom = pos[1] + tile_height
        
    def get_name(self):
        return self.name
    
    #returns whether hero can pass the tile or not
    def get_block(self):
        return self.block
        
    #returns special interactions between hero and tile      
    def get_action(self):
        return self.action

    def show_tile(self):
        screen.blit(self.image, self.rect)

    #if self.action, logic for actual event
    def act(self, hero, mapobj):
        pass
    

#below are subclasses for special\action tiles
#first battle with rogues
class T28(Tile):

    def act(self, hero, mapobj):      
        if army_alive(AIarmy):
            if (hero.get_realbottom() > self.rect.top) and\
                   (hero.get_realtop() < self.rect.bottom) and\
                   (hero.get_realleft() < self.rect.right) and\
                   (hero.get_realright() > self.rect.left):
                #does not proc multiple times since enemy army dies
                battle(screen, army, AIarmy, hero, "bg_beach.png", BLACK)
                mapobj.fought_battle(0)
            

#second battle with rogues
class T33(Tile):

    def act(self, hero, mapobj):    
        if army_alive(AIarmy2):
            if (hero.get_realbottom() > self.rect.top) and\
                   (hero.get_realtop() < self.rect.bottom) and\
                   (hero.get_realleft() < self.rect.right) and\
                   (hero.get_realright() > self.rect.left):
                #does not proc multiple times since enemy army dies
                battle(screen, army, AIarmy2, hero, "bg_beach.png", BLACK)
                mapobj.fought_battle(1)


#entrance to castle
class T52(Tile):

    def __init__(self, name, width, height, pos, block, action, image):
        Tile.__init__(self, name, width, height, pos, block, action, image)
        self.talkername = "KING"
        self.text1 = "The fishermen near the lake have more  "+\
                "information about the vagrants on the  "+\
                "coast."
        self.text2 = "We received information of something   "+\
                "suspicious going on at the lumber mill."+\
                "This needs to be investigated urgently."
        self.text3 = "Good job! You have done splendidly!    "+\
                "Still, I am afraid even more dire times"+\
                "might come upon us. Be ready for the   "+\
                "next summons, my boy."
    
    #different interactions depending on state of the game/map
    def act(self, hero, mapobj):
        if (hero.get_realbottom() > self.rect.top) and\
               (hero.get_realtop() < self.rect.bottom) and\
               (hero.get_realleft() < self.rect.right) and\
               (hero.get_realright() > self.rect.left):                        
            if (not mapobj.get_battle(0)) or (not mapobj.get_battle(1)):
                show_textbox(self.talkername, self.text1, "talker_king.png")
            if (mapobj.get_battle(0) and mapobj.get_battle(1)) and\
                    (not mapobj.get_battle(2)):
                show_textbox(self.talkername, self.text2, "talker_king.png")
            if mapobj.get_battle(0) and mapobj.get_battle(1) and\
                    mapobj.get_battle(2):
                show_textbox(self.talkername, self.text3, "talker_king.png")
                pygame.display.update()
                pygame.time.wait(5000)
                exit()


#house of Master-At-Arms; later will be used to train units" skills
class T81(Tile):

    def __init__(self, name, width, height, pos, block, action, image):
        Tile.__init__(self, name, width, height, pos, block, action, image)
        self.talkername = "MASTER-AT-ARMS"
        self.text1 = "We shall talk about your training when "+\
                "you are done running the KING'S errand,"+\
                "boy."
        self.text2 = "There have been some new developments. "+\
                "Go speak with the KING immediately!"
        self.text3 = "You have done well! You should go talk "+\
                "to the KING, boy."
    
    #different interactions depending on state of game/map    
    def act(self, hero, mapobj):
        if (hero.get_realbottom() > self.rect.top) and\
               (hero.get_realtop() < self.rect.bottom) and\
               (hero.get_realleft() < self.rect.right) and\
               (hero.get_realright() > self.rect.left):
            if (not mapobj.get_battle(0)) or (not mapobj.get_battle(1)):
                show_textbox(self.talkername, self.text1, "talker_maa.png")
            if (mapobj.get_battle(0) and mapobj.get_battle(1)) and\
                    (not mapobj.get_battle(2)):
                show_textbox(self.talkername, self.text2, "talker_maa.png")
            if mapobj.get_battle(0) and mapobj.get_battle(1) and\
                    mapobj.get_battle(2):
                show_textbox(self.talkername, self.text3, "talker_maa.png")


#house of Blacksmith; later will be used to buy/sell some basic items
class T83(Tile):

    def __init__(self, name, width, height, pos, block, action, image):
        Tile.__init__(self, name, width, height, pos, block, action, image)
        self.talkername = "BLACKSMITH"
        self.text = "Sorry, we are waiting for the materials"+\
                "to arrive..."
        
    def act(self, hero, mapobj):
        if (hero.get_realbottom() > self.rect.top) and\
               (hero.get_realtop() < self.rect.bottom) and\
               (hero.get_realleft() < self.rect.right) and\
               (hero.get_realright() > self.rect.left):
            show_textbox(self.talkername, self.text, "talker_blacksmith.png")


#fishermen
class T134(Tile):

    def __init__(self, name, width, height, pos, block, action, image):
        Tile.__init__(self, name, width, height, pos, block, action, image)
        self.talkername = "FISHER"
        self.text1 = "The bandits have been causing problems "+\
                "on the coast. We cannot go fishing in  "+\
                "the sea. Please do something!"
        self.text2 = "Sire, there is still one bandit group  "+\
                "on the other beach."
        self.text3 = "Thank you so much for clearing the     "+\
                "coast for us!"
        
    #different interactions depending on state of game/map
    def act(self, hero, mapobj):
        if (hero.get_realbottom() > self.rect.top) and\
               (hero.get_realtop() < self.rect.bottom) and\
               (hero.get_realleft() < self.rect.right) and\
               (hero.get_realright() > self.rect.left):
            if (not mapobj.get_battle(0)) and (not mapobj.get_battle(1)):
                show_textbox(self.talkername, self.text1, "talker_fisher.png")
            elif (mapobj.get_battle(0) or mapobj.get_battle(1)) and not\
                    (mapobj.get_battle(0) and mapobj.get_battle(1)):
                show_textbox(self.talkername, self.text2, "talker_fisher.png")
            elif mapobj.get_battle(0) and mapobj.get_battle(1):
                show_textbox(self.talkername, self.text3, "talker_fisher.png")


#lumber mill
class T229(Tile):

    def __init__(self, name, width, height, pos, block, action, image):
        Tile.__init__(self, name, width, height, pos, block, action, image)
        self.talkername1 = "LUMBERJACK"
        self.talkername2 = "ENEMY SOLDIER"
        self.talkername3 = None
        self.text1 = "No, sire. Everything going on as usual." 
        self.text2 = "So you have found our hideout...       "+\
                "Doesn't matter! You won't live to tell "+\
                "the tale!"
        self.text3 = "The lumber mill is empty after you have"+\
                "fended off the enemy soldiers."    
    
    #different interactions depending on state of game/map
    def act(self, hero, mapobj):
        if (hero.get_realbottom() > self.rect.top) and\
               (hero.get_realtop() < self.rect.bottom) and\
               (hero.get_realleft() < self.rect.right) and\
               (hero.get_realright() > self.rect.left):
            if (not mapobj.get_battle(0)) or (not mapobj.get_battle(1)):
                show_textbox(self.talkername1, self.text1,\
                            "talker_lumberjack.png")
            if mapobj.get_battle(0) and mapobj.get_battle(1) and\
                    (not mapobj.get_battle(2)):
                show_textbox(self.talkername2, self.text2,\
                            "talker_aifighter.png")
                pygame.display.update()
                pygame.time.wait(2500)
                battle(screen, army, AIarmy3, hero, "bg_forest.png")
                mapobj.fought_battle(2)
            if mapobj.get_battle(2):
                show_textbox(self.talkername3, self.text3)


#future place to transition to second map
class T295(Tile):

    def __init__(self, name, width, height, pos, block, action, image):
        Tile.__init__(self, name, width, height, pos, block, action, image)
        self.talkername = "HEALER"
        self.text = "We should finish the KING'S errand     "+\
                "before moving to explore further, sire."
        
    def act(self, hero, mapobj):
        if (hero.get_realbottom() > self.rect.top) and\
               (hero.get_realtop() < self.rect.bottom) and\
               (hero.get_realleft() < self.rect.right) and\
               (hero.get_realright() > self.rect.left):
            show_textbox(self.talkername, self.text, "talker_healer.png")


#hero class; the tile that will be moved on the map
class Hero(Tile):

    def __init__(self, width, height, pos, block, image1, image2):
        self.width = width
        self.height = height
        self.pos = pos
        self.block = block
        self.imageleft = pygame.image.load(os.path.join("png", image1))
        self.imageleft.set_colorkey(WHITE)
        self.imageright = pygame.image.load(os.path.join("png", image2))
        self.imageright.set_colorkey(WHITE)
        self.image = self.imageright
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.right = pos[0] + tile_width
        self.rect.top = pos[1]
        self.rect.bottom = pos[1] + tile_height
        self.offset = 10

        #movement related
        self.speed = 5
        self.speedx = 0
        self.speedy = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.turnedright = True
        self.turnedleft = False
    
    def move(self, blocklist):    
        if not (self.left and self.right):
            self.speedx = 0
        if not (self.up and self.down):
            self.speedy = 0
        if self.left and not self.right:
            if not self.checkleft(blocklist):
                self.speedx = -self.speed
                self.moveleft()
        if self.right and not self.left:
            if not self.checkright(blocklist):
                self.speedx = self.speed
                self.moveright()
        if self.up and not self.down:
            if not self.checkup(blocklist):
                self.speedy = -self.speed
                self.moveup()
        if self.down and not self.up:
            if not self.checkdown(blocklist):
                self.speedy = self.speed
                self.movedown()
    
    #hero rectangle must be smaller than 40x40px to make movements easier
    def get_realleft(self):    
        return self.rect.left + self.offset
        
    #hero rectangle must be smaller than 40x40px to make movements easier        
    def get_realright(self):
        return self.rect.right - self.offset       

    #hero rectangle must be smaller than 40x40px to make movements easier
    def get_realtop(self):        
        return self.rect.top + self.offset

    #hero rectangle must be smaller than 40x40px to make movements easier
    def get_realbottom(self):        
        return self.rect.bottom - self.offset

    def ifleft(self, boolean):        
        self.left = boolean

    def ifright(self, boolean):    
        self.right = boolean

    def ifup(self, boolean):    
        self.up = boolean

    def ifdown(self, boolean):    
        self.down = boolean

    def moveleft(self):        
        self.rect[0] += self.speedx
        if self.turnedright:
            self.turnedright = False
            self.turnedleft = True
            self.image = self.imageleft
    
    def moveright(self):    
        self.rect[0] += self.speedx
        if self.turnedleft:
            self.turnedright = True
            self.turnedleft = False
            self.image = self.imageright
        
    def moveup(self):
        self.rect[1] += self.speedy
        
    def movedown(self):
        self.rect[1] += self.speedy
    
    #check if blocked
    def checkleft(self, blocklist):    
        for tile in blocklist:
            if (self.rect.left == 0) or \
                    (self.get_realtop() < tile.rect.bottom) and \
                    (self.get_realbottom() > tile.rect.top) and \
                    (self.get_realleft() == tile.rect.right):
                return True
        return False

    #check if blocked
    def checkright(self, blocklist):
        for tile in blocklist:
            if (self.rect.right == screen_width) or \
                    (self.get_realtop() < tile.rect.bottom) and \
                    (self.get_realbottom() > tile.rect.top) and \
                    (self.get_realright() == tile.rect.left):
                return True
        return False
    
    
    #check if blocked
    def checkup(self, blocklist):
        for tile in blocklist:
            if (self.rect.top == 0) or \
                    (self.get_realleft() < tile.rect.right) and \
                    (self.get_realright() > tile.rect.left) and \
                    (self.get_realtop() == tile.rect.bottom):
                return True
        return False
    
    #check if blocked
    def checkdown(self, blocklist):
        for tile in blocklist:
            if (self.rect.top == screen_height) or \
                    (self.get_realleft() < tile.rect.right) and \
                    (self.get_realright() > tile.rect.left) and \
                    (self.get_realbottom() == tile.rect.top):
                return True
        return False
    
    #if not used, hero remembers which key was pressed last which makes
    #some movements blocked until key is pressed and released again
    def reset_movement(self):    
        self.speedx = 0
        self.speedy = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
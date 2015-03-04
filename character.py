"""Base class for all units in battle mode of the game; currently all
units belong to it, in future I plan to implement subclasses with
different attack ranges, abilities etc."""

#imports
import os
from random import *
from initials import *

class Character(pygame.sprite.Sprite):
    
    
    #int, list of two ints, 6 char string, [int, int], int, int, int,
    #image, image, image, image
    def __init__(self, hp, dmg, name, pos, offset, initiative, level, image_passive,\
                image_active=None, image_dead=None, image_pow="pow.png"):
        self.maxhp = hp
        self.hp = hp
        self.dmg = dmg
        self.name = name
        self.alive = True
        self.initiative = initiative
        self.level = level
        self.exp = 0

        if image_passive is not None:
            self.image_passive = pygame.image.load(os.path.join("png",\
                                                image_passive)).convert()
            self.image_passive.set_colorkey(WHITE)
            self.image = self.image_passive
        if image_active is not None:
            self.image_active = pygame.image.load(os.path.join("png",\
                                                image_active)).convert()
            self.image_active.set_colorkey(WHITE)
        if image_dead is not None:
            self.image_dead = pygame.image.load(os.path.join("png",\
                                                image_dead)).convert()
            self.image_dead.set_colorkey(WHITE)
        if image_pow is not None:
            self.pow = pygame.image.load(os.path.join("png",\
                                        image_pow)).convert()
            self.pow.set_colorkey(WHITE)
        
        self.pos = pos
        self.offset = offset
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]
        self.timecounter = 0
        self.bar = Rect((self.pos[0]+12+self.offset),\
                        (self.pos[1]+163), 53, 11)
                
    def get_maxhp(self):
        return self.maxhp

    def get_hp(self):
        return self.hp

    def get_dmg(self):
        return randrange(self.dmg[0], self.dmg[1]+1)

    def get_name(self):
        return self.name
        
    def get_level(self):
        return self.level
    
    #remember, it's not "get rekt"
    def get_rect(self):
        return self.rect
        
    #for clarity: pow is the effect that the weapon produces
    #not the effect of being hit
    def get_pow(self):
        return self.pow

    def take_damage(self, screen, taken, attacker_pow):
        self.hp -= taken
        if taken != 0:
            taken_text = "-" + str(taken)
        else:
            taken_text = str(taken)
        
        taken_to_show = largefont.render(taken_text, True , RED)
        screen.blit(taken_to_show, [self.pos[0], self.pos[1]+10])
        screen.blit(attacker_pow, [self.pos[0]+30, self.pos[1]+10])
        
    def increment_timecounter(self):    
        self.timecounter += self.initiative
        
    def reset_timecounter(self):
        self.timecounter = 0
        
    def lvlup(self, screen):
        if self.exp >= 6*self.level:
            self.level += 1
            self.maxhp += 2
            self.hp = self.maxhp
            self.dmg[0] += 1
            self.dmg[1] += 1
            if self.level%4 == 0:
                self.initiative += 1
            self.exp = 0
            
            screen.blit(largefont.render("LVL UP!", True, (255, 0, 0)),\
            [self.pos[0]+70, self.pos[1]+30])
            
    def postfight(self, expgain, screen):
        self.reset_timecounter()
        self.image = self.image_passive
        self.hp = self.maxhp
        self.show_image(screen)
        self.exp += expgain
        
    def is_active(self):
        if self.is_alive():
            if self.timecounter >= 100:
                self.image = self.image_active
                return True
            else:
                self.image = self.image_passive
                return False
    
    def is_alive(self):
        if self.hp < 1:
            self.timecounter = 0
            self.image = self.image_dead
            self.alive = False
        else:
            self.alive = True
        return self.alive

    def show_image(self, screen):    
        screen.blit(self.image, self.rect)

    def show_hp(self, screen, fontcolor):

        if self.is_alive():            
            disp_hp = str(self.hp) + "/" + str(self.maxhp)
            self.texthp = font.render(disp_hp, True , fontcolor)
            screen.blit(self.texthp,[self.pos[0]+67+self.offset,\
                        self.pos[1]+160])


    def show_bar(self, screen, fontcolor):
        if self.is_alive():
            self.bar_timecounter = Rect((self.pos[0]+14+self.offset),\
                                    (self.pos[1]+165), self.timecounter/2, 8)
            pygame.draw.rect(screen, fontcolor, self.bar, 2)
            if self.timecounter > 0:
                pygame.draw.rect(screen, (0, 0, 255), self.bar_timecounter, 0)

    
    def show_stats(self, screen, pos):
    
        disp_hp = str(self.hp) + "/" + str(self.maxhp)
        disp_dmg = str(self.dmg[0]) + "-" + str(self.dmg[1])
        disp_initiative = str(self.initiative)
        disp_level = str(self.level)
        disp_exp = str(self.exp) + "/" + str(6*self.level)

        self.textname = font.render(self.name, True, WHITE)
        self.texthp = font.render("HP: " + disp_hp, True, WHITE)
        self.textdmg = font.render("DMG: " + disp_dmg, True, WHITE)
        self.textinitiative = font.render("Initiative: " + \
                                disp_initiative, True, WHITE)
        self.textlevel = font.render("Level: " + disp_level, True, WHITE)
        self.textexp = font.render("Experience: " + disp_exp, True, WHITE)
        
        screen.blit(self.textname, [pos[0], pos[1]+40])
        screen.blit(self.texthp, [pos[0], pos[1]+60])
        screen.blit(self.textdmg, [pos[0], pos[1]+80])
        screen.blit(self.textinitiative, [pos[0], pos[1]+100])
        screen.blit(self.textlevel, [pos[0], pos[1]+120])
        screen.blit(self.textexp, [pos[0], pos[1]+140])
        

#initialise objects, armies and object groups for battles; cannot be in
#initials.py, since both files would have to import each other
fighter1 = Character(10, [2, 3], "FIGHTER", [250, 40], 0, 2, 1,\
           "fighter.png", "fighter_act.png", "fighter_dead.png")
fighter2 = Character(10, [2, 3], "FIGHTER", [250, 220], 0, 2, 1,\
           "fighter.png", "fighter_act.png", "fighter_dead.png")
fighter3 = Character(10, [2, 3],  "FIGHTER", [250, 400], 0, 2, 1,\
           "fighter.png", "fighter_act.png", "fighter_dead.png")

tutfighter1 = Character(10, [1, 1], "SPARRINGPARTNER", [470, 40], 0, 2, 0,\
            "tutorial.png", "tutorial_act.png", "tutorial_dead.png")           
tutfighter2 = Character(10, [1, 1], "SPARRINGPARTNER", [470, 220], 0, 2, 0,\
            "tutorial.png", "tutorial_act.png", "tutorial_dead.png")
tutfighter3 = Character(10, [1, 1], "SPARRINGPARTNER", [470, 400], 0, 2, 0,\
            "tutorial.png", "tutorial_act.png", "tutorial_dead.png")            

AIbandit1 = Character(5, [0, 4], "ROGUE", [470, 40], 10, 3, 1,\
            "rogue.png", "rogue_act.png", "rogue_dead.png")
AIbandit2 = Character(5, [0, 4], "ROGUE", [470, 220], 10, 3, 1,\
            "rogue.png", "rogue_act.png", "rogue_dead.png")
AIbandit3 = Character(5, [0, 4], "ROGUE", [470, 400], 10, 3, 1,\
            "rogue.png", "rogue_act.png", "rogue_dead.png")
            
AIbandit4 = Character(5, [0, 4], "ROGUE", [470, 40], 10, 3, 1,\
            "rogue.png", "rogue_act.png", "rogue_dead.png")
AIbandit5 = Character(5, [0, 4], "ROGUE", [470, 220], 10, 3, 1,\
            "rogue.png", "rogue_act.png", "rogue_dead.png")
AIbandit6 = Character(5, [0, 4], "ROGUE", [470, 400], 10, 3, 1,\
            "rogue.png", "rogue_act.png", "rogue_dead.png")
            
AIfighter1 = Character(10, [2, 3], "ENEMY FIGHTER", [470, 40], 0, 2, 1,\
            "aifighter.png", "aifighter_act.png", "aifighter_dead.png")
AIfighter2 = Character(10, [2, 3], "ENEMY FIGHTER", [470, 220], 0, 2, 1,\
            "aifighter.png", "aifighter_act.png", "aifighter_dead.png")
AIfighter3 = Character(10, [2, 3], "ENEMY FIGHTER", [470, 400], 0, 2, 1,\
            "aifighter.png", "aifighter_act.png", "aifighter_dead.png")

         
army = [fighter1, fighter2, fighter3]
tutarmy = [tutfighter1, tutfighter2, tutfighter3]
AIarmy = [AIbandit1, AIbandit2, AIbandit3]
AIarmy2 = [AIbandit4, AIbandit5, AIbandit6]
AIarmy3 = [AIfighter1, AIfighter2, AIfighter3]


#only for testing purposes, intentionally bad
Test1 = Character(1, [2, 3], "Test", [470, 40], 0, 10, 10,\
            "fighter.png", "aifighter_act.png", "aifighter_dead.png")
Test2 = Character(1, [2, 3], "Test", [470, 220], 0, 10, 10,\
            "fighter.png", "aifighter_act.png", "aifighter_dead.png")
Test3 = Character(1, [2, 3], "Test", [470, 400], 0, 10, 10,\
            "fighter.png", "aifighter_act.png", "aifighter_dead.png")
testarmy = [Test1, Test2, Test3]
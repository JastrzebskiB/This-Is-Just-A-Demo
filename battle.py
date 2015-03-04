#pygame.time.wait() times are adjusted for time needed to read messages

#imports
import os
from sys import *
from random import *
import pygame
from pygame.locals import *
from text import *
from character import *
from initials import *

#interestingly, Python treats i > 0 as True
def army_alive(army):
    i = 0
    for unit in army:
       if unit.is_alive():
           i += 1
    return i 

def fight(screen, attacker, defender):
    if attacker.is_alive() and defender.is_alive():
        dealt = attacker.get_dmg()
        defender.take_damage(screen, dealt, attacker.get_pow())
        attacker.reset_timecounter()
        pygame.display.update()
        pygame.time.wait(750)

def click_check(mousepos, AIarmy):
    x = mousepos[0]
    y = mousepos[1]
    for unit in AIarmy:
        if unit.is_alive():
            rect = unit.get_rect()
            if (x >= rect.left and x <= rect.right) and\
                    (y >= rect.top and y <= rect.bottom):
                return unit
            else:
                pass

#in current iteration, it is VERY unlikely this will be ever seen
#unless player tries hard to achieve it
def gameover(screen):
    gameover = pygame.image.load(os.path.join("png", "gg.png")).convert()
    gameover.set_colorkey(BLACK)
    shown = False

    while not shown:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit("Closed in gameover.")
                
        screen.fill(BLACK)
        screen.blit(gameover, [250, 250])
        pygame.display.update()
        pygame.time.wait(4000)
        shown = True

    exit("You have lost")

def end_ceremony(party, army, AIarmy, hero, bgrnd,\
                screen=screen, fontcolor=SUBTITLE_YELLOW):
    
    #enables hero movements without any shenanigans
    hero.reset_movement()    
    pygame.display.update()
    unitlist = []

    for i in range(len(AIarmy)):
        unitlist.append(AIarmy[i])    
    for i in range(len(army)):
        unitlist.append(army[i])    

    if party == army:
        expgain = 0
        for unit in AIarmy:
            expgain += unit.level
        for unit in army:
            unit.postfight(expgain, screen)    
        draw_battle(screen, unitlist, bgrnd, fontcolor)
        for unit in army:
            unit.lvlup(screen)
        
        pygame.display.update()    
        pygame.time.wait(450)
        text = "You won! All of your units have been   "+\
                "restored to full health!"
        show_textbox("HEALER", text, "talker_healer.png")
        pygame.display.update()
        pygame.time.wait(2000)
        
    elif party == AIarmy:
        draw_battle(screen, unitlist, bgrnd, fontcolor)
        text = "All of your units have been disabled!  "+\
                "You have lost the battle. The KING'S   "+\
                "mission is lost now!"
        show_textbox("MASTER-AT-ARMS", text, "talker_maa.png")
        pygame.display.update()
        pygame.time.wait(3000)
        gameover(screen)

def end_ceremony_tutorial(party, army, AIarmy, hero, bgrnd,\
                        screen=screen, fontcolor=SUBTITLE_YELLOW):
    
    #enables hero movements without any shenanigans
    hero.reset_movement()   
    shown1 = False
    shown2 = False
    unitlist = []

    for i in range(len(AIarmy)):
        unitlist.append(AIarmy[i])     
    for i in range(len(army)):
        unitlist.append(army[i])
    pygame.display.update()

    for unit in army:
        unit.timecounter = 0
        unit.image = unit.image_passive
        unit.hp = unit.maxhp

    while (shown1 == False) or (shown2 == False):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit("Closed in intro.")
            if event.type == MOUSEBUTTONDOWN: 
                if not shown1:
                    shown1 = True
                else:
                    shown2 = True
    
        if not shown1:
            draw_battle(screen, unitlist, bgrnd, fontcolor)
            show_textbox("HEALER",\
            "Mesire, it is an honor for me to have  "+\
            "been assigned as your personal medic.  "+\
            "I will tend to your units' health after"+\
            "each battle we manage to win - just as "+\
            "I have brought them back to full health",\
            "talker_healer.png", True)
            pygame.display.update()
        if shown1:
            draw_battle(screen, unitlist, bgrnd, fontcolor)
            show_textbox("HEALER",\
            "a moment ago. Should you want to learn "+\
            "more about your units, their skills and"+\
            "equipment, just click on your hero     "+\
            "while travelling. Use arrow keys to    "+\
            "move your hero on the map.",\
            "talker_healer.png", True)
            pygame.display.update()
            
        #regulate framerate
        pygame.time.wait(40)
        
def draw_battle(screen, unitlist, background, fontcolor):
    screen.blit(background, [0, 0])
    for unit in unitlist:
        unit.show_image(screen)
        unit.show_hp(screen, fontcolor)
        unit.show_bar(screen, fontcolor)

def any_active(unitlist):
    for unit in unitlist:
        if unit.is_active():
            return True
    return False

def which_active(unitlist):
    for unit in unitlist:
        if unit.is_active():
            return unit


#AI targeting algorithms
#for fighting intelligent, organised enemies (i.e. most of fights)
#battle() defaults to this algorithm
def base_targeting(army):
    #army_alive created so it can be shuffled without changing the
    #order in which your units act
    army_alive = []
    hplist = []
    for unit in army:
        if unit.is_alive():
            army_alive.append(unit)
    shuffle(army_alive) #so AI doesn't always attack same unit first
    for unit in army_alive:
        hplist.append(unit.hp)
    return army_alive[hplist.index(min(hplist))]

#for tutorial or cases where enemy wants to savour the victory
def worst_targeting(army):
    #army_alive created so it can be shuffled without changing the
    #order in which your units act
    army_alive = []
    hplist = []
    for unit in army:
        if unit.is_alive():
            army_alive.append(unit)
    shuffle(army_alive) #so AI doesn't always attack same unit first
    for unit in army_alive:
        hplist.append(unit.hp)
    return army_alive[hplist.index(max(hplist))]

#surprisingly, is very slightly better than "worst targeting"
#use for wild animals, mobs and other unorganised enemies
def random_targeting(army):
    army_alive = []
    for unit in army:
        if unit.is_alive():
            army_alive.append(unit)
    shuffle(army_alive) #so AI doesn't always attack same unit first
    if len(army_alive) > 0:
        return army_alive[0]

#main function
def battle(screen, army, AIarmy, hero, bgrnd, fontcolor=SUBTITLE_YELLOW,\
            AItargeting=base_targeting, tutorial=False):
    unitlist = []
    background = pygame.image.load(os.path.join("png", bgrnd)).convert()
    #simplified version since in the demo armies only have 3 units
    for i in range(3):
        unitlist.append(AIarmy[i])
        unitlist.append(army[i])


    while army_alive(army) and army_alive(AIarmy):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit("Closed in battle.")
            if event.type == MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                if any_active(army):
                    targeted = click_check(mousepos, AIarmy)
                    if targeted is not None:
                        fight(screen, which_active(army), targeted)

        #responsible for initiative; waits for action if any unit is active
        for unit in unitlist:
            if not any_active(unitlist):           
                if unit.is_alive():
                    unit.increment_timecounter()                    

        #graphics and text
        draw_battle(screen, unitlist, background, fontcolor)        
        pygame.display.update()
        
        #AIarmy fights
        if any_active(AIarmy) and not any_active(army):
            draw_battle(screen, unitlist, background, fontcolor)
            pygame.display.update()
            fight(screen, which_active(AIarmy), AItargeting(army))
        
        #regulate framerate
        pygame.time.wait(100)
    
    #only goes off after either army is dead
    if army_alive(army) and not tutorial:
        end_ceremony(army, army, AIarmy, hero, background, screen, fontcolor)    
    elif army_alive(AIarmy) and not tutorial:
        end_ceremony(AIarmy, army, AIarmy, hero, background, screen, fontcolor)
    elif army_alive(army) and tutorial:
        end_ceremony_tutorial(army, army, AIarmy, hero, background)
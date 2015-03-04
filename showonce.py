#imports
from battle import *
import pygame
from pygame.locals import *
from text import *
from initials import *

def intro(screen):
    castle_shown = False
    shown1 = False
    shown2 = False
    intro_picture = pygame.image.load(os.path.join("png",\
    "intro.png")).convert()
    title = pygame.image.load(os.path.join("png",\
    "title.png")).convert()
    fakemap = pygame.image.load(os.path.join("png",\
    "fakemap.png")).convert()
    title.set_colorkey(WHITE)
    i = -600

    while (not shown1) or (not shown2):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit("Closed in intro.")
            if event.type == MOUSEBUTTONDOWN:
                if castle_shown: 
                    if not shown1:
                        shown1 = True
                    else:
                        shown2 = True
                        
        #castle image scrolls onto the screen
        if i < 0 and (not castle_shown):
            screen.blit(intro_picture, [0, i])
            i += 2
            pygame.display.update()
        elif not castle_shown:    
            screen.blit(title, [55, 100])
            pygame.display.update()
            pygame.time.wait(4000)
            castle_shown = True
        
        if castle_shown and not shown1:
            screen.blit(fakemap, [0, 0])
            show_textbox("KING",\
            "Ah, it is good to see you my boy!      "+\
            "Lately we have been receiving reports  "+\
            "of vagrants, that attack anyone who    "+\
            "shows up on the coast. The fishermen   "+\
            "near the lake have more information    ",\
            "talker_king.png", True)
            pygame.display.update()
        
        if shown1:
            screen.blit(fakemap, [0, 0])
            show_textbox("KING",\
            "about them. MASTER-AT-ARMS wants to see"+\
            "you to refresh your knowledge about    "+\
            "tactics... or, ah, whatever you boys   "+\
            "call fighting nowadays. Report back to "+\
            "me after you get rid of the bandits.   ",\
            "talker_king.png", True)
            pygame.display.update()
            
        #regulate framerate
        pygame.time.wait(40)

def tutorial(screen, army, tutarmy, hero, bgrnd, AItargeting=worst_targeting,\
            color=SUBTITLE_YELLOW):   
    shown1 = False
    shown2 = False
    shown3 = False
    unitlist = []
    background = pygame.image.load(os.path.join("png", bgrnd)).convert()
    #simplified version since in the demo armies only have 3 units
    for i in range(len(tutarmy)):
        unitlist.append(tutarmy[i])
        unitlist.append(army[i])
    
    while (not shown1) or (not shown2) or (not shown3):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit("Closed in tutorial.")
            if event.type == MOUSEBUTTONDOWN:
                #funnily enough, works with if/if/if with reverse order
                #(i.e. if shown2/if shown1 and not shown2/if not shown1
                if (not shown1):
                    shown1 = True
                elif (shown1) and (not shown2):
                    shown2 = True
                elif (shown2):
                    shown3 = True
   
        draw_battle(screen, unitlist, background, color)
        
        if not shown1:
            show_textbox("MASTER-AT-ARMS",\
            "Time for the last sparring before you  "+\
            "go off to prove yourself. Quick rundown"+\
            "of everything you know: your soldiers  "+\
            "are on the left, enemy is on the right."+\
            "The bar fills as units get ready to act",\
            "talker_maa.png", True)
            pygame.display.update()
        
        if shown1 and not shown2:
            draw_battle(screen, unitlist, background, color)
            show_textbox("MASTER-AT-ARMS",\
            "and ones at top move before ones below "+\
            "them. Practice to heart's content and  "+\
            "don't worry about hurting anyone - the "+\
            "healers will bring everyone back to    "+\
            "scratch just as what will happen to    ",\
            "talker_maa.png", True)
            pygame.display.update()
            
        if shown2:
            draw_battle(screen, unitlist, background, color)
            show_textbox("MASTER-AT-ARMS",\
            "your units after a won battle. Your    "+\
            "soldiers will grow more experienced and"+\
            "stronger after fights - bring them back"+\
            "to me so that I could teach them some  "+\
            "new tricks.                            ",\
            "talker_maa.png", True)
            pygame.display.update()
            
        #regulate framerate
        pygame.time.wait(100)
            
    battle(screen, army, tutarmy, hero, bgrnd, color, AItargeting, True)
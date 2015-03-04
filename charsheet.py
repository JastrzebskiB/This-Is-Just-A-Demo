import pygame
from pygame.locals import *
from sys import *
from character import *
from initials import *

def drawtextrect(text, rect, screen):
    pygame.draw.rect(screen, UGRAY, rect, 4)
    screen.blit(largefont.render\
               (text, True, UGRAY), [rect.left+4, rect.top])

def hovertextdemo(rectlist, mousepos, screen):
    for rect in rectlist:
        if ((mousepos[0] > rect.left and mousepos[0] < rect.right) and\
            (mousepos[1] > rect.top and mousepos[1] < rect.bottom)):
            screen.blit(smallfont.render("(Will be implemented", \
            True, WHITE), [mousepos[0]+3, mousepos[1]+14])
            screen.blit(smallfont.render("in the full version.)", \
            True, WHITE), [mousepos[0]+3, mousepos[1]+28])
    
def charsheet(army, screen=screen):
    done = False
    items_rects = []
    for i in range(len(army)):
        name = str(i)
        name = Rect(596, (i*200)+40, 96, 26)
        items_rects.append(name)
    skills_rects = []
    for i in range(len(army)):
        name = str(i)
        name = Rect(596, (i*200)+76, 96, 26)
        skills_rects.append(name)
    #exit button   
    xbtn = Rect(750, 10, 30, 30) #left, top, width, height

    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit("Closed in charsheet.")
            if event.type == MOUSEBUTTONDOWN:
                if ((mousepos[0] > xbtn.left) and\
                        (mousepos[0] < xbtn.right) and\
                        (mousepos[1] > xbtn.top) and\
                        (mousepos[1] < xbtn.bottom)):
                    done = True
        
        mousepos = pygame.mouse.get_pos()
        screen.fill(BLUE)
        
        #simplified version, as in demo the max intended size
        #of our army is 3
        for i in range(len(army)):
            screen.blit(army[i].image, [80, i*200])
            army[i].show_stats(screen, [300, i*200])
     
        for rect in items_rects:
            drawtextrect("ITEMS", rect, screen)
                        
        for rect in skills_rects:
            drawtextrect("SKILLS", rect, screen)
        
        hovertextdemo(items_rects, mousepos, screen)
        hovertextdemo(skills_rects, mousepos, screen)
        
        #"exit" button
        pygame.draw.rect(screen, URED, xbtn, 4)
        pygame.draw.line(screen, URED, xbtn.topleft, xbtn.bottomright, 2)
        pygame.draw.line(screen, URED, xbtn.bottomleft, xbtn.topright, 2)
        
        pygame.display.update()
        pygame.time.wait(40)
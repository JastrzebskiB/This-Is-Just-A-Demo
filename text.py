"""Used to display text on a pygame.Surface screen in a blue, opaque
box on the bottom of the screen. Five lines, 39 chars each (plus name
in a separate line). Making sure text fits the required format is on
the end of user."""

#imports
import os
from initials import *

#declare textbox variables: non-transparent border, opaque filling
textborder = Rect(2, 455, 796, 179)
textfill = pygame.Surface((800, 200), SRCALPHA)
textfill.fill((0, 0, 255, 180))
imagerect = Rect(600, 200, 200, 400)

#str, str, pygame.Surface(200x400px png), bool, pygame.Surface(screen) 
def show_textbox(name, text, talker_image=None, remind=False, screen=screen):

    #bool determines if you need to click to proceed further (default
    #use in functions is that textbox disappears by itself)
    actionable = remind    
    textheight = 455
    screen.blit(textfill, textborder)
    pygame.draw.rect(screen, BLUE, textborder, 5)
    
    if actionable:
        reminder = "(Click to proceed.)"
        disp_reminder = smallfont.render(reminder, True, WHITE)
        screen.blit(disp_reminder, (404, textheight))
    
    if name is not None:
        name = name + ":"
        disp_name = largefont.render(name, True, WHITE)
        screen.blit(disp_name, (2, textheight, 796, 205))
    
    if talker_image is not None:
        talker_image = pygame.image.load(os.path.join("png", talker_image)).convert()
        talker_image.set_colorkey(WHITE)
        screen.blit(talker_image, imagerect)

    #lines are 39 characters long for 24 Courier
    lines = 0
    if len(text) % 40 == 0:
        lines = len(text) / 40
    else:
        lines = len(text) / 40 + 1

    #turn text to an array to use pop() later
    wholetext = []
    for char in text:
        wholetext.append(char)
    wholetext.reverse()

    #turn text into separate lines having 39 chars
    linesarray = []
    j = lines
    while j > 0:
        j -= 1
        i = 0
        oneline = ""     
        while i < 39:
            i += 1
            if len(wholetext) > 0:
                oneline += wholetext.pop()
        linesarray.append(oneline)
    
    #turn separate lines into text rendered by pygame
    j = lines
    while j > 0:
        textheight += 24
        text = linesarray[-j]
        disp_text = largefont.render(text, True, WHITE)
        screen.blit(disp_text, (2, textheight, 796, 205))
        j -= 1
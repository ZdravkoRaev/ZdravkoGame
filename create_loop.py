"""a"""
import json
import os
import pygame
from levelCreator.level import Level
from drawing_level import draw
from menus.button_creator import render_button
from menus.button import Button
from levels.converter import add_level_to_json


def run(level: Level, screen):
    """a"""
    pressed=(0,0)
    cursor_state=1

    state=0
    clock = pygame.time.Clock()
    running=True
    while running:
        clock.tick(60)
        mouse_pos=list(pygame.mouse.get_pos())
        mouse_press=pygame.mouse.get_pressed()[0]
        state=render_button(Button\
        (1200,850,300,50,"SaveLevel",100),screen,state,pressed,mouse_pos[0], mouse_pos[1])
        cursor_state=render_button\
            (Button(100,850,50,50,"Air",0),screen,cursor_state,pressed,mouse_pos[0], mouse_pos[1])
        cursor_state=render_button(Button\
        (200,850,50,50,"wall",1),screen,cursor_state,pressed,mouse_pos[0], mouse_pos[1])
        cursor_state=render_button(Button\
        (300,850,50,50,"Break",2),screen,cursor_state,pressed,mouse_pos[0], mouse_pos[1])
        cursor_state=render_button(Button\
        (400,850,50,50,"En1",3),screen,cursor_state,pressed,mouse_pos[0], mouse_pos[1])
        cursor_state=render_button(Button\
        (500,850,50,50,"En2",4),screen,cursor_state,pressed,mouse_pos[0], mouse_pos[1])
        cursor_state=render_button(Button\
        (600,850,50,50,"Proj",5),screen,cursor_state,pressed,mouse_pos[0], mouse_pos[1])
        cursor_state=render_button(Button\
        (700,850,50,50,"Target",6),screen,cursor_state,pressed,mouse_pos[0], mouse_pos[1])
        mouse_pos[0]=int((mouse_pos[0]-mouse_pos[0]%25)/25)
        mouse_pos[1]=int((mouse_pos[1]-mouse_pos[1]%25)/25)

        #the player can change only tiles that are not on the border and aren't the two startin tiles
        if mouse_press and mouse_pos[0]>=2 and mouse_pos[0]<=61\
            and mouse_pos[1]>=2 and mouse_pos[1]<=33\
            and not (mouse_pos[0]==4 and(mouse_pos[1]==32 or mouse_pos[1]==33)):
            level.objects[mouse_pos[0]][mouse_pos[1]]=cursor_state
        for event in pygame.event.get():
            if event.type==pygame.QUIT: # pylint: disable=maybe-no-member
                running=False
        pressed=(pressed[1],mouse_press)
        draw(screen,level)
        if state==100:
            running=False
            path1=os.getcwd()
            fullPath=os.path.join(path1,"levels","mainStory.txt")
            with open(fullPath, "r",encoding='utf-8') as jsonfile:
                json1 = json.load(jsonfile)
            for i in range(20):
                if not str(i+1) in json1:
                    add_level_to_json(level,i+1)
                    break

    return 0

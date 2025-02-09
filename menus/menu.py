import json
import os
import pygame
from menus import button_creator
from menus import button as button1
from levelCreator.level import Level
import create_loop
import run_level

from levels.converter import deleteLevelFromJson
def main():
    pygame.init() # pylint: disable=maybe-no-member
    pygame.display.set_caption("Game")

    pygame.font.init()
    bg = pygame.display.set_mode((1600, 900))

    pressed = (0,0)
    clock = pygame.time.Clock()
    running=True
    state=0
    in_level=False
    in_creator=False
    while running:
        if state<101:
            in_level=False
        if state!=100:
            in_creator=False
        if not in_level and not in_creator:
            bg.fill((183, 201, 226))
            clock.tick(60)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if state==0:
                state=button_creator.render_button(button1.Button\
                (650,300,300,100,"Main Levels",1),bg,state,pressed,mouse_x,mouse_y)
                state=button_creator.render_button(button1.Button\
                (650,430,300,100,"User Levels",2),bg,state,pressed,mouse_x,mouse_y)
                state=button_creator.render_button(button1.Button\
                (650,560,300,100,"Highscores",3),bg,state,pressed,mouse_x,mouse_y)
                state=button_creator.render_button(button1.Button\
                (650,690,300,100,"Credits",4),bg,state,pressed,mouse_x,mouse_y)
            elif state==1:
                for i in range(20):
                    x=450
                    y=200
                    offset=150
                    path1=os.getcwd()
                    fullPath=os.path.join(path1,"levels","mainStory.txt")
                    with open(fullPath, "r",encoding='utf-8') as jsonfile:
                        json1 = json.load(jsonfile)
                    if str(i+1) in json1:                    
                        state=button_creator.render_button(button1.Button\
                        (x+i%5*offset,y+int(i/5)*offset,100,100,str(i+1),i+101),bg,state,pressed,mouse_x,mouse_y)
                state=button_creator.render_button(button1.Button\
                (100,770,300,100,"Retrun to main menu",0),bg,state,pressed,mouse_x,mouse_y)
                state=button_creator.render_button(button1.Button\
                (1200,770,300,100,"Enter delete Mode",11),bg,state,pressed,mouse_x,mouse_y)
            elif state==11:
                deletion=-1
                for i in range(20):
                    x=450
                    y=200
                    offset=150
                    path1=os.getcwd()
                    fullPath=os.path.join(path1,"levels","mainStory.txt")
                    with open(fullPath, "r",encoding='utf-8') as jsonfile:
                        json1 = json.load(jsonfile)
                    if str(i+1) in json1:
                        deletion=button_creator.render_button(button1.Button\
                        (x+i%5*offset,y+int(i/5)*offset,100,100,str(i+1),i),bg,deletion,pressed,mouse_x,mouse_y)
                if deletion!=-1:
                    deleteLevelFromJson(str(deletion+1))
                state=11
                state=button_creator.render_button(button1.Button\
                (1200,770,300,100,"Exit delete Mode",1),bg,state,pressed,mouse_x,mouse_y)
                state=button_creator.render_button(button1.Button\
                (100,770,300,100,"Retrun to main menu",0),bg,state,pressed,mouse_x,mouse_y)
            elif state==2:
                state=button_creator.render_button(button1.Button\
                (100,770,300,100,"Retrun to main menu",0),bg,state,pressed,mouse_x,mouse_y)
                state=button_creator.render_button(button1.Button\
                (1200,770,300,100,"Create New Level",100),bg,state,pressed,mouse_x,mouse_y)

            pressed = (pressed[1],pygame.mouse.get_pressed()[0])
            if state>100 and state<121:
                in_level=True
                state=run_level.run_level(state-100,bg)
            elif state==100:
                in_creator=True
                state=create_loop.run(Level(),bg)


            for event in pygame.event.get():
                if event.type == pygame.QUIT: # pylint: disable=maybe-no-member
                    pygame.quit() # pylint: disable=maybe-no-member
                    raise SystemExit
            pygame.display.update()

if __name__ == "__main__":
    main()

import pygame
import json
import os
from menus import buttonCreator
from menus import button as button1
from levelCreator.level import Level
import createLoop
import runLevel

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
    inLevel=False
    inCreator=False
    while running:
        if state<101:
            inLevel=False
        if state!=100:
            inCreator=False
        if not inLevel and not inCreator:
            bg.fill((183, 201, 226))
            clock.tick(60)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if state==0:
                state=buttonCreator.renderButton(button1.Button\
                (650,300,300,100,"Main Levels",1),bg,state,pressed,mouse_x,mouse_y)
                state=buttonCreator.renderButton(button1.Button\
                (650,430,300,100,"User Levels",2),bg,state,pressed,mouse_x,mouse_y)
                state=buttonCreator.renderButton(button1.Button\
                (650,560,300,100,"Highscores",3),bg,state,pressed,mouse_x,mouse_y)
                state=buttonCreator.renderButton(button1.Button\
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
                        state=buttonCreator.renderButton(button1.Button\
                        (x+i%5*offset,y+int(i/5)*offset,100,100,str(i+1),i+101),bg,state,pressed,mouse_x,mouse_y)
                state=buttonCreator.renderButton(button1.Button\
                (100,770,300,100,"Retrun to main menu",0),bg,state,pressed,mouse_x,mouse_y)
                state=buttonCreator.renderButton(button1.Button\
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
                        deletion=buttonCreator.renderButton(button1.Button\
                        (x+i%5*offset,y+int(i/5)*offset,100,100,str(i+1),i),bg,deletion,pressed,mouse_x,mouse_y)
                if deletion!=-1:
                    deleteLevelFromJson(str(deletion+1))
                state=11
                state=buttonCreator.renderButton(button1.Button\
                (1200,770,300,100,"Exit delete Mode",1),bg,state,pressed,mouse_x,mouse_y)
                state=buttonCreator.renderButton(button1.Button\
                (100,770,300,100,"Retrun to main menu",0),bg,state,pressed,mouse_x,mouse_y)
            elif state==2:
                state=buttonCreator.renderButton(button1.Button\
                (100,770,300,100,"Retrun to main menu",0),bg,state,pressed,mouse_x,mouse_y)
                state=buttonCreator.renderButton(button1.Button\
                (1200,770,300,100,"Create New Level",100),bg,state,pressed,mouse_x,mouse_y)

            pressed = (pressed[1],pygame.mouse.get_pressed()[0])
            if state>100 and state<121:
                inLevel=True
                state=runLevel.runLevel(state-100,bg)
            elif state==100:
                inCreator=True
                state=createLoop.run(Level(),bg)


            for event in pygame.event.get():
                if event.type == pygame.QUIT: # pylint: disable=maybe-no-member
                    pygame.quit() # pylint: disable=maybe-no-member
                    raise SystemExit
            pygame.display.update()

if __name__ == "__main__":
    main()
    




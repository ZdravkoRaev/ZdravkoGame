import pygame
from levelCreator.level import Level
from drawingLevel import draw
from menus.buttonCreator import renderButton
from menus.button import Button
from levels.converter import addLevelToJson
import json
import os

def run(theLevel: Level, screen):
    pressed=(0,0)
    cursorState=1

    state=0
    clock = pygame.time.Clock()
    running=True
    while running:
        clock.tick(60)
        mousePos=list(pygame.mouse.get_pos())
        mousePress=pygame.mouse.get_pressed()[0]
        state=renderButton(Button(1200,850,300,50,"SaveLevel",(100,100,100),(150,150,150),(255,0,0),100),screen,state,pressed,mousePos[0], mousePos[1])
        cursorState=renderButton(Button(100,850,50,50,"Air",(100,100,100),(150,150,150),(255,0,0),0),screen,cursorState,pressed,mousePos[0], mousePos[1])
        cursorState=renderButton(Button(200,850,50,50,"wall",(100,100,100),(150,150,150),(255,0,0),1),screen,cursorState,pressed,mousePos[0], mousePos[1])
        cursorState=renderButton(Button(300,850,50,50,"Break",(100,100,100),(150,150,150),(255,0,0),2),screen,cursorState,pressed,mousePos[0], mousePos[1])
        cursorState=renderButton(Button(400,850,50,50,"En1",(100,100,100),(150,150,150),(255,0,0),3),screen,cursorState,pressed,mousePos[0], mousePos[1])
        cursorState=renderButton(Button(500,850,50,50,"En2",(100,100,100),(150,150,150),(255,0,0),4),screen,cursorState,pressed,mousePos[0], mousePos[1])
        cursorState=renderButton(Button(600,850,50,50,"Proj",(100,100,100),(150,150,150),(255,0,0),5),screen,cursorState,pressed,mousePos[0], mousePos[1])
        cursorState=renderButton(Button(700,850,50,50,"Target",(100,100,100),(150,150,150),(255,0,0),6),screen,cursorState,pressed,mousePos[0], mousePos[1])
        mousePos[0]=int((mousePos[0]-mousePos[0]%25)/25)
        mousePos[1]=int((mousePos[1]-mousePos[1]%25)/25)
        if mousePress and mousePos[0]>=2 and mousePos[0]<=61 and mousePos[1]>=2 and mousePos[1]<=33:
            theLevel.objects[mousePos[0]][mousePos[1]]=cursorState
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        pressed=(pressed[1],mousePress)
        draw(screen,theLevel)
        if state==100:
            running=False
            path1=os.getcwd()
            fullPath=os.path.join(path1,"levels","mainStory.txt")
            with open(fullPath, "r") as jsonfile:
                json1 = json.load(jsonfile)  
            for i in range(20):
                if not str(i+1) in json1:  
                    addLevelToJson(theLevel,i+1)
                    break

    return 0
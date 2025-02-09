"""a"""
#To do: make it only draw, not also update enemies
import os
import pygame
from enteties.player.player import Player
from enteties.enemies import basic_flier
from enteties.enemies import shooty_flier
from enteties.enemies import projectile
from enteties.enemies import target

def drawStart(screen,player : Player ,level,enemies):
    """a"""
    pygame.display.update()
    screen.fill((0,0,0))
    for x in range(64):
        for y in range(36):
            if level.objects[x][y]==3:
                enemy=basic_flier.BasicFlier()
                enemy.base.bounding_box.x=x*25
                enemy.base.bounding_box.y=y*25
                enemies.append(enemy)
                level.objects[x][y]=0
            if level.objects[x][y]==4:
                enemy=shooty_flier.ShootyFlier()
                enemy.base.bounding_box.x=x*25
                enemy.base.bounding_box.y=y*25
                enemies.append(enemy)
                level.objects[x][y]=0
            if level.objects[x][y]==5:
                enemy=projectile.Projectile()
                enemy.base.bounding_box.x=x*25
                enemy.base.bounding_box.y=y*25
                enemies.append(enemy)
                level.objects[x][y]=0
            if level.objects[x][y]==6:
                enemy=target.Target()
                enemy.base.bounding_box.x=x*25
                enemy.base.bounding_box.y=y*25
                enemies.append(enemy)
                level.objects[x][y]=0

    for x in range(64):
        for y in range(36):
            pygame.draw.rect(screen,(255,255,255),pygame.Rect((x*25,y*25,1,1)))
    if player.is_attacking:
        pygame.draw.rect(screen,(255,0,0),player.hurtbox)
    return enemies

def draw(screen,player : Player ,level,enemies,frame:int):
    image=pygame.image.load(os.path.join("sprites","enemies","target.png")).convert_alpha()
    walk1=pygame.image.load(os.path.join("sprites","player","walking","walk1.png")).convert_alpha()
    walk2=pygame.image.load(os.path.join("sprites","player","walking","walk2.png")).convert_alpha()
    walk3=pygame.image.load(os.path.join("sprites","player","walking","walk3.png")).convert_alpha()
    walk4=pygame.image.load(os.path.join("sprites","player","walking","walk4.png")).convert_alpha()
    walk5=pygame.image.load(os.path.join("sprites","player","walking","walk5.png")).convert_alpha()
    walk6=pygame.image.load(os.path.join("sprites","player","walking","walk6.png")).convert_alpha()
    
    pygame.display.update()
    screen.fill((0,0,0))
    if player.hp<=0:
        pygame.draw.rect(screen,(0,100,0),player.base.bounding_box)
    else:
        if int(frame/3)%6==0:
            screen.blit(walk1,(player.base.bounding_box.x-7,player.base.bounding_box.y-12))
        elif int(frame/3)%6==1:
            screen.blit(walk2,(player.base.bounding_box.x-7,player.base.bounding_box.y-12))
        elif int(frame/3)%6==2:
            screen.blit(walk3,(player.base.bounding_box.x-7,player.base.bounding_box.y-12))
        elif int(frame/3)%6==3:
            screen.blit(walk4,(player.base.bounding_box.x-7,player.base.bounding_box.y-12))
        elif int(frame/3)%6==4:
            screen.blit(walk5,(player.base.bounding_box.x-7,player.base.bounding_box.y-12))
        else: 
            screen.blit(walk6,(player.base.bounding_box.x-7,player.base.bounding_box.y-12))
    for item in enemies:
        color=(255,255,255)
        if item.id==1:
            color=(255,0,0)
            pygame.draw.rect(screen,color,item.base.bounding_box)
        if item.id==2:
            color=(255,0,255)
            pygame.draw.rect(screen,color,item.base.bounding_box)
        if item.id==100:
            color=(255,255,0)
            pygame.draw.rect(screen,color,item.base.bounding_box)
        if item.id==0:
            screen.blit(image,(item.base.bounding_box.x,item.base.bounding_box.y))
    for x in range(64):
        for y in range(36):
            if level.objects[x][y]==1:
                a=pygame.Rect((x*25,y*25,25,25))
                pygame.draw.rect(screen,(0,0,255),a)
            if level.objects[x][y]==2:
                a=pygame.Rect((x*25,y*25,25,25))
                pygame.draw.rect(screen,(0,255,255),a)
            if level.objects[x][y]==3:
                level.objects[x][y]=0
            if level.objects[x][y]==4:
                level.objects[x][y]=0
            if level.objects[x][y]==5:
                level.objects[x][y]=0

    for x in range(64):
        for y in range(36):
            pygame.draw.rect(screen,(255,255,255),pygame.Rect((x*25,y*25,1,1)))
    if player.is_attacking:
        pygame.draw.rect(screen,(255,0,0),player.hurtbox)

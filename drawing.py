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

def draw(screen,player : Player ,level,enemies,frame:int,tile,bg):

    pygame.display.update()
    screen.blit(bg,(0,0))
    screen.blit(player.sprites(frame),(player.base.bounding_box.x-8,player.base.bounding_box.y-12))



    for item in enemies:
        screen.blit(item.sprite(player),(item.base.bounding_box.x-8,item.base.bounding_box.y-12))

    for x in range(64):
        for y in range(36):
            if level.objects[x][y]==1:
                screen.blit(tile,(x*25,y*25))
            if level.objects[x][y]==2:
                a=pygame.Rect((x*25,y*25,25,25))
                pygame.draw.rect(screen,(0,255,255),a)
            if level.objects[x][y]==3:
                level.objects[x][y]=0
            if level.objects[x][y]==4:
                level.objects[x][y]=0
            if level.objects[x][y]==5:
                level.objects[x][y]=0

    if player.is_attacking:
        pygame.draw.rect(screen,(255,0,0),player.hurtbox)

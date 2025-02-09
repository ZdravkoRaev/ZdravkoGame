"""draws the requested sprite on a surface"""
import os
import pygame
def draw(ID : int, x : int, y : int,surface):
    """function"""
    ID+=2
    image=pygame.image.load(os.path.join("sprites","enemies","target.png")).convert_alpha()
    surface.blit(image,(x,y))

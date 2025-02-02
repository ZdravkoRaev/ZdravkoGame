import pygame
import os
def draw(ID : int, x : int, y : int,surface):
    image=pygame.image.load(os.path.join("sprites","enemies","target.png")).convert_alpha()
    surface.blit(image,(x,y))

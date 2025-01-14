import pygame
def draw(ID : int, x : int, y : int,surface):
    image=pygame.image.load("C:\pythonstuff\homework7\sprites\wallsprites\wall0.png").convert_alpha()
    surface.blit(image,(x,y))

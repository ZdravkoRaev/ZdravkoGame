"""a"""
import pygame
from enteties.template_entety import TempalteEntety

def collysions(entety : TempalteEntety,level):
    """a"""
    collisions_with_level=list()
    for x in range(6):
        for y in range(6):
            #making sure wee are checking only parts in the level
            if x+int((entety.x-entety.x%25)/25)-3>=0 and\
            x+int((entety.x-entety.x%25)/25)-3<=63 and\
            y+int((entety.y-entety.y%25)/25)-3>=0 and\
            y+int((entety.y-entety.y%25)/25)-3<=35:
                if level.objects\
                    [x+int((entety.x-entety.x%25)/25)-3][y+int((entety.y-entety.y%25)/25)-3]:
                    a=pygame.Rect(((x+int((entety.x-entety.x%25)/25)-3)*25,\
                                   (y+int((entety.y-entety.y%25)/25)-3)*25,25,25))
                    if entety.colliderect(a):
                        collisions_with_level.append(a)
    return collisions_with_level

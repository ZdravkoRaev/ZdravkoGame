"""handles all collisions"""
import pygame
from enteties.template_entety import TempalteEntety
def collisions_enteties(entety1 :TempalteEntety,all_enteties :list[TempalteEntety]):
    """checks if an entety collieds with other enteties"""
    collis_ent=list()
    for item in all_enteties:
        if item is not entety1:
            if item.base.bounding_box.x+500>entety1.base.bounding_box.x\
            and item.base.bounding_box.y+500>entety1.base.bounding_box.y\
            and item.base.bounding_box.x-500<entety1.base.bounding_box.x\
            and item.base.bounding_box.y-500<entety1.base.bounding_box.y\
            and entety1.base.bounding_box.colliderect(item.base.bounding_box):
                collis_ent.append(item)
    return collis_ent
def collysions_with_level(entety : TempalteEntety,level):
    """checks if an entety collides with parts of the level"""
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

def dir_collisions(entety : TempalteEntety,level):
    """sets which parts of an entety are colliding"""
    entety.base.wall_below=False
    entety.base.wall_left=False
    entety.base.wall_above=False
    entety.base.wall_right=False
    entety.base.bounding_box.x+=entety.base.x_vel
    collisions=collysions_with_level(entety.base.bounding_box,level)


    for item in collisions:
        if entety.base.x_vel>0:
            entety.base.wall_right=True
            entety.base.bounding_box.right=item.left
            entety.base.x_vel=0
        elif entety.base.x_vel<0:
            entety.base.wall_left=True
            entety.base.bounding_box.left=item.right
            entety.base.x_vel=0
    entety.base.bounding_box.y+=entety.base.y_vel
    collisions=collysions_with_level(entety.base.bounding_box,level)
    for item in collisions:
        if entety.base.y_vel>0:
            entety.base.wall_below=True
            entety.base.bounding_box.bottom=item.top
            entety.base.y_vel=0
        elif entety.base.y_vel<0:
            entety.base.wall_above=True
            entety.base.bounding_box.top=item.bottom
            entety.base.y_vel=0
    return entety

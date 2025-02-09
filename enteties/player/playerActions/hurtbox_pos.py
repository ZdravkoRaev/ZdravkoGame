"""a"""
import math
from enteties.player.player import Player
def hurt_pos(player : Player,mouse_pos):
    """a"""
    x=mouse_pos[0]-player.base.bounding_box.centerx
    y=mouse_pos[1]-player.base.bounding_box.centery
    lenght=math.sqrt(x*x+y*y)
    player.hurtbox.centerx=player.base.bounding_box.centerx+x/lenght*30
    player.hurtbox.centery=player.base.bounding_box.centery+y/lenght*30
    return player

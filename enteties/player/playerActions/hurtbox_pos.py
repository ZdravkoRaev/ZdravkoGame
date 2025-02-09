"""a"""
import math
from enteties.player.player import Player
def hurt_pos(player : Player,mouse_pos):
    """a"""
    x=mouse_pos[0]-player.base.bounding_box.x
    y=mouse_pos[1]-player.base.bounding_box.y
    lenght=math.sqrt(x*x+y*y)
    player.hurtbox.x=player.base.bounding_box.x+x/lenght*30-13
    player.hurtbox.y=player.base.bounding_box.y+y/lenght*30
    return player

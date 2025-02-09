"""a"""
import math
from enteties.player.player import Player
def hurt_pos(player : Player,mouse_pos):
    """a"""
    x=mouse_pos[0]-player.base.boundingBox.x
    y=mouse_pos[1]-player.base.boundingBox.y
    lenght=math.sqrt(x*x+y*y)
    player.hurtbox.x=player.base.boundingBox.x+x/lenght*30-13
    player.hurtbox.y=player.base.boundingBox.y+y/lenght*30
    return player

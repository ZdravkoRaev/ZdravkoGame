"""sets the players vel to to thee needed one for dashing"""
import math
from enteties.player.player import Player
def dash(player : Player,mouse_pos):
    """function"""
    if player.cad_dash:
        x=mouse_pos[0]-player.base.bounding_box.x-12
        y=mouse_pos[1]-player.base.bounding_box.y-25
        lenght=math.sqrt(x*x+y*y)
        player.base.x_vel=x/lenght*12
        player.base.y_vel=y/lenght*8
        player.is_dashing=True
        player.cad_dash=False
    return player

"""sets the players vel to to thee needed one for dashing"""
import math
from enteties.player.player import Player
def dash(player : Player,mouse_pos):
    """function"""
    if player.canDash:
        x=mouse_pos[0]-player.base.boundingBox.x
        y=mouse_pos[1]-player.base.boundingBox.y
        lenght=math.sqrt(x*x+y*y)
        player.base.x_vel=x/lenght*12
        player.base.y_vel=y/lenght*8
        player.isDashing=True
        player.canDash=False
    return player

import math
from enteties.player.player import Player
def dash(player : Player,mouse,mousePos):
    if player.canDash:
        x=mousePos[0]-player.base.boundingBox.x
        y=mousePos[1]-player.base.boundingBox.y
        lenght=math.sqrt(x*x+y*y)
        player.base.x_vel=x/lenght*12
        player.base.y_vel=y/lenght*8
        player.isDashing=True
        player.canDash=False
    return player
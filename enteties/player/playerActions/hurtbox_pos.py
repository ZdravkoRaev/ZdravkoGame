import math
from enteties.player.player import Player
def hurtPos(player : Player,mousePos):   
    x=mousePos[0]-player.base.boundingBox.x
    y=mousePos[1]-player.base.boundingBox.y
    lenght=math.sqrt(x*x+y*y)
    player.hurtbox.x=player.base.boundingBox.x+x/lenght*30-13
    player.hurtbox.y=player.base.boundingBox.y+y/lenght*30
    return player
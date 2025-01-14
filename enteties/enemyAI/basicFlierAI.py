from enteties.enemies.basicFlier import BasicFlier
from enteties.player import Player
from math import sqrt
def AI(player :Player, enemy : BasicFlier):
    x1=player.base.boundingBox.x
    x2=enemy.base.boundingBox.x
    y1=player.base.boundingBox.y
    y2=enemy.base.boundingBox.y
    if x1==x2 and y1==y2:
        return enemy
    distance=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    if distance<400:
        
        enemy.base.x_vel=(x1-x2)/distance*3
        enemy.base.y_vel=(y1-y2)/distance*3
    else:
        enemy.base.x_vel*=0.9
        enemy.base.y_vel*=0.9

    return enemy
    

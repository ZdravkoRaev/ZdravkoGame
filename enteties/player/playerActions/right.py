"""a"""
from enteties.player.player import Player
def move_right(player : Player):
    """a"""
    if player.base.wall_below:
        if player.base.x_vel<6:
            player.base.x_vel+=2
    else:
        if player.base.x_vel<6:
            player.base.x_vel+=1

    return player

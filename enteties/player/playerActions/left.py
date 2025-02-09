"""moveing left logic"""
from enteties.player.player import Player
def move_left(player : Player):
    """logic"""
    if player.base.wall_below:
        if player.base.x_vel>-6:
            player.base.x_vel+=-2
    else:
        if player.base.x_vel>-6:
            player.base.x_vel+=-1

    return player

"""a"""
from enteties.player.player import Player
def jump1(player : Player):
    """a"""
    if player.base.wall_below:
        player.base.y_vel=-16
    elif player.base.wall_right:
        player.base.y_vel=-16
        player.base.x_vel=-6
    elif player.base.wall_left:
        player.base.y_vel=-16
        player.base.x_vel=6

    return player

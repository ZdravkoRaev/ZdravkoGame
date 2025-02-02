from enteties.player.player import Player
def jump1(player : Player):
    if player.base.wallBelow:
        player.base.y_vel=-16
    elif player.base.wallRight:
        player.base.y_vel=-16
        player.base.x_vel=-6
    elif player.base.wallLeft:
        player.base.y_vel=-16
        player.base.x_vel=6

    return player
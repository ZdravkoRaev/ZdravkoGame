from enteties.player import Player
def moveLeft(player : Player):
    if player.base.wallBelow:
        if player.base.x_vel>-6:
            player.base.x_vel=-6
    else:
        if player.base.x_vel>-6:
            player.base.x_vel+=-1

    return player
"""a"""
from enteties.player.player import Player
def dashing(player : Player):
    """a"""
    player.base.y_vel-=1
    player.attack_lenght-=1
    if player.attack_lenght==0:
        player.is_dashing=False
        player.attack_lenght=6
        if player.base.x_vel>6:
            player.base.x_vel=6
        if player.base.x_vel<-6:
            player.base.x_vel=-6
        if player.base.y_vel<-6:
            player.base.y_vel=-6
        player.attack_cd=40
    return player

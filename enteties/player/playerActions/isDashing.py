from enteties.player.player import Player
def dashing(player : Player):

    player.base.y_vel-=1
    player.attackLenght-=1
    if player.attackLenght==0:
        player.isDashing=False
        player.attackLenght=3
        if player.base.x_vel>6:
            player.base.x_vel=6
        if player.base.x_vel<-6:
            player.base.x_vel=-6
        if player.base.y_vel<-6:
            player.base.y_vel=-6
        player.attackCooldown=40
    return player
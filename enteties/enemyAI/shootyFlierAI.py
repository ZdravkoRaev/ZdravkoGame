from enteties.enemies.projectile import Projectile
from enteties.enemies.shootyFlier import ShootyFlier
from enteties.player import Player
from math import sqrt
def AI(player :Player, shootyFlier : ShootyFlier):
    shootyFlier.attackCooldown-=1
    shot=None
    if shootyFlier.attackCooldown<0:
        shot=Projectile()
        shot.base.boundingBox.x=shootyFlier.base.boundingBox.x
        shot.base.boundingBox.y=shootyFlier.base.boundingBox.y

        if shootyFlier.base.boundingBox.x==player.base.boundingBox.x and shootyFlier.base.boundingBox.y==player.base.boundingBox.y:
            shot.base.x_vel=1
            shot.base.y_vel=0
        else:
            distance=sqrt((player.base.boundingBox.x-shootyFlier.base.boundingBox.x)*(player.base.boundingBox.x-shootyFlier.base.boundingBox.x)+(player.base.boundingBox.y-shootyFlier.base.boundingBox.y)*(player.base.boundingBox.y-shootyFlier.base.boundingBox.y))
            shot.base.x_vel=(player.base.boundingBox.x-shootyFlier.base.boundingBox.x)/distance*5
            shot.base.y_vel=(player.base.boundingBox.y-shootyFlier.base.boundingBox.y)/distance*5
        shootyFlier.attackCooldown=60
    return list((shootyFlier,shot))
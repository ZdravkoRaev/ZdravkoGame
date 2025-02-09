"""stands in place in the air and shoots the player"""
from math import sqrt
from enteties.base_entety import BaseEntety
from enteties.player.player import Player
from enteties.enemies.projectile import Projectile
class ShootyFlier():
    """class"""
    def __init__(self):
        self.hp=1
        self.ID=2
        self.base=BaseEntety(25,25)
        self.attack_cooldown=60
    def AI(self,player :Player):
        """how the enemy acts"""
        self.attack_cooldown-=1
        shot=None
        if self.attack_cooldown<0:
            shot=Projectile()
            shot.base.boundingBox.x=self.base.boundingBox.x
            shot.base.boundingBox.y=self.base.boundingBox.y

            if self.base.boundingBox.x==player.base.boundingBox.x and\
                  self.base.boundingBox.y==player.base.boundingBox.y:
                shot.base.x_vel=1
                shot.base.y_vel=0
            else:
                distance=sqrt((player.base.boundingBox.x-self.base.boundingBox.x)**2+(player.base.boundingBox.y-self.base.boundingBox.y)**2)
                shot.base.x_vel=(player.base.boundingBox.x-self.base.boundingBox.x)/distance*5
                shot.base.y_vel=(player.base.boundingBox.y-self.base.boundingBox.y)/distance*5
            self.attack_cooldown=60
        return list((self,shot))

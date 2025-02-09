"""stands in place in the air and shoots the player"""
from math import sqrt
from enteties.base_entety import BaseEntety
from enteties.player.player import Player
from enteties.enemies.projectile import Projectile
class ShootyFlier():
    """class"""
    def __init__(self):
        self.hp=1
        self.id=2
        self.base=BaseEntety(25,25)
        self.attack_cooldown=60
    def ai(self,player :Player):
        """how the enemy acts"""
        self.attack_cooldown-=1
        shot=None
        if self.attack_cooldown<0:
            shot=Projectile()
            shot.base.bounding_box.x=self.base.bounding_box.x
            shot.base.bounding_box.y=self.base.bounding_box.y

            if self.base.bounding_box.x==player.base.bounding_box.x and\
                  self.base.bounding_box.y==player.base.bounding_box.y:
                shot.base.x_vel=1
                shot.base.y_vel=0
            else:
                distance=sqrt((player.base.bounding_box.x-self.base.bounding_box.x)**2+(player.base.bounding_box.y-self.base.bounding_box.y)**2)
                shot.base.x_vel=(player.base.bounding_box.x-self.base.bounding_box.x)/distance*5
                shot.base.y_vel=(player.base.bounding_box.y-self.base.bounding_box.y)/distance*5
            self.attack_cooldown=60
        return list((self,shot))

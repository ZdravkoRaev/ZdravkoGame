"""stands in place in the air and shoots the player"""
import os
import math
import pygame
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
        self.standing=pygame.image.load(os.path.join("sprites","enemies","shooty_flier.png")).convert_alpha()
    def ai(self,player :Player):
        """how the enemy acts"""
        self.attack_cooldown-=1
        shot=None
        if self.attack_cooldown<0:
            shot=Projectile()
            shot.base.bounding_box.centerx=self.base.bounding_box.centerx
            shot.base.bounding_box.centery=self.base.bounding_box.centery+20

            if self.base.bounding_box.x==player.base.bounding_box.x and\
                  self.base.bounding_box.y==player.base.bounding_box.y:
                shot.base.x_vel=1
                shot.base.y_vel=0
            else:
                distance=math.sqrt((player.base.bounding_box.x-self.base.bounding_box.x)**2+(player.base.bounding_box.y-self.base.bounding_box.y)**2)
                shot.base.x_vel=(player.base.bounding_box.x-self.base.bounding_box.x)/distance*5
                shot.base.y_vel=(player.base.bounding_box.y-self.base.bounding_box.y)/distance*5
            self.attack_cooldown=60
            shot.rotationx=player.base.bounding_box.centerx-self.base.bounding_box.centerx
            shot.rotationy=player.base.bounding_box.centery-self.base.bounding_box.centery
        return list((self,shot))
    def sprite(self,player:Player):
        wanted=self.standing
        x=player.base.bounding_box.centerx-self.base.bounding_box.centerx
        y=player.base.bounding_box.centery-self.base.bounding_box.centery
        if x<0:
            wanted=pygame.transform.flip(wanted,True,False)
        if x!=0:
            wanted=pygame.transform.rotate(wanted,-math.atan(y/x)*180/math.pi)
        return wanted


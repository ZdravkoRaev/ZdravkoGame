"""chases the player if the player is too close. Deals damage on touch"""
import math
import os
import pygame
from enteties.base_entety import BaseEntety
from enteties.player.player import Player

class BasicFlier():
    """a"""
    def __init__(self):
        self.hp=1
        self.id=1
        self.base=BaseEntety(25,25)
        self.standing=pygame.image.load(os.path.join("sprites","enemies","basic_flier.png")).convert_alpha()


    def ai(self,player :Player):
        """a"""
        x1=player.base.bounding_box.x
        x2=self.base.bounding_box.x
        y1=player.base.bounding_box.y
        y2=self.base.bounding_box.y
        if x1==x2 and y1==y2:
            return self
        distance=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
        if distance<400:

            self.base.x_vel=(x1-x2)/distance*3
            self.base.y_vel=(y1-y2)/distance*3
        else:
            self.base.x_vel*=0.9
            self.base.y_vel*=0.9

        return self
    def sprite(self,player:Player):
        wanted=self.standing
        x=player.base.bounding_box.centerx-self.base.bounding_box.centerx
        y=player.base.bounding_box.centery-self.base.bounding_box.centery
        if x<0:
            wanted=pygame.transform.flip(wanted,True,False)
        if x!=0:
            wanted=pygame.transform.rotate(wanted,-math.atan(y/x)*180/math.pi)
        return wanted


"""a"""
import os
import pygame
import math
from enteties.base_entety import BaseEntety
class Projectile():
    """a"""
    def __init__(self):
        self.hp=1
        self.id=100
        self.base=BaseEntety(5,5)
        self.rotationx=0
        self.rotationy=0
        self.standing=pygame.image.load(os.path.join("sprites","enemies","projectile.png")).convert_alpha()
    def ai(self):
        """a"""
        if self.base.wall_below or self.base.wall_above or self.base.wall_left or self.base.wall_right:
            self.hp=-1
        return self
    def sprite(self,player):
        wanted=self.standing
        if self.rotationx<0:
            wanted=pygame.transform.flip(wanted,True,False)
        if self.rotationx!=0:
            wanted=pygame.transform.rotate(wanted,-math.atan(self.rotationy/self.rotationx)*180/math.pi)

        return wanted
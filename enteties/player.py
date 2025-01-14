from pygame import Rect
from enteties.baseEntety import BaseEntety
class Player:
    def __init__(self):
        self.base=BaseEntety(25,50)
        self.hp=3
        self.invonrabilityFrames=30
        self.attackCooldown=20
        self.canDash=False
        self.isDashing=False
        self.attackLenght=3
        self.hurtbox=Rect((100,100,50,50))
        self.isAttacking=False
        self.invFrames=0
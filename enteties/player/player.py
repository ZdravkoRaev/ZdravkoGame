from pygame import Rect
from enteties.base_entety import BaseEntety
class Player:
    def __init__(self):
        self.base=BaseEntety(25,50)
        self.wallJumpBox=BaseEntety(27,48)

        self.hp=3
        self.invonrabilityFrames=30

        self.attackCooldown=0
        self.canDash=False
        self.isDashing=False
        self.attackLenght=3
        self.hurtbox=Rect((100,100,50,50))
        self.isAttacking=False



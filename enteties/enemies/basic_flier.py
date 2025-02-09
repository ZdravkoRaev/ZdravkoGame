"""chases the player if the player is too close. Deals damage on touch"""
from math import sqrt
from enteties.base_entety import BaseEntety
from enteties.player.player import Player

class BasicFlier():
    """a"""
    def __init__(self):
        self.hp=1
        self.id=1
        self.base=BaseEntety(25,25)


    def ai(self,player :Player):
        """a"""
        x1=player.base.boundingBox.x
        x2=self.base.boundingBox.x
        y1=player.base.boundingBox.y
        y2=self.base.boundingBox.y
        if x1==x2 and y1==y2:
            return self
        distance=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
        if distance<400:

            self.base.x_vel=(x1-x2)/distance*3
            self.base.y_vel=(y1-y2)/distance*3
        else:
            self.base.x_vel*=0.9
            self.base.y_vel*=0.9

        return self

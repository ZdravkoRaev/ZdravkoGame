"""a"""
from enteties.base_entety import BaseEntety
class Projectile():
    """a"""
    def __init__(self):
        self.hp=1
        self.id=100
        self.base=BaseEntety(20,20)
    def ai(self):
        """a"""
        if self.base.wallBelow or self.base.wallAbove or self.base.wallLeft or self.base.wallRight:
            self.hp=-1
        return self



        
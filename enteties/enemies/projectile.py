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
        if self.base.wall_below or self.base.wall_above or self.base.wall_left or self.base.wall_right:
            self.hp=-1
        return self



        
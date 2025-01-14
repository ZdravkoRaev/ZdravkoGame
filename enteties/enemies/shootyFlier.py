#stands in place in the air and shoots the player
from enteties.baseEntety import BaseEntety
class ShootyFlier():
    def __init__(self):
        self.hp=1
        self.ID=2
        self.base=BaseEntety(25,25)
        self.attackCooldown=60
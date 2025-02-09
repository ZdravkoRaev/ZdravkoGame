#stands in place and shoots the player
from enteties.base_entety import BaseEntety
class basicFlier():
    def __init__(self):
        self.hp=1
        self.ID=4
        self.base=BaseEntety(25,25)
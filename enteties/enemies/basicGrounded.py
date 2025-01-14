#goes left and right. Deals damage on touch.
from enteties.baseEntety import BaseEntety
class basicFlier():
    def __init__(self):
        self.hp=1
        self.ID=3
        self.base=BaseEntety(25,25)
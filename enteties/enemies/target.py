"""target that does nothing, but need to be destroyed to finish the level"""
import os
import pygame
from enteties.base_entety import BaseEntety
class Target():
    """stats"""

    def __init__(self):
        self.hp=1
        self.id=0
        self.base=BaseEntety(25,25)
        self.standing=pygame.image.load(os.path.join("sprites","enemies","target.png")).convert_alpha()
    def ai(self):
        """does nothing"""
        return self
    def sprite(self,player):
        return self.standing
"""target that does nothing, but need to be destroyed to finish the level"""
from enteties.base_entety import BaseEntety
class Target():
    """stats"""

    def __init__(self):
        self.hp=1
        self.id=0
        self.base=BaseEntety(25,25)
    def ai(self):
        """does nothing"""
        return self

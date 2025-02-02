from enteties.baseEntety import BaseEntety
class Target():
    def __init__(self):
        self.hp=1
        self.ID=0
        self.base=BaseEntety(25,25)
    def AI(self):
        return self
"""a"""
from pygame import Rect
from enteties.base_entety import BaseEntety
class Player:
    """a"""
    def __init__(self):
        self.base=BaseEntety(25,50)
        self.wall_jump_box=BaseEntety(27,48)

        self.hp=3
        self.i_frames=30

        self.attack_cd=0
        self.cad_dash=False
        self.is_dashing=False
        self.attack_lenght=3
        self.hurtbox=Rect((150,150,75,75))
        self.is_attacking=False

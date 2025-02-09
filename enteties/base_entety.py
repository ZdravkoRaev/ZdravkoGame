"""a"""
import pygame
class BaseEntety:
    """a"""
    def __init__(self,lenght: int,height : int):
        self.bounding_box=pygame.Rect((0,0,lenght,height))
        self.x_vel=0
        self.y_vel=0
        self.wall_below=False
        self.wall_above=False
        self.wall_left=False
        self.wall_right=False

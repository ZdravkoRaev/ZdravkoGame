import pygame
class BaseEntety:
    def __init__(self,lenght: int,height : int):
        self.boundingBox=pygame.Rect((0,0,lenght,height))
        self.x_vel=0
        self.y_vel=0
        self.wallBelow=False
        self.wallAbove=False
        self.wallLeft=False
        self.wallRight=False
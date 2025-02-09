"""a"""
import pygame
import os
from enteties.base_entety import BaseEntety
class Player:
    """a"""
    def __init__(self):
        self.base=BaseEntety(25,50)
        self.wall_jump_box=BaseEntety(27,48)
        self.hp=1
        self.i_frames=30
        self.attack_cd=0
        self.cad_dash=False
        self.is_dashing=False
        self.attack_lenght=3
        self.hurtbox=pygame.Rect((150,150,75,75))
        self.is_attacking=False

        self.walk1=pygame.image.load(os.path.join("sprites","player","walking","walk1.png")).convert_alpha()
        self.walk2=pygame.image.load(os.path.join("sprites","player","walking","walk2.png")).convert_alpha()
        self.walk3=pygame.image.load(os.path.join("sprites","player","walking","walk3.png")).convert_alpha()
        self.walk4=pygame.image.load(os.path.join("sprites","player","walking","walk4.png")).convert_alpha()
        self.walk5=pygame.image.load(os.path.join("sprites","player","walking","walk5.png")).convert_alpha()
        self.walk6=pygame.image.load(os.path.join("sprites","player","walking","walk6.png")).convert_alpha()

        self.stand0=pygame.image.load(os.path.join("sprites","player","standing","stand0.png")).convert_alpha()
        self.stand1=pygame.image.load(os.path.join("sprites","player","standing","stand1.png")).convert_alpha()
        self.stand2=pygame.image.load(os.path.join("sprites","player","standing","stand2.png")).convert_alpha()
        self.stand3=pygame.image.load(os.path.join("sprites","player","standing","stand3.png")).convert_alpha()

        self.jump0=pygame.image.load(os.path.join("sprites","player","jumping","jump0.png")).convert_alpha()
        self.jump1=pygame.image.load(os.path.join("sprites","player","jumping","jump1.png")).convert_alpha()
        self.jump2=pygame.image.load(os.path.join("sprites","player","jumping","jump2.png")).convert_alpha()

        self.slide0=pygame.image.load(os.path.join("sprites","player","wall_sliding","slide0.png")).convert_alpha()
        self.slide1=pygame.image.load(os.path.join("sprites","player","wall_sliding","slide1.png")).convert_alpha()
        self.slide2=pygame.image.load(os.path.join("sprites","player","wall_sliding","slide2.png")).convert_alpha()

    def ai(self):
        pass
    def sprites(self,frame : int):
        wanted=None
        if self.base.wall_below:
            if abs(self.base.x_vel)>0.1:
                if int(frame/3)%6==0:
                    wanted=self.walk1
                elif int(frame/3)%6==1:
                    wanted=self.walk2
                elif int(frame/3)%6==2:
                    wanted=self.walk3
                elif int(frame/3)%6==3:
                    wanted=self.walk4
                elif int(frame/3)%6==4:
                    wanted=self.walk5
                else:
                    wanted=self.walk6
            else:
                if int(frame/12)%4==0:
                    wanted=self.stand0
                elif int(frame/12)%4==1:
                    wanted=self.stand1
                elif int(frame/12)%4==2:
                    wanted=self.stand2
                else:
                    wanted=self.stand3
        else:
            if self.base.wall_left:
                if int(frame/3)%3==0:
                    return self.slide0
                elif int(frame/3)%3==1:
                    return self.slide1
                else:
                    return self.slide2
            elif self.base.wall_right:
                if int(frame/3)%3==0:
                    wanted=self.slide0
                elif int(frame/3)%3==1:
                    wanted=self.slide1
                else:
                    wanted=self.slide2
                wanted=pygame.transform.flip(wanted, True, False)
                return wanted
            else:
                if int(frame/6)%3==0:
                    wanted=self.jump0
                elif int(frame/6)%3==1:
                    wanted=self.jump1
                elif int(frame/6)%3==2:
                    wanted=self.jump2

        if self.base.x_vel<0:
            wanted = pygame.transform.flip(wanted, True, False)
        return wanted
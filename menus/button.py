
class Button():
    def __init__(self,x : int,y : int, lenght : int, height : int, text : str, color : tuple, colorOnHover : tuple, colorOnClick : tuple, actionID : int):
        self.x=x
        self.y=y
        self.lenght=lenght
        self.height=height
        self.text=text
        self.color=color
        self.colorOnHover=colorOnHover
        self.colorOnClick=colorOnClick
        self.actionID=actionID
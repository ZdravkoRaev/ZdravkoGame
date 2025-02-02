from enteties.collisions.collisionsWithLevel import collysions
from enteties.templateEntety import TempalteEntety
def dirCollysions(entety : TempalteEntety,level):
    entety.base.wallBelow=False
    entety.base.wallLeft=False
    entety.base.wallAbove=False
    entety.base.wallRight=False
    entety.base.boundingBox.x+=entety.base.x_vel
    collisions=collysions(entety.base.boundingBox,level)

            
    for item in collisions:
        if entety.base.x_vel>0:
            entety.base.wallRight=True
            entety.base.boundingBox.right=item.left
            entety.base.x_vel=0
        elif entety.base.x_vel<0:
            entety.base.wallLeft=True
            entety.base.boundingBox.left=item.right
            entety.base.x_vel=0
    entety.base.boundingBox.y+=entety.base.y_vel
    collisions=collysions(entety.base.boundingBox,level)
    for item in collisions:
        if entety.base.y_vel>0:
            entety.base.wallBelow=True
            entety.base.boundingBox.bottom=item.top
            entety.base.y_vel=0
        elif entety.base.y_vel<0:
            entety.base.wallAbove=True
            entety.base.boundingBox.top=item.bottom
            entety.base.y_vel=0
    return entety
"""a"""
from enteties.collisions.collisions_with_enteties import collysions
from enteties.template_entety import TempalteEntety
def dir_collisions(entety : TempalteEntety,level):
    """a"""
    entety.base.wall_below=False
    entety.base.wall_left=False
    entety.base.wall_above=False
    entety.base.wall_right=False
    entety.base.bounding_box.x+=entety.base.x_vel
    collisions=collysions(entety.base.bounding_box,level)


    for item in collisions:
        if entety.base.x_vel>0:
            entety.base.wall_right=True
            entety.base.bounding_box.right=item.left
            entety.base.x_vel=0
        elif entety.base.x_vel<0:
            entety.base.wall_left=True
            entety.base.bounding_box.left=item.right
            entety.base.x_vel=0
    entety.base.bounding_box.y+=entety.base.y_vel
    collisions=collysions(entety.base.bounding_box,level)
    for item in collisions:
        if entety.base.y_vel>0:
            entety.base.wall_below=True
            entety.base.bounding_box.bottom=item.top
            entety.base.y_vel=0
        elif entety.base.y_vel<0:
            entety.base.wall_above=True
            entety.base.bounding_box.top=item.bottom
            entety.base.y_vel=0
    return entety

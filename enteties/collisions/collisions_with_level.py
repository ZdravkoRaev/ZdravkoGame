"""a"""
from enteties.template_entety import TempalteEntety

def collisions_enteties(entety1 :TempalteEntety,all_enteties :list[TempalteEntety]):
    """a"""
    collis_ent=list()
    for item in all_enteties:
        if item is not entety1:
            if item.base.bounding_box.x+500>entety1.base.bounding_box.x\
            and item.base.bounding_box.y+500>entety1.base.bounding_box.y\
            and item.base.bounding_box.x-500<entety1.base.bounding_box.x\
            and item.base.bounding_box.y-500<entety1.base.bounding_box.y\
            and entety1.base.bounding_box.colliderect(item.base.bounding_box):
                collis_ent.append(item)
    return collis_ent

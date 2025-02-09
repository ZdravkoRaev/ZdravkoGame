"""a"""
from enteties.template_entety import TempalteEntety

def collisions_enteties(entety1 :TempalteEntety,all_enteties):
    """a"""
    collis_ent=list()
    for item in all_enteties:
        if item is not entety1:
            if item.base.boundingBox.x+500>entety1.base.boundingBox.x\
            and item.base.boundingBox.y+500>entety1.base.boundingBox.y\
            and item.base.boundingBox.x-500<entety1.base.boundingBox.x\
            and item.base.boundingBox.y-500<entety1.base.boundingBox.y\
            and entety1.base.boundingBox.colliderect(item.base.boundingBox):
                collis_ent.append(item)
    return collis_ent

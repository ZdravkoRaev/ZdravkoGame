from enteties.templateEntety import TempalteEntety

def collisionsEnteties(entety1 :TempalteEntety,allEnteties):
    collis_ent=list()
    for item in allEnteties:
        if item is not entety1:
            if entety1.base.boundingBox.colliderect(item.base.boundingBox):
                collis_ent.append(item)
    return collis_ent

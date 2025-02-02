from enteties.basicEntety import TempalteEntety

def collisionsEnteties(entety1 :TempalteEntety,allEnteties):
    collisEnt=list()
    for item in allEnteties:
        if item is not entety1:
            if entety1.base.boundingBox.colliderect(item.base.boundingBox):
                collisEnt.append(item)
    return collisEnt         
              
        

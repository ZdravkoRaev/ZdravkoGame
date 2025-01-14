from enteties.basicEntety import BasicEntety

def collisionsEnteties(entety1 :BasicEntety,allEnteties):
    collisEnt=list()
    for item in allEnteties:
        if item is not entety1:
            if entety1.base.boundingBox.colliderect(item.base.boundingBox):
                collisEnt.append(item)
    return collisEnt         
              
        

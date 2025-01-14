import gameLoop
from levels import converter
def runLevel(levelID : int,screen):
    level=converter.loadLevelFromJson(levelID)
    state=gameLoop.run(level,screen)
    return state


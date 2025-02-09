import game_loop
from levels import converter
def runLevel(levelID : int,screen):
    level=converter.loadLevelFromJson(levelID)
    state=game_loop.run(level,screen)
    return state


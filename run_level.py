"""a"""
import game_loop
from levels import converter
def run_level(level_ID : int,screen):
    """a"""
    level=converter.loadLevelFromJson(level_ID)
    state=game_loop.run(level,screen)
    return state

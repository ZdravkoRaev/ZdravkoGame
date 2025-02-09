"""makes the player attack and then makes him dash if he can"""
from enteties.player.playerActions.dash import dash
from enteties.player.player import Player
def attack(player : Player,mouse_pos):
    """function"""
    player.is_attacking=True
    player=dash(player,mouse_pos)
    return player

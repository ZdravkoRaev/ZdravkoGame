"""makes the player attack and then makes him dash if he can"""
from enteties.player.playerActions.dash import dash
from enteties.player.player import Player
def attack(player : Player,mousePos):
    """function"""
    player.isAttacking=True
    player=dash(player,mousePos)

    
    return player
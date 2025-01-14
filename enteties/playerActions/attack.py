from enteties.playerActions.dash import dash
from enteties.player import Player
def attack(player : Player,mouse,mousePos):
    player.isAttacking=True
    player=dash(player,mouse,mousePos)

    
    return player
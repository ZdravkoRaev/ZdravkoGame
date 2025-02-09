"""converts the pressed keys to actions"""
from pygame import K_d,K_a,K_SPACE
from enteties.player.player import Player

from enteties.player.playerActions.left import moveLeft
from enteties.player.playerActions.right import moveRight
from enteties.player.playerActions.jumping import jump1
from enteties.player.playerActions.attack import attack
from enteties.player.playerActions.isDashing import dashing
from enteties.player.playerActions.hurtboxPosition import hurtPos

def move(player : Player,keys,mouse,mousePos):
    """thee function"""
    if player.base.wallBelow:
        player.canDash=True
        if not keys[K_d] and not keys[K_a]:
            player.base.x_vel*=0.5

    if player.base.wallLeft or player.base.wallRight:
        player.canDash=True

    if player.isAttacking:
        player.attackLenght-=1
        if player.attackLenght<=0:
            player.isAttacking=False
            player.attackLenght=6
            player.attackCooldown=40
    if player.isDashing:
        player=dashing(player)
    if keys[K_d]:
        player=moveRight(player)
    if keys[K_a]:
        player=moveLeft(player)
    if  keys[K_SPACE]:
        player=jump1(player)
    if mouse[2] and player.attackCooldown<0:
        player=attack(player,mousePos)
    player.attackCooldown-=1
    player=hurtPos(player,mousePos)


    return player

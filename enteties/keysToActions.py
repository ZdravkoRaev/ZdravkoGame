
from pygame import K_d,K_a,K_SPACE
from enteties.player import Player
from enteties.playerActions.left import moveLeft
from enteties.playerActions.right import moveRight
from enteties.playerActions.jumping import jump1
from enteties.playerActions.attack import attack
from enteties.playerActions.isDashing import dashing
from enteties.playerActions.hurtboxPosition import hurtPos
def move(player : Player,keys,mouse,mousePos):
    if player.base.wallBelow:
        player.base.x_vel=0
        player.canDash=True
    if player.base.wallLeft:
        player.canDash=True
    if player.base.wallRight:
        player.canDash=True

    if player.isAttacking:
        player.attackLenght-=1
        if player.attackLenght==0:
            player.isAttacking=False
            player.attackLenght=5
    if player.isDashing:
        player=dashing(player)
    if keys[K_d]:
        player=moveRight(player)
    if keys[K_a]:
        player=moveLeft(player)
    if  keys[K_SPACE]:
        player=jump1(player)
    if mouse[2] and player.attackCooldown<0:
        player=attack(player,mouse,mousePos)
    player=hurtPos(player,mousePos)


    return player
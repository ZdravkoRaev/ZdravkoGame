"""converts the pressed keys to actions"""
import pygame
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
        if not keys[pygame.K_d] and not keys[pygame.K_a]: # pylint: disable=maybe-no-member
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
    if keys[pygame.K_d]: # pylint: disable=maybe-no-member
        player=moveRight(player)
    if keys[pygame.K_a]: # pylint: disable=maybe-no-member
        player=moveLeft(player)
    if  keys[pygame.K_SPACE]: # pylint: disable=maybe-no-member
        player=jump1(player)
    if mouse[2] and player.attackCooldown<0:
        player=attack(player,mousePos)
    player.attackCooldown-=1
    player=hurtPos(player,mousePos)


    return player

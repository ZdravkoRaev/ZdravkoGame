"""converts the pressed keys to actions"""
import pygame
from enteties.player.player import Player

from enteties.player.playerActions.left import move_left
from enteties.player.playerActions.right import move_right
from enteties.player.playerActions.jumping import jump1
from enteties.player.playerActions.attack import attack
from enteties.player.playerActions.is_dashing import dashing
from enteties.player.playerActions.hurtbox_pos import hurt_pos

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
        player=move_right(player)
    if keys[pygame.K_a]: # pylint: disable=maybe-no-member
        player=move_left(player)
    if  keys[pygame.K_SPACE]: # pylint: disable=maybe-no-member
        player=jump1(player)
    if mouse[2] and player.attackCooldown<0:
        player=attack(player,mousePos)
    player.attackCooldown-=1
    player=hurt_pos(player,mousePos)


    return player

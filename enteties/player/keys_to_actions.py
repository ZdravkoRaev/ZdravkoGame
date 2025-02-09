"""converts the pressed keys to actions"""
import pygame
from enteties.player.player import Player

from enteties.player.playerActions.left import move_left
from enteties.player.playerActions.right import move_right
from enteties.player.playerActions.jumping import jump1
from enteties.player.playerActions.attack import attack
from enteties.player.playerActions.is_dashing import dashing
from enteties.player.playerActions.hurtbox_pos import hurt_pos

def move(player : Player,keys,mouse,mouse_pos):
    """thee function"""
    if player.base.wall_below:
        player.cad_dash=True
        if not keys[pygame.K_d] and not keys[pygame.K_a]: # pylint: disable=maybe-no-member
            player.base.x_vel*=0.5

    if player.base.wall_left or player.base.wall_right:
        player.cad_dash=True

    if player.is_attacking:
        player.attack_lenght-=1
        if player.attack_lenght<=0:
            player.is_attacking=False
            player.attack_lenght=6
            player.attack_cd=25
    if player.is_dashing:
        player=dashing(player)
    if keys[pygame.K_d]: # pylint: disable=maybe-no-member
        player=move_right(player)
    if keys[pygame.K_a]: # pylint: disable=maybe-no-member
        player=move_left(player)
    if  keys[pygame.K_SPACE]: # pylint: disable=maybe-no-member
        player=jump1(player)
    if mouse[2] and player.attack_cd<0:
        player=attack(player,mouse_pos)
    player.attack_cd-=1
    player=hurt_pos(player,mouse_pos)


    return player

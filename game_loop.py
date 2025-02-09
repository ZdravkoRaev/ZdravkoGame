"""a"""
import pygame
from levelCreator.level import Level
from enteties.player.player import Player
from enteties.player.keys_to_actions import move
from drawing import draw
from drawing import drawStart
from enteties import collisions
from enteties.enemies.enemyAI.sorter import sort_ai
def run(level: Level, screen):
    """a"""
    x_camera=0
    y_camera=0
    clock = pygame.time.Clock()
    player=Player()
    enemies=list()
    running=True
    player.base.bounding_box.x=100
    player.base.bounding_box.y=800
    surface=screen.copy()
    enemies=drawStart(surface,player,level,enemies)
    frame=0

    while running:
        frame+=1
        clock.tick(60)


        #getting the player imput
        keys=pygame.key.get_pressed()
        mouse=pygame.mouse.get_pressed()
        mouse_pos=list(pygame.mouse.get_pos())

        #converting the mouse pos to match the displayed image
        mouse_pos[0]=mouse_pos[0]/2-(-x_camera+800)/2
        mouse_pos[1]=mouse_pos[1]/2-(-y_camera+450)/2


        surface=screen.copy()
        surface.fill((100, 100, 100))
        draw(surface,player,level,enemies,frame)
        for item in enemies:
            if item.hp<=0:
                enemies.remove(item) # pylint: disable = modified-iterating-list
            new_enemies=sort_ai(player,item)
            item=new_enemies[0]
            item=collisions.dir_collisions(item,level)
            if new_enemies[1] is not None:
                enemies.append(new_enemies[1]) # pylint: disable = modified-iterating-list

        player=move(player,keys,mouse,mouse_pos)
        enemy_col=collisions.collisions_enteties(player,enemies)
        if player.is_attacking:
            for item in enemies:
                if player.hurtbox.colliderect(item.base.bounding_box):
                    item.hp-=1
                    if item.hp<=0:
                        enemies.remove(item) # pylint: disable = modified-iterating-list
        if enemy_col and player.i_frames<=0:
            player.hp-=1
            player.i_frames=60
        player.i_frames-=1

        if player.is_attacking:
            collisions_attack=collisions.collysions_with_level(player.hurtbox,level) # pylint: disable = modified-iterating-list
            for item in collisions_attack:
                if level.objects[int(item.x/25)][int(item.y/25)]==2:
                    level.objects[int(item.x/25)][int(item.y/25)]=0
        #gravity
        player=collisions.dir_collisions(player,level)
        if player.base.y_vel<10:
            player.base.y_vel+=1

        #making wallSlides/wallJumps better

        player.wall_jump_box.bounding_box.x=player.base.bounding_box.x-1
        player.wall_jump_box.bounding_box.y=player.base.bounding_box.y+1
        wall_stuff=collisions.collysions_with_level(player.wall_jump_box.bounding_box,level)
        if   player.base.y_vel>2 and wall_stuff:
            player.base.y_vel=2
            for item in wall_stuff:
                if item.x<player.base.bounding_box.x:
                    player.base.wall_left=True
                else:
                    player.base.wall_right=True

        #camera controls
        x_camera=player.base.bounding_box.x*2+25+(pygame.mouse.get_pos()[0]-800)/8
        y_camera=player.base.bounding_box.y*2+50+(pygame.mouse.get_pos()[1]-450)/16
        surface=pygame.transform.scale\
            (surface, (screen.get_rect().size[0]*2,screen.get_rect().size[1]*2))

        #making sure the camera doesn't show stuff out of the level
        if x_camera<800:
            x_camera=800
        elif x_camera>2400:
            x_camera=2400
        if y_camera<450:
            y_camera=450
        elif y_camera>1350:
            y_camera=1350

        screen.blit(surface,(-x_camera+800,-y_camera+450))


        for event in pygame.event.get():
            if event.type==pygame.QUIT: # pylint: disable=maybe-no-member
                running=False
        if not enemies:
            running=False

    return 0

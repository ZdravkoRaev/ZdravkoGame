import pygame
from levelCreator.level import Level
from enteties.player.player import Player
from enteties.player.keys_to_actions import move
from drawing import draw
from drawing import drawStart
from enteties.collisions.collisions_with_enteties import collysions
from enteties.collisions.directional_collisions import dirCollysions
from enteties.collisions.collisions_with_level import collisionsEnteties
from enteties.enemies.enemyAI.sorter import sortAI
def run(theLevel: Level, screen):
    x_camera=0
    y_camera=0
    clock = pygame.time.Clock()
    player=Player()
    enemies=list()
    running=True
    player.base.boundingBox.x=200
    player.base.boundingBox.y=200
    surface=screen.copy()
    enemies=drawStart(surface,player,theLevel,enemies)

    while running:
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
        draw(surface,player,theLevel,enemies)
        for item in enemies:
            if item.hp<=0:
                enemies.remove(item)
            new_enemies=sortAI(player,item)
            item=new_enemies[0]
            item=dirCollysions(item,theLevel)
            if new_enemies[1] is not None:
                enemies.append(new_enemies[1])

        player=move(player,keys,mouse,mouse_pos)
        enemy_col=collisionsEnteties(player,enemies)
        if player.isAttacking:
            for item in enemies:
                if player.hurtbox.colliderect(item.base.boundingBox):
                    item.hp-=1
                    if item.hp<=0:
                        enemies.remove(item)
        if enemy_col and player.invonrabilityFrames<=0:
            player.hp-=1
            player.invonrabilityFrames=60
        player.invonrabilityFrames-=1

        if player.isAttacking:
            collisions=collysions(player.hurtbox,theLevel)
            for item in collisions:
                if theLevel.objects[int(item.x/25)][int(item.y/25)]==2:
                    theLevel.objects[int(item.x/25)][int(item.y/25)]=0
        #gravity
        player=dirCollysions(player,theLevel)
        if player.base.y_vel<10:
            player.base.y_vel+=1
        
        #making wallSlides/wallJumps better
        
        player.wallJumpBox.boundingBox.x=player.base.boundingBox.x-1
        player.wallJumpBox.boundingBox.y=player.base.boundingBox.y+1
        wall_stuff=collysions(player.wallJumpBox.boundingBox,theLevel)
        if   player.base.y_vel>2 and wall_stuff:
            player.base.y_vel=2
            for item in wall_stuff:
                if item.x<player.base.boundingBox.x:
                    player.base.wallLeft=True
                else:
                    player.base.wallRight=True

        #camera controls
        x_camera=player.base.boundingBox.x*2+25+(pygame.mouse.get_pos()[0]-800)/8
        y_camera=player.base.boundingBox.y*2+50+(pygame.mouse.get_pos()[1]-450)/16
        surface=pygame.transform.scale(surface, (screen.get_rect().size[0]*2,screen.get_rect().size[1]*2))

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
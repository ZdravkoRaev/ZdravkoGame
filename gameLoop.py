import pygame
from levelCreator.level import Level
from enteties.player import Player
from enteties.playerWallJump import PlayerWallJump
from enteties.keysToActions import move
from drawing import draw
from enteties.collisionsWithLevel import collysions
from enteties.directionalColisions import dirCollysions
from enteties.collisionsWithEnteties import collisionsEnteties
from enteties.enemyAI.sorter import sortAI
def run(theLevel: Level, screen):
    theLevel.objects[0][0]=5
    x_camera=0
    y_camera=0
    clock = pygame.time.Clock()
    player=Player()
    player_wall=PlayerWallJump()
    enemies=list()
    running=True
    player.base.boundingBox.x=200
    player.base.boundingBox.y=200
    while running:
        keys=pygame.key.get_pressed()
        mouse=pygame.mouse.get_pressed()
        mouse_pos=list(pygame.mouse.get_pos())
        mouse_pos[0]=mouse_pos[0]/2-(-x_camera+800)/2
        mouse_pos[1]=mouse_pos[1]/2-(-y_camera+450)/2
        surface=screen.copy()
        surface.fill((100, 100, 100))
        enemies=draw(surface,player,player_wall,theLevel,enemies)
        for item in enemies:
            if item.hp<=0:
                enemies.remove(item)
            newSTuff=sortAI(player,item)
            item=newSTuff[0]
            item=dirCollysions(item,theLevel)
            if newSTuff[1] is not None:
                enemies.append(newSTuff[1])

        player=move(player,keys,mouse,mouse_pos)
        enemyCol=collisionsEnteties(player,enemies)
        if player.isAttacking:
            for item in enemies:
                if player.hurtbox.colliderect(item.base.boundingBox):
                    item.hp-=1
                    if item.hp<=0:
                        enemies.remove(item)
        if enemyCol and player.invonrabilityFrames<=0:
            player.hp-=1
            player.invonrabilityFrames=60
        player.invonrabilityFrames-=1

        if player.isAttacking:
            collisions=collysions(player.hurtbox,theLevel)
            for item in collisions:
                if theLevel.objects[int(item.x/25)][int(item.y/25)]==2:
                    theLevel.objects[int(item.x/25)][int(item.y/25)]=0
        clock.tick(60)
        player=dirCollysions(player,theLevel)

        if player.base.y_vel<10:
            player.base.y_vel+=1
        pos=mouse_pos
        pos[0]=int((pos[0]-pos[0]%25)/25)
        pos[1]=int((pos[1]-pos[1]%25)/25)

        if  keys[pygame.K_1]:
          if pos[0]>=0 and pos[0]<=63 and pos[1]>=0 and pos[1]<=35: 
                theLevel.objects[mouse_pos[0]][mouse_pos[1]]=1
        if  keys[pygame.K_2]:
            theLevel.objects[mouse_pos[0]][mouse_pos[1]]=2
        if  keys[pygame.K_3]:
            theLevel.objects[mouse_pos[0]][mouse_pos[1]]=3
        if  keys[pygame.K_4]:
            theLevel.objects[mouse_pos[0]][mouse_pos[1]]=4
        if  keys[pygame.K_5]:
            theLevel.objects[mouse_pos[0]][mouse_pos[1]]=5

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        if not enemies:
            running=False

        x_camera=player.base.boundingBox.x*2+25+(pygame.mouse.get_pos()[0]-800)/8
        y_camera=player.base.boundingBox.y*2+50+(pygame.mouse.get_pos()[1]-450)/16
        surface=pygame.transform.scale(surface, (screen.get_rect().size[0]*2,screen.get_rect().size[1]*2))
        if x_camera<800:
            x_camera=800
        elif x_camera>2400:
            x_camera=2400
        if y_camera<450:
            y_camera=450
        elif y_camera>1350:
            y_camera=1350
        screen.blit(surface,(-x_camera+800,-y_camera+450))
        player_wall.base.boundingBox.x=player.base.boundingBox.x-1
        player_wall.base.boundingBox.y=player.base.boundingBox.y+1
        wall_stuff=collysions(player_wall.base.boundingBox,theLevel)
        if   player.base.y_vel>2 and wall_stuff:
            player.base.y_vel=2
            for item in wall_stuff:
                if item.x<player.base.boundingBox.x:
                    player.base.wallLeft=True
                else:
                    player.base.wallRight=True
    return 0
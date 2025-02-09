import pygame
def draw(screen,level):
    screen.fill((0,0,0))
    pygame.display.update()

    for x in range(64):
        for y in range(36):

            if level.objects[x][y]==3:
                a=pygame.Rect((x*25,y*25,25,25))
                pygame.draw.rect(screen,(255,0,0),a)
            if level.objects[x][y]==1:
                a=pygame.Rect((x*25,y*25,25,25))
                pygame.draw.rect(screen,(0,0,255),a)
            if level.objects[x][y]==4:
                a=pygame.Rect((x*25,y*25,25,25))
                pygame.draw.rect(screen,(255,0,255),a)
            if level.objects[x][y]==5:
                a=pygame.Rect((x*25,y*25,25,25))
                pygame.draw.rect(screen,(255,255,0),a)
            if level.objects[x][y]==6:
                a=pygame.Rect((x*25,y*25,25,25))
                pygame.draw.rect(screen,(200,200,200),a)

            if level.objects[x][y]==2:
                a=pygame.Rect((x*25,y*25,25,25))
                pygame.draw.rect(screen,(0,255,255),a)

    for x in range(64):
        for y in range(36):
            pygame.draw.rect(screen,(255,255,255),pygame.Rect((x*25,y*25,1,1)))

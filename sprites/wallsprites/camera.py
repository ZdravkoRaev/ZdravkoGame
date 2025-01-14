import pygame
def main(xCamera,yCamera):

    display_win=pygame.display.set_mode((1600,900))
    surface=display_win.copy()
    surface.fill((100, 100, 100))
    surface=pygame.transform.scale(surface, (display_win.get_rect().size[0]*2,display_win.get_rect().size[1]*2))
    if xCamera<800:
        xCamera=800
    elif xCamera>1600:
        xCamera=1600
    if yCamera<450:
        yCamera=450
    elif yCamera>900:
        yCamera=900
    display_win.blit(surface,(-xCamera,-yCamera+450))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        yCamera-=6
    if keys[pygame.K_a]:
        xCamera-=6
    if keys[pygame.K_s]:
        yCamera+=6
    if keys[pygame.K_d]:
        xCamera+=6


main(0,0)
    




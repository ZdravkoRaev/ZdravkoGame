import drawSprite
import pygame
clock = pygame.time.Clock()
surface = pygame.display.set_mode((1600, 900))
while True:

    clock.tick(60)
    surface.fill((110,110,110))
    drawSprite.draw(0,100,100,surface)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    pygame.display.update()
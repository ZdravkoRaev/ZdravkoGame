import pygame
from menus.button import Button

def renderButton(button1: Button, bg, state : int, pressed,mouse_x: int,mouse_y: int):
    pygame.font.init()
    font1 = pygame.font.Font(None, 24)
    button_text = font1.render(button1.text, True, (0, 0, 0))
    button = pygame.draw.rect(bg,(100,100,100),(button1.x, button1.y, button1.lenght, button1.height))
    button_text_rect = button_text.get_rect(center=button.center)

    button = pygame.draw.rect(
        bg,
        (100,100,100),
        (button1.x, button1.y,
        button1.lenght, button1.height),
    )
    bg.blit(button_text, button_text_rect)
    # Check if button was hovored
    if button.collidepoint(mouse_x, mouse_y):
        button = pygame.draw.rect(
        bg,
        (150,150,150),
        (button1.x, button1.y,
        button1.lenght, button1.height),
    )
        bg.blit(button_text, button_text_rect)
        if pressed[1] == 1 and not pressed[0]:
            button = pygame.draw.rect(
            bg,
            (255,0,0),
            (button1.x, button1.y,
            button1.lenght, button1.height)
            )
            bg.blit(button_text, button_text_rect)
            return button1.actionID
    return state

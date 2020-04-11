import pygame
import button
import inputsys
from constants import INPUT_OK_BUTTON, FPS, WIDTH, HEIGHT, SCREEN_DARKEN, SCREEN_DARKEN_ALPHA, INPUT_BACK_BUTTON
import os


def show_power_menu(main_menu_buttons: button.ButtonRenderer, clock: pygame.time.Clock,
                    dsp: pygame.Surface, bg_image: pygame.Surface, font: pygame.font.Font):

    in_menu = True

    power_buttons = button.ButtonRenderer(True)
    power_buttons.buttons.append(button.Button("Shutdown", WIDTH / 2, HEIGHT * (3/8), font))
    power_buttons.buttons.append(button.Button("Reboot", WIDTH / 2, HEIGHT * (5 / 8), font))
    power_buttons.active_button = 0

    power_buttons.buttons[0].on_click = lambda: os.system("sudo shutdown -h now")
    power_buttons.buttons[1].on_click = lambda: os.system("sudo shutdown -r now")

    power_buttons.snap_position()

    while in_menu:
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_menu = False
                if event.key == pygame.K_RETURN:
                    clicked = True
            if event.type == pygame.JOYBUTTONDOWN:
                if inputsys.joystick_count:
                    if inputsys.joy_in.get_button(INPUT_OK_BUTTON):
                        clicked = True
                    elif inputsys.joy_in.get_button(INPUT_BACK_BUTTON):
                        in_menu = False

        power_buttons.update(clicked)

        dsp.fill((0, 0, 0))
        dsp.blit(bg_image, (0, 0))

        main_menu_buttons.draw(dsp, font)

        grey_screen(dsp)

        power_buttons.draw(dsp, font)

        pygame.display.update()
        clock.tick(FPS)


def grey_screen(dsp: pygame.Surface):
    surf = pygame.Surface((dsp.get_width(), dsp.get_height()))
    surf.fill(SCREEN_DARKEN)
    surf.set_alpha(SCREEN_DARKEN_ALPHA)
    rect = surf.get_rect()
    rect.x = rect.y = 0
    dsp.blit(surf, rect)

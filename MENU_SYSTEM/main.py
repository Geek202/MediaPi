import pygame

import subprocess
import sys

import button
import inputsys
import power_menu
from constants import WIDTH, HEIGHT, BACKGROUND_WALLPAPER, INPUT_OK_BUTTON, FPS


# FUNCTIONS
def draw_display():
    text: pygame.Surface = font.render("Steamlink", True, (255, 255, 255))
    text_rect: pygame.Rect = text.get_rect()
    text_rect.centerx = WIDTH / 2
    text_rect.centery = HEIGHT / 2

    background_rect = text_rect.copy()
    background_rect.inflate(512, 512)

    background_surf = pygame.Surface((background_rect.width, background_rect.height))
    background_surf.fill(transp_bg)
    background_surf.set_alpha(96)

    display.blit(text, text_rect)
    display.blit(background_surf, background_rect)


def start(name):
    print("Starting:", name)
    p = subprocess.Popen([name])
    pygame.quit()
    p.wait()
    exit()


pygame.init()

display = pygame.display.set_mode([WIDTH, HEIGHT], pygame.FULLSCREEN)

bg_image = pygame.image.load(BACKGROUND_WALLPAPER)
# noinspection PyArgumentList
transp_bg = pygame.color.Color(255, 255, 255)

clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 72)

pygame.mouse.set_visible(False)


btn_manager = button.ButtonRenderer(False)
btn_manager.buttons.append(button.Button("Steamlink", WIDTH/4, HEIGHT/2, font))
btn_manager.buttons.append(button.Button("Kodi", WIDTH/2, HEIGHT/2, font))
btn_manager.buttons.append(button.Button("Power", WIDTH*3/4, HEIGHT/2, font))
btn_manager.active_button = 1

btn_manager.buttons[0].on_click = lambda: start("steamlink")
btn_manager.buttons[1].on_click = lambda: start("kodi")
btn_manager.buttons[2].on_click = lambda: power_menu.show_power_menu(btn_manager, clock, display, bg_image, font)

btn_manager.snap_position()

running = True
while running:
    clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                clicked = True
        if event.type == pygame.JOYBUTTONDOWN:
            if inputsys.joystick_count and inputsys.joy_in.get_button(INPUT_OK_BUTTON):
                clicked = True

    display.fill((0, 0, 0))
    display.blit(bg_image, (0, 0))

    # draw_display()
    btn_manager.update(clicked)
    btn_manager.draw(display, font)
    pygame.display.update()

    clock.tick(FPS)

sys.exit(-1)

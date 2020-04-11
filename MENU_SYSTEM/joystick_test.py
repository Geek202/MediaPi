import pygame
import constants
import sys

pygame.init()
pygame.joystick.init()

def check_controller():
    pygame.joystick.quit()
    pygame.joystick.init()
    return pygame.joystick.get_count() != 0


running = not check_controller()
if not running:
    sys.exit()

dsp: pygame.Surface = pygame.display.set_mode([constants.WIDTH, constants.HEIGHT], pygame.FULLSCREEN)

wallpaper_surf = pygame.image.load(constants.BACKGROUND_WALLPAPER)
wallpaper_rect = wallpaper_surf.get_rect()
wallpaper_rect.x = wallpaper_rect.y = 0

clock = pygame.time.Clock()

font = pygame.font.Font(pygame.font.get_default_font(), 96)
text_surf: pygame.Surface = font.render("Waiting for controller to connect...", True, constants.BUTTON_FONT_COLOUR)
text_rect: pygame.Rect = text_surf.get_rect()
text_rect.centerx = constants.WIDTH/2
text_rect.centery = constants.HEIGHT/2


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    if check_controller():
        running = False

    dsp.fill(pygame.color.THECOLORS['black'])
    dsp.blit(wallpaper_surf, wallpaper_rect)
    dsp.blit(text_surf, text_rect)

    pygame.display.update()
    clock.tick(10)

import pygame
import inputsys
import constants

# noinspection PyArgumentList
transparent_bg = pygame.color.Color(138, 43, 226)
# noinspection PyArgumentList
font_colour = pygame.color.Color(64, 224, 208)


class Button:
    def __init__(self, text, x, y, font: pygame.font.Font):
        self.text = text
        self.x, self.y = x, y
        self.w, self.h = font.size(self.text)

    def draw_to_surface(self, dsp: pygame.Surface, font):
        text: pygame.Surface = font.render(self.text, True, font_colour)
        text_rect: pygame.Rect = text.get_rect()
        text_rect.centerx = self.x
        text_rect.centery = self.y

        dsp.blit(text, text_rect)

        '''if self.w < 0:
            self.w, self.h = text_rect.w, text_rect.h'''

        return text_rect

    def on_click(self):
        raise NotImplementedError("on_click")


class ButtonRenderer:
    def __init__(self, vertical):
        self.buttons = list()
        self.vertical = vertical
        self.active_button = -1
        self.selection_x = self.selection_y = 0
        self.selection_w = self.selection_h = 0
        self.selection_target_x = self.selection_target_y = 0
        self.selection_target_w = self.selection_target_h = 0

    # noinspection PyArgumentList
    def update(self, clicked):
        if self.active_button < 0 or self.active_button >= len(self.buttons):
            return

        x, y = inputsys.check_input()
        move = y if self.vertical else x
        self.active_button += move
        if self.active_button < 0:
            self.active_button = 0
        if self.active_button >= len(self.buttons):
            self.active_button = len(self.buttons) - 1

        btn = self.buttons[self.active_button]
        self.selection_target_x, self.selection_target_y = btn.x, btn.y
        self.selection_target_w, self.selection_target_h = btn.w, btn.h

        current_pos = pygame.Vector2(self.selection_x, self.selection_y)
        target_pos = pygame.Vector2(self.selection_target_x, self.selection_target_y)
        new_pos = current_pos.lerp(target_pos, constants.BUTTON_MOVE_SPEED)
        self.selection_x = new_pos.x
        self.selection_y = new_pos.y

        current_size = pygame.Vector2(self.selection_w, self.selection_h)
        target_size = pygame.Vector2(self.selection_target_w, self.selection_target_h)
        new_pos = current_size.lerp(target_size, constants.BUTTON_MOVE_SPEED)
        self.selection_w = new_pos.x
        self.selection_h = new_pos.y

        if clicked:
            btn.on_click()

    def draw(self, dsp, font):
        for i, button in enumerate(self.buttons):
            rect = button.draw_to_surface(dsp, font)
            if i == self.active_button:
                background_rect = rect.copy()
                background_rect.width = self.selection_w
                background_rect.height = self.selection_h
                background_rect.width += constants.BUTTON_EXPAND_WIDTH
                background_rect.height += constants.BUTTON_EXPAND_HEIGHT
                background_rect.center = (self.selection_x, self.selection_y)

                background_surf = pygame.Surface((background_rect.width, background_rect.height))
                background_surf.fill(transparent_bg)
                background_surf.set_alpha(96)

                dsp.blit(background_surf, background_rect)

    def snap_position(self):
        btn: Button = self.buttons[self.active_button]
        self.selection_target_x, self.selection_target_y = btn.x, btn.y
        self.selection_target_w, self.selection_target_h = btn.w, btn.h

        self.selection_x, self.selection_y = self.selection_target_x, self.selection_target_y
        self.selection_w, self.selection_h = self.selection_target_w, self.selection_target_h

from pygame import key, joystick
from pygame.locals import *

def restart():
    global joy_in, joystick_count
    joystick.init()
    joystick_count = joystick.get_count()

    if joystick_count > 0:
        joy_in = joystick.Joystick(0)
        joy_in.init()

restart()

def check_input():
    global joy_in, joystick_count
    x_axis = y_axis = 0
    if joystick_count > 0:
        x_axis = joy_in.get_axis(0)
        y_axis = joy_in.get_axis(1)
    move_x = move_y = 0
    if key.get_pressed()[K_LEFT] or x_axis < -0.8:
        move_x = -1
    if key.get_pressed()[K_RIGHT] or x_axis > 0.8:
        move_x = 1
    if key.get_pressed()[K_UP] or y_axis < -0.8:
        move_y = -1
    if key.get_pressed()[K_DOWN] or y_axis > 0.8:
        move_y = 1
    return move_x, move_y

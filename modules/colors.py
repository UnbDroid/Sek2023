from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port

from modules.variables import *

color_sensor_floor_left = ColorSensor(Port.S2)
color_sensor_floor_right = ColorSensor(Port.S1)
# color_sensor_floor_aux = ColorSensor(Port.S4) #!!!!!!!!!!!!

cor_vista = ""

# Get colors  ----------------------------------------------

def red_left():
    return color_sensor_floor_left.rgb()[0]

def green_left():
    return color_sensor_floor_left.rgb()[1]

def blue_left():
    return color_sensor_floor_left.rgb()[2]

def red_right():
    return color_sensor_floor_right.rgb()[0]

def green_right():
    return color_sensor_floor_right.rgb()[1]

def blue_right():
    return color_sensor_floor_right.rgb()[2]

# def red_aux():
#     return color_sensor_floor_aux.rgb()[0]

# def green_aux():
#     return color_sensor_floor_aux.rgb()[1]

# def blue_aux():
#     return color_sensor_floor_aux.rgb()[2]

# Atomação thamires.13 ------------------------------------------------------------------

range_max_black_left = get_range_colors(range_black_left(), 'max')
range_min_black_left = get_range_colors(range_black_left(), 'min')

range_max_black_right = get_range_colors(range_black_right(), 'max')
range_min_black_right = get_range_colors(range_black_right(), 'min')

# -----------------------------------------------

range_max_yellow_left = get_range_colors(range_yellow_left(), 'max')
range_min_yellow_left = get_range_colors(range_yellow_left(), 'min')

range_max_yellow_right = get_range_colors(range_yellow_right(), 'max')
range_min_yellow_right = get_range_colors(range_yellow_right(), 'min')

# -----------------------------------------------

range_max_blue_left = get_range_colors(range_blue_left(), 'max')
range_min_blue_left = get_range_colors(range_blue_left(), 'min')

range_max_blue_right = get_range_colors(range_blue_right(), 'max')
range_min_blue_right = get_range_colors(range_blue_right(), 'min')

# -----------------------------------------------

range_max_red_left = get_range_colors(range_red_left(), 'max')
range_min_red_left = get_range_colors(range_red_left(), 'min')

range_max_red_right = get_range_colors(range_red_right(), 'max')
range_min_red_right = get_range_colors(range_red_right(), 'min')

# -----------------------------------------------

range_max_meio_blue_left = get_range_colors(range_meio_blue_left(), 'max')
range_min_meio_blue_left = get_range_colors(range_meio_blue_left(), 'min')

range_max_meio_blue_right = get_range_colors(range_meio_blue_right(), 'max')
range_min_meio_blue_right = get_range_colors(range_meio_blue_right(), 'min')

# Range das cores ------------------------------------------------------------------------
 
## MEIO ##

def is_meio_left():
    return range_min_meio_blue_left[0] <= red_left() <= range_max_meio_blue_left[0] and range_min_meio_blue_left[1] <= green_left() <= range_max_meio_blue_left[1] and range_min_meio_blue_left[2] <= blue_left() <= range_max_meio_blue_left[2]

def is_meio_right():
    return range_min_meio_blue_right[0] <= red_right() <= range_max_meio_blue_right[0] and range_min_meio_blue_right[1] <= green_right() <= range_max_meio_blue_right[1] and range_min_meio_blue_right[2] <= blue_right() <= range_max_meio_blue_right[2]

def is_meio():
    return is_meio_left() and is_meio_right() 
 
 
## BLACK ##


def is_black_left():
    return range_min_black_left[0] <= red_left() <= range_max_black_left[0] and range_min_black_left[1] <= green_left() <= range_max_black_left[1] and range_min_black_left[2] <= blue_left() <= range_max_black_left[2]

def is_black_right():
    return range_min_black_right[0] <= red_right() <= range_max_black_right[0] and range_min_black_right[1] <= green_right() <= range_max_black_right[1] and range_min_black_right[2] <= blue_right() <= range_max_black_right[2]

def is_black():
    return is_black_left() and is_black_right()


## YELLOW ##


def is_yellow_left():
    return range_min_yellow_left[0] <= red_left() <= range_max_yellow_left[0] and range_min_yellow_left[1] <= green_left() <= range_max_yellow_left[1] and range_min_yellow_left[2] <= blue_left() <= range_max_yellow_left[2]

def is_yellow_right():
    return range_min_yellow_right[0] <= red_right() <= range_max_yellow_right[0] and range_min_yellow_right[1] <= green_right() <= range_max_yellow_right[1] and range_min_yellow_right[2] <= blue_right() <= range_max_yellow_right[2]

def is_yellow():
    return is_yellow_left() and is_yellow_right()

## BLUE ##


def is_blue_left():
    return range_min_blue_left[0] <= red_left() <= range_max_blue_left[0] and range_min_blue_left[1] <= green_left() <= range_max_blue_left[1] and range_min_blue_left[2] <= blue_left() <= range_max_blue_left[2]

def is_blue_right():
    return range_min_blue_right[0] <= red_right() <= range_max_blue_right[0] and range_min_blue_right[1] <= green_right() <= range_max_blue_right[1] and range_min_blue_right[2] <= blue_right() <= range_max_blue_right[2]

def is_blue():
    return is_blue_left() and is_blue_right()

## RED ##


def is_red_left():
    return range_min_red_left[0] <= red_left() <= range_max_red_left[0] and range_min_red_left[1] <= green_left() <= range_max_red_left[1] and range_min_red_left[2] <= blue_left() <= range_max_red_left[2]

def is_red_right():
    return range_min_red_right[0] <= red_right() <= range_max_red_right[0] and range_min_red_right[1] <= green_right() <= range_max_red_right[1] and range_min_red_right[2] <= blue_right() <= range_max_red_right[2]

def is_red():
    return is_red_left() and is_red_right()


## BROWN ##

rage_max_brown_left = [30, 30, 30]
rage_min_brown_left = [0, 0, 0]

range_max_brown_right = [30, 30, 30]
range_min_brown_right = [0, 0, 0]

def is_brown_left():
    return range_min_brown_left[0] <= red_left() <= range_max_brown_left[0] and range_min_brown_left[1] <= green_left() <= range_max_brown_left[1] and range_min_brown_left[2] <= blue_left() <= range_max_brown_left[2]

def is_brown_right():
    return range_min_brown_right[0] <= red_right() <= range_max_brown_right[0] and range_min_brown_right[1] <= green_right() <= range_max_brown_right[1] and range_min_brown_right[2] <= blue_right() <= range_max_brown_right[2]

def is_brown():
    return is_brown_left() and is_brown_right()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def is_wall():
    return (is_black_left() and is_yellow_right()) or (is_yellow_left() and is_black_right())
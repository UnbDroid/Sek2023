from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port

from modules.variables import *

color_sensor_floor_left = ColorSensor(Port.S1)
color_sensor_floor_right = ColorSensor(Port.S2)

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


#azul os dois Esquerda:  (13, 27, 99) Direita:  (16, 31, 100)
# VERMELHO OS DOIS : Esquerda:  (89, 19, 25) Direita:  (89, 19, 36)
# BRANCO OS DOIS : Esquerda:  (90, 92, 100) Direita:  (93, 96, 100)
# AMARELO : Esquerda:  (95, 84, 48) Direita:  (100, 96, 67)
# PRETO   : Esquerda:  (10, 12, 15) Direita:  (10, 10, 21)

# Atomação thamires.13 ------------------------------------------------------------------

range_max_black_left = get_range_colors([10, 12, 15], 'max')
range_min_black_left = get_range_colors([10, 12, 15], 'min')

range_max_black_right = get_range_colors([10, 10, 21], 'max')
range_min_black_right = get_range_colors([10, 10, 21], 'min')

# -----------------------------------------------

range_max_yellow_left = get_range_colors([95, 84, 48], 'max')
range_min_yellow_left = get_range_colors([95, 84, 48], 'min')

range_max_yellow_right = get_range_colors([100, 96, 67], 'max')
range_min_yellow_right = get_range_colors([100, 96, 67], 'min')

# -----------------------------------------------

range_max_blue_left = get_range_colors([13, 27, 99], 'max')
range_min_blue_left = get_range_colors([13, 27, 99], 'min')

range_max_blue_right = get_range_colors([16, 31, 100], 'max')
range_min_blue_right = get_range_colors([16, 31, 100], 'min')

# -----------------------------------------------

range_max_red_left = get_range_colors([85, 16, 21], 'max')
range_min_red_left = get_range_colors([85, 16, 21], 'min')

range_max_red_right = get_range_colors([91, 22, 36], 'max')
range_min_red_right = get_range_colors([91, 22, 36], 'min')

# Range das cores ------------------------------------------------------------------------
 
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



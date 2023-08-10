from pybricks.ev3devices import ColorSensor                                 
from pybricks.parameters import Port

color_sensor_floor_left = ColorSensor(Port.S1)
color_sensor_floor_right = ColorSensor(Port.S2)

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

# -------------------------------------------------------------

range_max_black_left = [26, 25, 20]
range_min_black_left = [0, 0, 0]

range_max_black_right = [27, 27, 32]
range_min_black_right = [0, 0, 2]

def is_black_left():
    return range_min_black_left[0] < red_left() < range_max_black_left[0] and range_min_black_left[1] < green_left() < range_max_black_left[1] and range_min_black_left[2] < blue_left() < range_max_black_left[2]

def is_black_right():
    return range_min_black_right[0] < red_right() < range_max_black_right[0] and range_min_black_right[1] < green_right() < range_max_black_right[1] and range_min_black_right[2] < blue_right() < range_max_black_right[2]

def is_black():
    return is_black_left() and is_black_right()

# -------------------------------------------------------------

range_max_yellow_left = [100, 97, 50]
range_min_yellow_left = [70, 67, 20]

range_max_yellow_right = [100, 100, 86]
range_min_yellow_right = [84, 81, 55]

def is_yellow_left():
    return range_min_yellow_left[0] < red_left() < range_max_yellow_left[0] and range_min_yellow_left[1] < green_left() < range_max_yellow_left[1] and range_min_yellow_left[2] < blue_left() < range_max_yellow_left[2]

def is_yellow_right():
    return range_min_yellow_right[0] < red_right() < range_max_yellow_right[0] and range_min_yellow_right[1] < green_right() < range_max_yellow_right[1] and range_min_yellow_right[2] < blue_right() < range_max_yellow_right[2]

def is_yellow():
    return is_yellow_left() and is_yellow_right()

# -------------------------------------------------------------

range_max_blue_left = [33, 45, 100]
range_min_blue_left = [2, 15, 85]

range_max_blue_right = [38, 51, 100]
range_min_blue_right = [8, 21, 85]

def is_blue_left():
    return range_min_blue_left[0] < red_left() < range_max_blue_left[0] and range_min_blue_left[1] < green_left() < range_max_blue_left[1] and range_min_blue_left[2] < blue_left() < range_max_blue_left[2]

def is_blue_right():
    return range_min_blue_right[0] < red_right() < range_max_blue_right[0] and range_min_blue_right[1] < green_right() < range_max_blue_right[1] and range_min_blue_right[2] < blue_right() < range_max_blue_right[2]

def is_blue():
    return is_blue_left() and is_blue_right()

# -------------------------------------------------------------

range_max_red_left = [85, 32, 20]
range_min_red_left = [55, 2, 0]

range_max_red_right = [95, 40, 35]
range_min_red_right = [65, 10, 5]

def is_red_left():
    return range_min_red_left[0] < red_left() < range_max_red_left[0] and range_min_red_left[1] < green_left() < range_max_red_left[1] and range_min_red_left[2] < blue_left() < range_max_red_left[2]

def is_red_right():
    return range_min_red_right[0] < red_right() < range_max_red_right[0] and range_min_red_right[1] < green_right() < range_max_red_right[1] and range_min_red_right[2] < blue_right() < range_max_red_right[2]

def is_red():
    return is_red_left() and is_red_right()
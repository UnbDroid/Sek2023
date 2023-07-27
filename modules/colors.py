
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

def is_black():
    return (red_left() < 18 and green_left() < 18 and blue_left() < 18) or (red_right() < 18 and green_right() < 18 and blue_right() < 18)

def is_yellow():
    return (red_left() > 70 and green_left() > 70 and blue_left() < 45) or (red_right() > 70 and green_right() > 70 and blue_right() < 45)

def is_blue():
    return (red_left() < 35 and green_left() < 35 and blue_left() > 75) or (red_right() < 35 and green_right() < 35 and blue_right() > 75)

def is_red():
    return (red_left() > 65 and green_left() < 25 and blue_left() < 25) or (red_right() > 65 and green_right() < 25 and blue_right() < 25)
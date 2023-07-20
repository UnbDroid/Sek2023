from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

color_sensor_floor = ColorSensor(Port.S1)

def red():
    return color_sensor_floor.rgb()[0]

def green():
    return color_sensor_floor.rgb()[1]

def blue():
    return color_sensor_floor.rgb()[2]

def is_black():
    return red() < 18 and green() < 18 and blue() < 18

def is_yellow():
    return red() > 18 and green() > 18 and blue() < 18

def is_blue():
    return red() < 18 and green() < 18 and blue() > 18

def is_red():
    return red() > 18 and green() < 18 and blue() < 18
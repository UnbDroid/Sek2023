from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

color_sensor_right_lower = ColorSensor(Port.S2)
color_sensor_right_upper = ColorSensor(Port.S3)

def is_tube_of_15():
    return color_sensor_right_lower.reflection() > 1 and color_sensor_right_upper.reflection() > 1

def is_tube_of_10():
    return color_sensor_right_lower.reflection() > 1 and color_sensor_right_upper.reflection() < 1

def is_red_tube():
    return color_sensor_right_lower.rgb()[0] > 10 and color_sensor_right_lower.rgb()[1] < 10 and color_sensor_right_lower.rgb()[2] < 10

def is_green_tube():
    return color_sensor_right_lower.rgb()[0] < 10 and color_sensor_right_lower.rgb()[1] > 10 and color_sensor_right_lower.rgb()[2] < 10

def is_blue_tube():
    return color_sensor_right_lower.rgb()[0] < 10 and color_sensor_right_lower.rgb()[1] < 10 and color_sensor_right_lower.rgb()[2] > 10

def is_brown_tube():
    return color_sensor_right_lower.rgb()[0] > 10 and color_sensor_right_lower.rgb()[1] > 10 and color_sensor_right_lower.rgb()[2] < 10
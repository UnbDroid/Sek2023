from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from modules.colors import *
from modules.delivery import *
from modules.detect import *
from modules.path import *
from modules.tube import *

motor_left = Motor(Port.A) 
motor_right = Motor(Port.B)

motors = DriveBase(motor_left, motor_right, wheel_diameter = 42.1, axle_track = 115.3)

def move_forward(n):
    motors.straight(15*n)
    
def move_backward(n):
    motors.straight(-15*n)
    
def turn_left():
    motors.turn(-90)
    if pointed_to == 0:
        pointed_to = 3
    else:
        pointed_to -= 1

def turn_right():
    motors.turn(90)
    if pointed_to == 3:
        pointed_to = 0
    else:
        pointed_to += 1
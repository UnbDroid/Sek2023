from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

motors = DriveBase(left_motor, right_motor, wheel_diameter=42.1, axle_track=115.3)

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
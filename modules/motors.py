from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase


from pybricks.robotics import DriveBase


from modules.colors import *
from modules.delivery import *
from modules.detect import *
from modules.path import *

left_motor = Motor(Port.A) 
right_motor = Motor(Port.B)

motors = DriveBase(left_motor, right_motor, 42.1, 1)

def move_forward(n):
    motors.straight(150*n)
    
def move_backward(n):
    motors.straight(-150*n)
    
def turn_left():
    motors.turn(-90)

def turn_right():
    motors.turn(90)
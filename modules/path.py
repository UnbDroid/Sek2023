from modules.motors import *
from modules.colors import *
from modules.detect import *
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

pointed_to = 1
cardinal_points = ["N", "E", "S", "W"]
cronometer = StopWatch()
size_of_tube = 0
color_of_tube = ""
initial_path = [0, 0, 0, 0]
current_path = [0, 0, 0, 0]

def find_blue_line():
    cronometer.reset()
    while not is_blue() and not is_black() and not is_yellow() and not is_red():
        motors.drive(100, 0)
    if is_red():
        move_backward(2)
        turn_left()
        while not is_blue() and not is_black() and not is_yellow() and not is_red():
            motors.drive(100, 0)
        if is_black() or is_yellow():
            turn_right()
            turn_right()
            while not is_blue() and not is_black() and not is_yellow() and not is_red():
                motors.drive(100, 0)
    if is_black() or is_yellow():
        time_forward = cronometer.time()
        cronometer.reset()
        while cronometer.time() < time_forward:
            motors.drive(-100, 0)
        turn_right()
        find_blue_line()
        
def align_to_begin_scan():
    turn_right()
    while not is_red():
        motors.drive(100, 0)
    turn_left()
    turn_left()

def scan():
    pointed_to = 0
    while not is_tube_of_15() and not is_tube_of_10():
        motors.drive(100, 0)
        
    if is_tube_of_15():
        size_of_tube = 15
    if is_tube_of_10():
        size_of_tube = 10
        
    if is_red_tube():
        color_of_tube = "RED"
    if is_green_tube():
        color_of_tube = "GREEN"
    if is_blue_tube():
        color_of_tube = "BLUE"
    if is_brown_tube():
        color_of_tube = "BROWN"
        
def align_to_begin_deliver():
    pointed_to = 0
    while not is_red():
        motors.drive(100, 0)
    move_backward(4)

def set_path():
    if size_of_tube == 15:
        if color_of_tube == "RED": #Farmacia
            initial_path = [0, 0, 0, 0]
        if color_of_tube == "GREEN": #Prefeitura
            
        if color_of_tube == "BLUE": #Museu
            
        if color_of_tube == "BROWN": #Padaria
            
    else:
        if color_of_tube == "GREEN": #Parque
            
        if color_of_tube == "BLUE": #Escola
            
        if color_of_tube == "BROWN": #Biblioteca
            
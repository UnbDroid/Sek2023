#!/usr/bin/env pybricks-micropython
from modules.colors import *
from modules.path import *
from modules.motors import *

from pybricks.hubs import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()

find_blue_line()
align_to_begin_scan()

# while True:
#     motors.turn(360)
#     motors.stop()
#     wait(1000)

# while True:
#     print("Esquerda: ", color_sensor_floor_left.rgb() , "Direita: ", color_sensor_floor_right.rgb())
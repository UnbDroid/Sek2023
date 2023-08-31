#!/usr/bin/env pybricks-micropython
from modules.colors import *
from modules.path import *
from modules.motors import *
from modules.detect import *
from modules.delivery import *
from modules.claw import *

from pybricks.hubs import EV3Brick


ev3 = EV3Brick()



# Codigo ---------------------------------------------------------------------------------------

find_blue_line()
# print("RGB Esquerdo: ", red_left(), green_left(), blue_left(), "RGB Direito: ", red_right(), green_right(), blue_right())
ev3.speaker.beep(444, 1000)
while True:
    align_to_begin_scan()
    ev3.speaker.beep(444, 1000)
    scan()
    ev3.speaker.beep(444, 1000)
    go_to_check_point()
    ev3.speaker.beep(444, 1000)
    set_path()
    ev3.speaker.beep(444, 1000)


#-----------------------------------------------------------------------------------------------



# Ajustar curva de 90 graus --------------------------------------------------------------------

# motors.turn(180)
# print(left_motor.angle(), right_motor.angle())
# brake_motors()

# Ajustar axle_track ---------------------------------------------------------------------------

# while True:
#     turn_left(360)
#     brake_motors()
#     wait(1000)

#-----------------------------------------------------------------------------------------------



# Abrir ou fechar a garra ----------------------------------------------------------------------

# Open()
# Close()

#-----------------------------------------------------------------------------------------------



# Ajustar ranges das cores ---------------------------------------------------------------------

# while True:
#     print("Esquerda: ", color_sensor_floor_left.rgb() , "Direita: ", color_sensor_floor_right.rgb())

#-----------------------------------------------------------------------------------------------



# Ajustar ranges dos tubos ---------------------------------------------------------------------

# while True:
#     print(tube_verificator.rgb())

#-----------------------------------------------------------------------------------------------



# Ajustar andar reto ---------------------------------------------------------------------------

# while True:
#     andar_reto(360)

#-----------------------------------------------------------------------------------------------
#!/usr/bin/env pybricks-micropython
from modules.colors import *
from modules.path import *
from modules.motors import *
from modules.detect import *
from modules.delivery import *
from modules.claw import *

from pybricks.hubs import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()

# Codigo ---------------------------------------------------------------------------------------

find_blue_line()
print("RGB Esquerdo: ", red_left(), green_left(), blue_left(), "RGB Direito: ", red_right(), green_right(), blue_right())
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



# Andar reto -----------------------------------------------------------------------------------

# cronometer.reset()
# while cronometer.time() < 10000:
#     andar_reto(50)

#-----------------------------------------------------------------------------------------------
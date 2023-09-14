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

# find_blue_line(0)
# # print("RGB Esquerdo: ", red_left(), green_left(), blue_left(), "RGB Direito: ", red_right(), green_right(), blue_right())
# ev3.speaker.beep(444, 1000)
# while True:
#     align_to_begin_scan()
#     ev3.speaker.beep(444, 1000)
#     scan()
#     ev3.speaker.beep(444, 1000)
#     go_to_check_point()
#     ev3.speaker.beep(444, 1000)
#     set_path()
#     ev3.speaker.beep(444, 1000)

# -----------------------------------------------------------------------------------------------



# Ajustar curva de 90 graus --------------------------------------------------------------------

# motors.turn(180)
# print(left_motor.angle(), right_motor.angle())
# brake_motors()

#-----------------------------------------------------------------------------------------------



# Ajustar axle_track ---------------------------------------------------------------------------

# for i in range(3):                                       # 1212
#     motors.turn(330)                                     # 1212
#     while not is_black():                                # 1216
#         motors.turn(1)
#     motors.stop()
#     print(left_motor.angle(), right_motor.angle())
#     brake_motors()

#-----------------------------------------------------------------------------------------------



# Testar curvas PID ----------------------------------------------------------------------------
# i = 0
# while i < 6:
#     turn_right_pid(90)
#     wait(500)
#     i+=1

#-----------------------------------------------------------------------------------------------



# Abrir ou fechar a garra ----------------------------------------------------------------------

# Open()
# Close()

#-----------------------------------------------------------------------------------------------



# Ajustar ranges das cores ---------------------------------------------------------------------

# while True:
#     wait(500)
#     print("Esquerda: ", color_sensor_floor_left.rgb() , "Direita: ", color_sensor_floor_right.rgb())

#-----------------------------------------------------------------------------------------------



# Ajustar ranges dos tubos ---------------------------------------------------------------------

# while True:
#     print(ultrasound_sensor.distance())

#-----------------------------------------------------------------------------------------------



# Ajustar andar reto ---------------------------------------------------------------------------

# while True:
#     andar_reto(360)

# move_forward(100)

#-----------------------------------------------------------------------------------------------

# Ajustar o ajust color ------------------------------------------------------------------------

# while not is_yellow_left() and not is_yellow_right():
#     andar_reto(360)
    
# cor_vista = "AMARELO"
# brake_motors()
# ajust_color(cor_vista)
# found_door()
# move_backward(1000)

#-----------------------------------------------------------------------------------------------

# Ajustar a distância --------------------------------------------------------------------------

distance = []

for i in range(5):
    while ultrasound_sensor.distance() < 250:
        andar_reto(-360)
    brake_motors()
    while ultrasound_sensor.distance() > 200:
        andar_reto(360)
    brake_motors()
    while ultrasound_sensor.distance() < 200:
        andar_reto(-100)
    brake_motors()
    cronometer.reset()
    while cronometer.time() < 1000:
        andar_reto(360)
    brake_motors()
    distance.append(200 - ultrasound_sensor.distance())
    print("Distância por segundo: ", (200 - ultrasound_sensor.distance()))

print("Distância média por segundo: ", sum(distance)/len(distance))
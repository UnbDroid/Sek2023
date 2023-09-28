#!/usr/bin/env pybricks-micropython
from modules.colors import *
from modules.path import *
from modules.motors import *
from modules.detect import *
from modules.delivery import *
from modules.claw import *

from pybricks.hubs import EV3Brick

# has_object_in = []
# # Codigo ---------------------------------------------------------------------------------------

# find_blue_line(0)
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
   


# ---------------------------------------------------------

branco = range_white_right()[0] 
azul = range_blue_right()[0] 
threshold = (branco + azul) / 2  
vel = 100

scan_tube = 'Sem tubo'

while scan_tube == 'Sem tubo':
    delta = red_right() - threshold
    kp = 0.5
    erro = delta * kp
    motors.drive(vel, erro)   
     
    mbox.send('de_ladinho')
    mbox.wait()
    scan_tube = mbox.read()

    
brake_motors_para_drive_base()
brake_motors()

deu_bom_familia()


# manobras --- 

move_forward(5)
turn_right_pid(90)
Close(False)
while True:
    print("Entrei")
    mbox.send('tem tubo?')
    mbox.wait()
    tem_tubo = mbox.read()
    print("li")
    if tem_tubo == "tem tubo":
        print("sai")
        break
    andar_reto(80)
    
andou_frente = [left_motor.angle(), right_motor.angle()]
brake_motors()
while left_motor.angle() < andou_frente[0] or right_motor.angle() < andou_frente[1]:
    andar_reto(-80)


# Editando o Range------------------------------------------------------------------------------

# while True:
#     print("Vejo?", tube_is_detected(), "Cor",is_brown_tube() )
    # print("oi novinha", tube_verificator.rgb())
    # Cor (4, 2, 0)
    # Vejo? True Cor (38, 4, 1)

# Teste range sensor auxiliar ------------------------------------------------------------------

# while True:
#     print(red_aux(), green_aux(), blue_aux())
#     wait(500)

# Ajustar curva de 90 graus --------------------------------------------------------------------

# count = 0
# while count < 4:
#     count+=1
#     turn_right_pid(180)
#     print(left_motor.angle(), right_motor.angle())
#     brake_motors()

#-----------------------------------------------------------------------------------------------

# Ajustar axle_track ---------------------------------------------------------------------------

# for i in range(5):                                       # 1212
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
#     turn_left_pid(90)
#     wait(500)
#     i+=1

#-----------------------------------------------------------------------------------------------



# Abrir ou fechar a garra ----------------------------------------------------------------------

# Open()
# wait(2000)
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
#     andar_reto(500)

# move_forward(100)

#-----------------------------------------------------------------------------------------------

# Ajustar o ajust color ------------------------------------------------------------------------

# while not is_red_left() and not is_red_right():
#     andar_reto(500)
    
# cor_vista = "RED"
# brake_motors()
# ajust_color(cor_vista)
# move_backward(10)

#-----------------------------------------------------------------------------------------------

# Ajustar a distância --------------------------------------------------------------------------

# move_backward(43)

#-----------------------------------------------------------------------------------------------

# Teste de girar o motor -----------------------------------------------------------------------

# while True:
#     left_motor.run(40)
#     right_motor.run(-30)
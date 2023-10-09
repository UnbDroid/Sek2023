#!/usr/bin/env pybricks-micropython
from modules.colors import *
from modules.path import *
from modules.motors import *
from modules.detect import *
from modules.delivery import *
from modules.claw import *

from pybricks.hubs import EV3Brick

'''
! Range do azul no brick aux 
! Range do ultrassom no aux
! Ida pra bakery - Teoricamente feito!
! Ida pro park - Teoricamente feito!
! Alinhar com azul (deixar mais no azul)
! Regular a entrada no azul
'''
    

#* Codigo para pegar por dentro da área de coleta 😶‍🌫️👀🔑 ---------------------------------------------------------------------------------------

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
   

#* Codigo para pegar de ladinho The Ladinho 😎🫡🤠 -------------------------------------------------------------------------------------

find_blue_line(0)
ev3.speaker.beep(444, 1000)
while True:
    
    align_to_be_ladinho()
    
    ev3.speaker.beep(444, 1000)
    scan_de_ladinho_papai()
    ev3.speaker.beep(444, 1000)
    

    set_path()
    ev3.speaker.beep(444, 1000)
    
# ---------------------------------------------------------

# Teste <3

# while not is_yellow() or not is_black_left() or not is_black_right():
#     andar_reto(100)
    
#     if is_yellow():
        
#         ajust_color("YELLOW")
#         break
#     elif is_black_left():
        
#         brake_motors()
#         move_backward(6)
#         print("vou virar")
#         turn_left_pid(70) #! Ajustar o valor
#         print("Virei")
#         move_backward(5)
#         turn_right_pid(70)
        
#     elif is_black_right():
        
#         brake_motors()
#         move_backward(5)
#         turn_right_pid(70)
#         move_backward(5)
#         turn_left_pid(70)
    
    # elif color_sensor_floor_left.rgb():
    







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
#         motors.drive(0,5)
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
#     print("Esquerda: ",color_sensor_floor_left.rgb() , "Direita: ", color_sensor_floor_right.rgb())
    

#-----------------------------------------------------------------------------------------------



# Ajustar ranges dos tubos ---------------------------------------------------------------------

# while True:
#     print(ultrasound_sensor.distance())

#-----------------------------------------------------------------------------------------------



# Ajustar andar reto ---------------------------------------------------------------------------

# while not is_red_left() and not is_red_right():
#     andar_reto(500)
# wait(3000)
# move_backward(100)
# move_forward(100)

#-----------------------------------------------------------------------------------------------

# Ajustar o ajust color ------------------------------------------------------------------------

# while not is_black_left() and not is_black_right():
#     andar_reto(500)
    
# cor_vista = "BLACK"
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
#!/usr/bin/env pybricks-micropython
from modules.colors import *
from modules.path import *
from modules.motors import *

from pybricks.hubs import EV3Brick
from pybricks.tools import wait

# server 
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# # The server must be started before the client!
# print('waiting for connection...')
# server.wait_for_connection()
# print('connected!')

# # In this program, the server waits for the client to send the first message
# # and then sends a reply.
# mbox.wait()
# print(mbox.read())
# mbox.send('hello to you!')

# ev3 = EV3Brick()



# Mudar quando ele está no C olhando para o amarelo, e pensar de um jeito de deixar mais simples quando encontra o vermelho direto. Ele fica em um loop infinito virando 180° 
# Mudar a condicional de vermelho






# print(motors.heading_control.pid())
# print(motors.distance_control.pid())

# while True:
#     find_blue_line()
#     align_to_begin_scan()


while True:
    andar_reto(50)


# while True:
#     left_motor.run(50)
#     print(left_motor.speed())

# while True:
#     motors.turn(360)
#     motors.stop()
#     wait(1000)

# while True:
#     print("Esquerda: ", color_sensor_floor_left.rgb() , "Direita: ", color_sensor_floor_right.rgb())


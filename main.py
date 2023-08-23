#!/usr/bin/env pybricks-micropython
from modules.colors import *
from modules.path import *
from modules.motors import *
from modules.detect import *
from modules.delivery import *
from modules.claw import *

from pybricks.hubs import EV3Brick
from pybricks.tools import wait

# # In this program, the server waits for the client to send the first message
# # and then sends a reply.
# mbox.wait()
# print(mbox.read())
# mbox.send('hello to you!')

ev3 = EV3Brick()
# Open()
# Close()

#teste
# cronometer.reset()
# while cronometer.time() < 10000:
#     andar_reto(50)



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



# while True:
#     print(tube_verificator.rgb())
#     andar_reto(50)
# print("Achou vermelho", cronometer.time())


# while True:
#     left_motor.run(50)
#     print(left_motor.speed())

# while True:
#     motors.turn(360)
#     motors.stop()
#     wait(1000)

# cout=0
# while cronometer.time() < 5000:
#     andar_reto(40)
#     print("Esquerda: ", color_sensor_floor_left.rgb() , "Direita: ", color_sensor_floor_right.rgb())
#     cout+=1
    
# print(cout)

# while True:
#     print("Esquerda: ", color_sensor_floor_left.rgb() , "Direita: ", color_sensor_floor_right.rgb())

# tube_presence = tube_verificator.reflection()
# while tube_presence == 0: 
#     tube_presence = tube_verificator.reflection()
#     scan()

# turn_right(90)
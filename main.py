#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.nxtdevices import ColorSensor



# Defininindo as portas
ev3 = EV3Brick()
color_upper = ColorSensor(Port.S4)
color_lower = ColorSensor(Port.S3)

# Programando
while True:
    if color_lower.reflection() > 10 and color_upper.reflection() > 7:
        print("Tubo de 15 :) ")
        
    if  color_lower.reflection() > 10 and color_upper.reflection () < 7:
        print("Tubo de 10 :) ") 
        
        
from pybricks.ev3devices import UltrasonicSensor
from modules.colors import *

tube_verificator = ColorSensor(Port.S4)

def tube_is_detected():
    if tube_verificator.reflection() > 3:
        return True
    else:
        return False

ultrasound_sensor = UltrasonicSensor(Port.S3)

def has_obstacle():
    if ultrasound_sensor.distance() <= 110:
        print("Obstáculo detectado")
        return True
    else:
        print("Obstáculo não detectado")
        return False

# def is_tube_of_15():
#     return tube_verificator.reflection() > 1 and color_sensor_right_upper.reflection() > 1

# def is_tube_of_10():
#     return tube_verificator.reflection() > 1 and color_sensor_right_upper.reflection() < 1

def is_red_tube():
    return tube_verificator.rgb()[0] > (tube_verificator.rgb()[1] + tube_verificator.rgb()[2])

def is_green_tube():
    return (tube_verificator.rgb()[0] + tube_verificator.rgb()[2]) < tube_verificator.rgb()[1]

def is_blue_tube():
    return (tube_verificator.rgb()[0] + tube_verificator.rgb()[1]) < tube_verificator.rgb()[2] > 10
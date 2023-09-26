from pybricks.ev3devices import UltrasonicSensor
from modules.colors import *
from modules.beeps import *

tube_verificator = ColorSensor(Port.S4)

def tube_is_detected():
    # print("reflexion papai ",tube_verificator.reflection())
    print("cor tube ",tube_verificator.rgb())
    if tube_verificator.reflection() >= 8 or (tube_verificator.rgb()[0] >= 2 and tube_verificator.rgb()[1] >=3):
        return True
    else:
        return False

ultrasound_sensor = UltrasonicSensor(Port.S3)

def has_obstacle():
    valores_lidos = []
    if len(valores_lidos) < 5:
        valores_lidos.append(ultrasound_sensor.distance())
    else:
        valores_lidos.pop(0)
        valores_lidos.append(ultrasound_sensor.distance())
    if sum(valores_lidos) / len(valores_lidos) <= 100:
        print("Obstáculo detectado")
        found_wall()
        return True
    else:
        return False


def is_red_tube():
    return tube_verificator.rgb()[0] >= (tube_verificator.rgb()[1] + tube_verificator.rgb()[2]) and tube_verificator.rgb()[0] > 20

def is_green_tube():
    return (tube_verificator.rgb()[0] + tube_verificator.rgb()[2]) <= tube_verificator.rgb()[1]

def is_blue_tube():
    return (tube_verificator.rgb()[0] + tube_verificator.rgb()[1]) <= tube_verificator.rgb()[2]

def is_brown_tube():
    return tube_verificator.rgb()[0] >= (tube_verificator.rgb()[1] + tube_verificator.rgb()[2]) and tube_verificator.rgb()[0] < 10 and tube_verificator.rgb()[0] > 2

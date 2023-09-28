from pybricks.ev3devices import UltrasonicSensor
from pybricks.nxtdevices import ColorSensor as CSNXT
from modules.colors import *
from modules.beeps import *

<<<<<<< HEAD
=======
tube_verificator = CSNXT(Port.S4)

def tube_is_detected():
    # print("reflexion papai ",tube_verificator.reflection())
    #print("cor tube ",tube_verificator.rgb())
    if tube_verificator.reflection() >= 8 or (tube_verificator.rgb()[0] >= 2 and tube_verificator.rgb()[1] >=3):
        return True
    else:
        return False

>>>>>>> 0f7e5fbc34b469d8064b60a1609a792ea30e0336
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
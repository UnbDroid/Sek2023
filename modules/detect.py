from pybricks.ev3devices import UltrasonicSensor, InfraredSensor
from modules.colors import *
from modules.beeps import *
from modules.motors import *

ultrasound_sensor = UltrasonicSensor(Port.S3)
tube_sensor = InfraredSensor(Port.S4)  #InfraredSensor

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
    
def tube_is_detected():
    if tube_sensor.distance() <= 12: 
        return True
    else:
        return False
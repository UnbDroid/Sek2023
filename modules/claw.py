from modules.path import *

claw_motor = Motor(Port.A)

def Open(quantidade = 1100,time = 1100):
    print("Abrindooo")
    claw_motor.run_angle(time, quantidade, wait=True)

def Close(quantidade = -1100, esperar=True,time = 1100):
    print("Fechandooo")
    claw_motor.run_angle(time, quantidade, wait=esperar)
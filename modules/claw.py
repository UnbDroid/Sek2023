from modules.path import *

claw_motor = Motor(Port.A)

def Open(quantidade = 1100,time = 1500,esperar = True):
    print("Abrindooo")
    claw_motor.run_angle(time, quantidade, wait=esperar )

def Close(quantidade = -1100, esperar=True,time = 1500): #1100
    print("Fechandooo")
    claw_motor.run_angle(time, quantidade, wait=esperar)
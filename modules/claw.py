from modules.path import *

claw_motor = Motor(Port.C)

def Open(quantidade=800,time = 800):
    print("Abrindooo")
    claw_motor.run_angle(time, quantidade, wait=True)

def Close(quantidade=-800, esperar=True,time = 800):
    print("Fechandooo")
    claw_motor.run_angle(time, quantidade, wait=esperar)
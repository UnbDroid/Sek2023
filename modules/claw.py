from modules.path import *

claw_motor = Motor(Port.C)

def Open(quantidade=800):
    # claw_motor.run_time(250,3200,Stop.HOLD,True)
    claw_motor.run_angle(250, quantidade, wait=True)

def Close(quantidade=-800, esperar=True):
    # claw_motor.run_time(-250,3200,Stop.HOLD,wait=fechar)
    claw_motor.run_angle(250, quantidade, wait=esperar)
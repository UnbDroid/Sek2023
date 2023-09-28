from modules.path import *

claw_motor = Motor(Port.C)

def Open():
    claw_motor.run_time(250,3200,Stop.HOLD,True)

def Close(fechar=True):
    claw_motor.run_time(-250,3200,Stop.HOLD,wait=fechar)


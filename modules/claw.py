from modules.path import *

claw_motor = Motor(Port.C)

def Open():
    # claw_motor.run_time(250,3200,Stop.HOLD,True)
    claw_motor.run_time(250,1200,Stop.HOLD,True)

def Close(fechar=True):
    # claw_motor.run_time(-250,3200,Stop.HOLD,wait=fechar)
    claw_motor.run_time(-250,1200,Stop.HOLD,wait=fechar)

def New_Open(quantidade = 800):
    claw_motor.run_angle(250, quantidade, wait=True)
    
def New_Close(quantidade = -800):
    claw_motor.run_angle(250, quantidade, wait=True)

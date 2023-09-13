from modules.path import *

claw_motor = Motor(Port.C)

def Open():
    claw_motor.run_time(600,2600,Stop.HOLD,True)

def Close():
    claw_motor.run_time(-600,2600,Stop.HOLD,True)


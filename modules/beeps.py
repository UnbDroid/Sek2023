from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
left_motor = Motor(Port.A) 
right_motor = Motor(Port.B)
motors = DriveBase(left_motor, right_motor, 42.1, 150) # 140.88

def found_door():
    motors.stop()
    ev3.speaker.beep(100, 1000)
    
def found_wall():
    motors.stop()
    ev3.speaker.beep(1000, 500)
    wait(250)
    ev3.speaker.beep(1000, 500)
    # Teste
    
def not_found_wall():
    motors.stop()
    ev3.speaker.beep(100, 1000)
    
def alined_to_wall():
    motors.stop()
    ev3.speaker.beep(100, 1000)
    
def deu_bom_familia():
    ev3.speaker.beep(1000, 500)
    wait(250)
    ev3.speaker.beep(1000, 500)

    
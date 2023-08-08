from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase


from pybricks.robotics import DriveBase


from modules.colors import *
from modules.delivery import *
from modules.detect import *
from modules.path import *

left_motor = Motor(Port.A) 
right_motor = Motor(Port.B)

motors = DriveBase(left_motor, right_motor, 42.1, 141.0) # 140.88

def andar_reto(velo):
    kp = 0.010 #0.001
    delta = (left_motor.angle() - right_motor.angle())/360
    erro = delta * kp
    
    # right_motor.dc(velo - erro)
    
    right_motor.dc(velo + erro) #dc
    left_motor.dc(velo - erro) #dc

def go_forward(x):
    left_motor.run(x)
    right_motor.run(x)
    pass
    
def go_backward(x):
    left_motor.run(-x)
    right_motor.run(-x)
    pass
    
def break_motors():
    left_motor.brake()
    right_motor.brake()

def move_forward(n):
    motors.straight(150*n)
    
def move_backward(n):
    motors.straight(-150*n)
    
def turn_left():
    motors.turn(-90)

def turn_right():
    motors.turn(90)
    
def ajust_color():
    print("Ajustando cor...")
    
    if is_black_left() and not is_black_right():
        while not is_black_right():
            right_motor.dc(20)
        break_motors()
        motors.turn(-5)
    elif not is_black_left() and is_black_right():
        while not is_black_left():
            left_motor.dc(20)
        break_motors()
        motors.turn(5)
        
        
# --------------------------------- 
        
    elif is_red_left() and not is_red_right():
        while not is_red_right():
            right_motor.dc(20)
        break_motors()
        motors.turn(-5)
    elif not is_red_left() and is_red_right():
        while not is_red_left():
            left_motor.dc(20)
        break_motors()
        motors.turn(5)
    
# ---------------------------------
    
    elif is_blue_left() and not is_blue_right():
        while not is_blue_right():
            right_motor.dc(20)
        break_motors()
        motors.turn(-5)
    elif not is_blue_left() and is_blue_right():
        while not is_blue_left():
            left_motor.dc(20)
        break_motors()
        motors.turn(5)

# ---------------------------------

    elif is_yellow_left() and not is_yellow_right():
        while not is_yellow_right() and not is_black_right():
            right_motor.dc(20)
        motors.turn(-5)
    elif not is_yellow_left() and not is_black_left():
        while not is_yellow_left():
            left_motor.dc(10)
        motors.turn(5)
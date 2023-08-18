from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch
from pybricks.robotics import DriveBase


from modules.colors import *
from modules.detect import *
from modules.path import *

left_motor = Motor(Port.A) 
right_motor = Motor(Port.B)

cronometer = StopWatch()

motors = DriveBase(left_motor, right_motor, 42.1, 141.0) # 140.88

integral = 0
prev_delta = 0

def andar_reto(velo):
    #print("Angulo Esquerda: ", left_motor.angle(), "- Angulo Direita: ", right_motor.angle(), "- Diferença: ", left_motor.angle() - right_motor.angle())
    global integral
    global prev_delta
    kp = 110
    ki = 1.002
    kd = 0.9955
    
    delta = (left_motor.angle() - right_motor.angle()) / 360
    erro = delta * kp
    
    integral += delta
    integral *= ki
    
    derivative = delta - prev_delta
    derivative *= kd
    
    control_output = erro + integral + derivative
    
    prev_delta = delta
    
    right_motor.dc(velo + control_output)
    left_motor.dc(velo - control_output)    
    

def break_motors():
    left_motor.brake()
    right_motor.brake()

def move_forward(n):
    cronometer.reset()
    while cronometer.time() < n:
        andar_reto(50)
    break_motors()
    
def move_backward(n):
    cronometer.reset()
    while cronometer.time() < n:
        andar_reto(-50)
    break_motors()
    
def turn_left(x):
    motors.turn(-x)
    motors.stop()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

def turn_right(x):
    motors.turn(x)
    motors.stop()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
def ajust_color():
    print("Ajustando cor...")
    
    if cor_vista == "PRETO":
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
        
    if cor_vista == "VERMELHO":
        if is_red_left() and not is_red_right():
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
    
    if cor_vista == "AZUL":
        if is_blue_left() and not is_blue_right():
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

    if cor_vista == "AMARELO":
        if is_yellow_left() and not is_yellow_right():
            while not is_yellow_right() and not is_black_right():
                right_motor.dc(20)
            motors.turn(-5)
        elif not is_yellow_left() and not is_black_left():
            while not is_yellow_left():
                left_motor.dc(10)
            motors.turn(5)
            
# ---------------------------------

    if cor_vista == "PAREDE":
        if (is_black_left() or is_yellow_left()) and not (is_black_right() or is_yellow_right()):
            while not (is_black_right() or is_yellow_right()):
                right_motor.dc(20)
            break_motors()
            motors.turn(-5)
        elif not (is_black_left() or is_yellow_left()) and (is_black_right() or is_yellow_right()):
            while not (is_black_left() or is_yellow_left()):
                left_motor.dc(20)
            break_motors()
            motors.turn(5)
            
# ---------------------------------

    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
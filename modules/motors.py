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

motors = DriveBase(left_motor, right_motor, 42.1, 142.3) # 140.88

integral = 0
prev_delta = 0

def andar_reto(velo):
    # global integral
    # global prev_delta
    # kp = 110
    # ki = 1.002
    # kd = 0.9955
    
    # delta = (left_motor.angle() - right_motor.angle()) / 360
    # erro = delta * kp
    
    # integral += delta
    # integral *= ki
    
    # derivative = delta - prev_delta
    # derivative *= kd
    
    # control_output = erro + integral + derivative
    
    # prev_delta = delta
    
    # right_motor.dc(velo + control_output)
    # left_motor.dc(velo - control_output)    
    
    
    # TESTE -------------------------
    
    global integral
    global prev_delta
    kp = 110
    ki = 1.002
    kd = 0.9955
    
    angulo_esquerda = left_motor.angle()
    angulo_direita = right_motor.angle()
    
    delta = (angulo_esquerda - angulo_direita) / 360
    erro = delta * kp
    
    integral += delta
    integral *= ki
    
    derivative = delta - prev_delta
    derivative *= kd
    
    control_output = erro + integral + derivative
    
    prev_delta = delta
    
    # Ajustar os motores com base no controle calculado
    right_motor.run_angle(velo + control_output, 360, wait = False)
    left_motor.run_angle(velo - control_output, 360, wait = False)
    

def brake_motors():
    motors.stop()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

def move_forward(tempo, vel=360):
    cronometer.reset()
    while cronometer.time() < tempo:
        andar_reto(vel)
    brake_motors()
    
def move_backward(tempo, vel=360):
    cronometer.reset()
    while cronometer.time() < tempo:
        andar_reto(-vel)
    brake_motors()
    
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
    
def ajust_color(cor_vista):
    print("Ajustando cor...")
    
    if cor_vista == "PRETO":
        if is_black_left() and not is_black_right():
            while not is_black_right():
                right_motor.run_angle(20, 360)
            brake_motors()
            motors.turn(-5)
        elif not is_black_left() and is_black_right():
            while not is_black_left():
                left_motor.run_angle(20, 360)
            brake_motors()
            motors.turn(5)
        
        
# --------------------------------- 
        
    if cor_vista == "VERMELHO":
        if is_red_left() and not is_red_right():
            while not is_red_right():
                right_motor.run_angle(20, 360)
            brake_motors()
            motors.turn(-5)
        elif not is_red_left() and is_red_right():
            while not is_red_left():
                left_motor.run_angle(20, 360)
            brake_motors()
            motors.turn(5)
    
# ---------------------------------
    
    if cor_vista == "AZUL":
        if is_blue_left() and not is_blue_right():
            while not is_blue_right():
                right_motor.run_angle(20, 360)
            brake_motors()
            motors.turn(-5)
        elif not is_blue_left() and is_blue_right():
            while not is_blue_left():
                left_motor.run_angle(20, 360)
            brake_motors()
            motors.turn(5)

# ---------------------------------

    if cor_vista == "AMARELO":
        if is_yellow_left() and not is_yellow_right():
            while not is_yellow_right() and not is_black_right():
                right_motor.run_angle(20, 360)
            motors.turn(-5)
        elif not is_yellow_left() and not is_black_left():
            while not is_yellow_left():
                left_motor.dc(10)
            motors.turn(5)
            
# ---------------------------------

    if cor_vista == "PAREDE":
        if (is_black_left() or is_yellow_left()) and not (is_black_right() or is_yellow_right()):
            while not (is_black_right() or is_yellow_right()):
                right_motor.run_angle(20, 360)
            brake_motors()
            motors.turn(-5)
        elif not (is_black_left() or is_yellow_left()) and (is_black_right() or is_yellow_right()):
            while not (is_black_left() or is_yellow_left()):
                left_motor.run_angle(20, 360)
            brake_motors()
            motors.turn(5)
            
# ---------------------------------

    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
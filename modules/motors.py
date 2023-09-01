from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch
from pybricks.robotics import DriveBase

from pybricks.tools import wait
from modules.colors import *
from modules.detect import *
from modules.path import *

left_motor = Motor(Port.A) 
right_motor = Motor(Port.B)

cronometer = StopWatch()

motors = DriveBase(left_motor, right_motor, 42.1, 150) # 140.88

integral = 0
prev_delta = 0


def andar_reto(velo):
    
    global integral
    global prev_delta
    kp = 4.89 #5.05
    ki = 1.0
    
    #kd = 0.9955
    
    angulo_esquerda = left_motor.angle()
    angulo_direita = right_motor.angle()
    
    delta = (angulo_esquerda - angulo_direita) / 360
    erro = delta * kp
    
    integral += delta
    integral *= ki
    
    derivative = delta - prev_delta
    #derivative *= kd
    
    control_output = erro + integral + derivative
    
    prev_delta = delta
    
    print("Diferença:", delta)
    
    # Ajustar os motores com base no controle calculado
    right_motor.run_angle((velo + control_output), 360, wait = False)
    left_motor.run_angle((velo - control_output), 360, wait = False)

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
    wait(200)
    brake_motors()
    valor_a_girar = 1226 * (x / 360)
    left_motor.run_angle(200, -valor_a_girar, wait = False)
    right_motor.run_angle(200, valor_a_girar, wait = True)
    left_motor.hold()
    right_motor.hold()
    wait(200)
    if left_motor.angle() != -valor_a_girar:
        left_motor.run_angle(5, (-valor_a_girar - left_motor.angle()), wait = False)
    if right_motor.angle() != valor_a_girar:
        right_motor.run_angle(5, (valor_a_girar - right_motor.angle()), wait = True)
    print(left_motor.angle(), right_motor.angle())
    brake_motors()
    wait(200)
    
    # motors.stop()
    # left_motor.reset_angle(0)
    # right_motor.reset_angle(0)
    # while left_motor.angle() > -20:
    #     left_motor.run_angle(50, -1, wait = False)
    #     right_motor.run_angle(50, 1, wait = True)
    #     motors.stop()
    # left_motor.reset_angle(0)
    # right_motor.reset_angle(0)
    
def turn_right(x):
    wait(200)
    brake_motors()
    valor_a_girar = 1226* (x / 360)
    left_motor.run_angle(200, valor_a_girar, wait = False)
    right_motor.run_angle(200, -valor_a_girar, wait = True)
    left_motor.hold()
    right_motor.hold()
    wait(200)
    if left_motor.angle() != valor_a_girar:
        left_motor.run_angle(5, (valor_a_girar - left_motor.angle()), wait = False)
    if right_motor.angle() != -valor_a_girar:
        right_motor.run_angle(5, (-valor_a_girar - right_motor.angle()), wait = True)
    print(left_motor.angle(), right_motor.angle())
    brake_motors()
    wait(200)
    
def turn_right_pid(x):  
    kp = 0.42
    ki = 0.0
    setpoint = 1226 * (x / 360)
    
    setpoint = round(setpoint)
      
    wait(200)
    brake_motors()
      
    while not abs(calculate_error(setpoint)) < 2.5:
        current_angle = left_motor.angle()
        control_signal = calcule(current_angle, setpoint, kp, ki)
        left_motor.run_angle(200, control_signal, wait = False)
        right_motor.run_angle(200, -control_signal, wait = True)
        
        print(left_motor.angle(), right_motor.angle())
        
        print(calculate_error(setpoint))
        
        # if(abs(calculate_error(setpoint)) < 1.5):
        # wait(200)
        # break
    # move_forward(500)
    
    brake_motors()
            
def turn_left_pid(x):  
    kp = 0.42
    ki = 0.0
    setpoint = 1226 * (x / 360)
      
    setpoint = round(setpoint)
    
    wait(200)
    brake_motors()
    
    while not (abs(calculate_error_right(setpoint)) < 2.5):
        current_angle = right_motor.angle()
        control_signal = calcule(current_angle, setpoint, kp, ki)
        left_motor.run_angle(200, -control_signal, wait = False)
        right_motor.run_angle(200, control_signal, wait = True)
        
        print(left_motor.angle(), right_motor.angle())
        
        print(calculate_error_right(setpoint))
        
        # if(abs(calculate_error_right(setpoint)) < 1.5):
        # wait(200)
        # break
    
    brake_motors()
    # move_forward(500)
    
    
def calcule(current_value, setpoint, kp, ki):
    integral = 0
    prev_error = 0
    
    error = setpoint - current_value
    p = error * kp
    
    integral += error
    i = integral * ki
    
    control_signal = p + i 
    
    prev_error = error  
    
    return control_signal 

def calculate_error(setpoint):
    return setpoint - left_motor.angle()

def calculate_error_right(setpoint):
    return setpoint - right_motor.angle()
     
    # motors.stop()
    # left_motor.reset_angle(0)
    # right_motor.reset_angle(0)
    # while right_motor.angle() > -20:
    #     left_motor.run_angle(50, 1, wait = False)
    #     right_motor.run_angle(50, -1, wait = True)
    #     motors.stop()
    # left_motor.reset_angle(0)
    # right_motor.reset_angle(0)
    
def ajust_color(cor_vista):
    print("Ajustando cor...")
    
    if cor_vista == "PRETO":
        if is_black_left() and not is_black_right():
            while not is_black_right():
                right_motor.run_angle(100, 1, wait = False)
                left_motor.run_angle(-50, 1, wait = False)
            brake_motors()
            
        elif not is_black_left() and is_black_right():
            
            while not is_black_left():
                left_motor.run_angle(100, 1, wait = False)
                right_motor.run_angle(-50, 1, wait = False)
            brake_motors()
        
        
# --------------------------------- 
        
    if cor_vista == "VERMELHO":
        if is_red_left() and not is_red_right():
            while not is_red_right():
                right_motor.run_angle(100, 1, wait = False)
                left_motor.run_angle(-50, 1, wait = False)
            brake_motors()
        elif not is_red_left() and is_red_right():
            while not is_red_left():
                left_motor.run_angle(100, 1, wait = False)
                right_motor.run_angle(-50, 1, wait = False)
            brake_motors()
    
# ---------------------------------
    
    if cor_vista == "AZUL":
        if is_blue_left() and not is_blue_right():
            while not is_blue_right():
                right_motor.run_angle(100, 1, wait = False)
                left_motor.run_angle(-50, 1, wait = False)
            brake_motors()
            
        elif not is_blue_left() and is_blue_right():
            
            while not is_blue_left():
                left_motor.run_angle(100, 1, wait = False)
                right_motor.run_angle(-50, 1, wait = False)
            brake_motors()

# ---------------------------------

    if cor_vista == "AMARELO":
        if is_yellow_left() and not is_yellow_right():
            while not is_yellow_right() and not is_black_right():
                right_motor.run_angle(100, 1, wait = False)
                left_motor.run_angle(-50, 1, wait = False)
            brake_motors()
            
        elif not is_yellow_left() and not is_black_left():
            
            while not is_yellow_left():
                left_motor.run_angle(100, 1, wait = False)
                right_motor.run_angle(-50, 1, wait = False)
            brake_motors()
            
# ---------------------------------

    if cor_vista == "PAREDE":
        if (is_black_left() or is_yellow_left()) and not (is_black_right() or is_yellow_right()):
            while not is_black_right() and not is_yellow_right():
                right_motor.run_angle(100, 1, wait = False)
                left_motor.run_angle(-50, 1, wait = False)
                
            brake_motors()
        elif not (is_black_left() or is_yellow_left()) and (is_black_right() or is_yellow_right()):
            while not is_black_left() and not is_yellow_left():
                left_motor.run_angle(100, 1, wait = False)
                right_motor.run_angle(-50, 1, wait = False)
            brake_motors()
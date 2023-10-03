from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch
from pybricks.robotics import DriveBase

from pybricks.tools import wait
from modules.path import *
from modules.variables import *
from modules.colors import *
from modules.beeps import *

left_motor = Motor(Port.A) 
right_motor = Motor(Port.B)

cronometer = StopWatch()

estabilizou = False
motors = DriveBase(left_motor, right_motor, 42.1, 150) # 140.88



# CONTROLE -----------------------------------------------------------------------------------------------

integral = 0
prev_delta = 0
time_teste = 0

def andar_reto(velo):
    global time_teste    
    global estabilizou
    time_teste += 1
    
    kp_left = 0.9
    kp_right = 1
    ki_left = 0.05
    ki_right = 0.1
    control_signal_left = left_motor.speed()
    control_signal_right = right_motor.speed()

    velo_double = velo

    control_signal_left += calcule(control_signal_left, velo_double, kp_left, ki_left)
    control_signal_right += calcule(control_signal_right, velo_double, kp_right, ki_right)

    if control_signal_left < 1 and control_signal_left > -1:
        control_signal_left = 1
    if control_signal_right < 1 and control_signal_right > -1:
        control_signal_right = 1

    right_motor.run(control_signal_right)
    left_motor.run(control_signal_left)
    
def calcule(current_value, setpoint, kp, ki):
    integral = 0
    
    error = setpoint - current_value
    p = error * kp
    
    integral += error
    i = integral * ki
    
    control_signal = p + i 
    
    return control_signal 

def calculate_error(setpoint):
    return setpoint - left_motor.angle()

def calculate_error_right(setpoint):
    return setpoint - right_motor.angle()

# FUNÇÕES BÁSICAS ----------------------------------------------------------------------------------------------------------------

def brake_motors():
    left_motor.hold()
    right_motor.hold()
    while left_motor.speed() != 0 or right_motor.speed() != 0:
        wait(1)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
def brake_motors_para_drive_base():
    while left_motor.speed() != 0 or right_motor.speed() != 0:
        motors.stop()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)


def move_forward(distancia, vel=500):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    motors.stop()
    angulo = (distancia * 3398)/124
    while left_motor.angle() < angulo or right_motor.angle() < angulo:
        andar_reto(vel)   
    # print(left_motor.angle(), right_motor.angle()) # Teste para o erro
    
    brake_motors()
 

    
def move_backward(distancia, vel=500):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    motors.stop()
    angulo = (distancia * -1496)/55
    while left_motor.angle() > angulo or right_motor.angle() > angulo:
        andar_reto(-vel)
    # print(left_motor.angle(), right_motor.angle()) # Teste para o erro
    
    brake_motors()

    
            
def turn_left_pid(x, vel=360):  
    kp = 1.0
    ki = 0.0156
    setpoint = 1228 * (x / 360)
      
    setpoint = round(setpoint)
    
    brake_motors()
    
    while not (abs(calculate_error_right(setpoint)) < 177):
        current_angle = right_motor.angle()
        current_angle += calcule(current_angle, setpoint, kp, ki)
        left_motor.run_angle(vel, -current_angle, wait = False)
        right_motor.run_angle(vel, current_angle, wait = True)
        
    brake_motors()
    
def turn_right_pid(x, vel=360):  
    kp = 1.0
    ki = 0.0156
    setpoint = 1228 * (x / 360)
    
    setpoint = round(setpoint)
    brake_motors()
      
    while not abs(calculate_error(setpoint)) < 176:
        current_angle = left_motor.angle()
        current_angle += calcule(current_angle, setpoint, kp, ki)
        left_motor.run_angle(vel, current_angle, wait = False)
        right_motor.run_angle(vel, -current_angle, wait = True)
    
    
    print(left_motor.angle(), right_motor.angle())
         
    brake_motors()
    
def turn_180():
    kp = 1.0
    ki = 0.0156
    setpoint = 1228/2
    setpoint = round(setpoint)
      
      
    brake_motors()
      
    while not abs(calculate_error(setpoint)) < 176:
        current_angle = left_motor.angle()
        current_angle += calcule(current_angle, setpoint, kp, ki)
        
        left_motor.run_angle(360, current_angle, wait = False)
        right_motor.run_angle(360, -current_angle, wait = True)


# ALINHAMENTO NAS CORES--------------------------------------------------------------------------------------------
     
def ajust_color(cor_vista):
    print("Ajustando cor...")
    brake_motors()

    move_backward(1)
    
# -----------------------------------------------------------------------------------------------------------------
    if cor_vista == "BLACK":
            
        while (red_left() not in get_treshold_left_black() ) or (red_right() not in get_treshold_right_black() ):
    
            while red_left() not in (get_treshold_left_black()) :
                
                while red_left() > (max(get_treshold_left_black())) : #white
                    left_motor.run(40)
                    right_motor.run(-5)
                brake_motors()
                
                while red_left() < min(get_treshold_left_black()) : #black
                    left_motor.run(-40)
                    right_motor.run(5)
                brake_motors()   

            while red_right() not in (get_treshold_right_black()) :
                
                while red_right() > (max(get_treshold_right_black())) : #white
                    right_motor.run(40)
                    left_motor.run(-5)
                brake_motors()
                    
                while red_right() < (min(get_treshold_right_black())) : #black
                    right_motor.run(-40)
                    left_motor.run(5)
                brake_motors()

# ----------------------------------------------------------------------------------------
    if cor_vista == "RED":
        
        
        while (green_left() not in get_treshold_left_red() ) or (green_right() not in get_treshold_right_red() ):
           
            while green_left() not in get_treshold_left_red() :
                
                while green_left() > max(get_treshold_left_red()) : #white
                    left_motor.run(40)
                    right_motor.run(-5)
                brake_motors()
                
                while green_left() < min(get_treshold_left_red()) : #black
                    left_motor.run(-40)
                    right_motor.run(5)
                brake_motors()

            while green_right() not in get_treshold_right_red() :
                
                while green_right() > max(get_treshold_right_red()) : #white
                    right_motor.run(40)
                    left_motor.run(-5)
                brake_motors()
                    
                while green_right() < min(get_treshold_right_red()) : #black
                    right_motor.run(-40)
                    left_motor.run(5)
                brake_motors()
    
# ----------------------------------------------------------------------------------------
    if cor_vista == "YELLOW":
        
        
        while (blue_left() not in get_treshold_left_yellow() ) or (blue_right() not in get_treshold_right_yellow()):
            
            while blue_left() not in get_treshold_left_yellow() :
                
                while blue_left() > max(get_treshold_left_yellow()) : 
                    left_motor.run(40)
                    right_motor.run(-5)
                brake_motors()
                
                while blue_left() < min(get_treshold_left_yellow()) : 
                    left_motor.run(-40)
                    right_motor.run(5)
                brake_motors()

            while blue_right() not in get_treshold_right_yellow():
                
                while blue_right() > max(get_treshold_right_yellow()): 
                    right_motor.run(40)
                    left_motor.run(-5)
                brake_motors()
                    
                while blue_right() < min(get_treshold_right_yellow()): 
                    right_motor.run(-40)
                    left_motor.run(5)         
                brake_motors()

    brake_motors()
    print("Cor ajustada!")   
    alined_to_wall()          
    brake_motors()
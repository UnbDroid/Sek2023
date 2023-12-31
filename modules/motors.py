from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch
from pybricks.robotics import DriveBase

from pybricks.tools import wait
from modules.colors import *
from modules.detect import *
from modules.path import *
from modules.variables import *

left_motor = Motor(Port.A) 
right_motor = Motor(Port.B)

cronometer = StopWatch()

estabilizou = False
motors = DriveBase(left_motor, right_motor, 42.1, 150) # 140.88

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
    #42
    # print("Sinal de controle esquerdo:", control_signal_left, "Sinal de controle direito:", control_signal_right)
    
    
def brake_motors():
    motors.stop()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

def teste():
    # cronometer.reset()
    #ELE ANDA 51 cm EM 10 SEGUNDOS
    #ELE ANDA 4,5 cm EM 298 MILISEGUNDOS
    # while cronometer.time() < 298:
    #     andar_reto(360)
    # brake_motors()
    while left_motor.angle() > -747 or right_motor.angle() > -747:
        andar_reto(-360)
    motors.stop()
    # print(left_motor.angle(), right_motor.angle())

def move_forward(distancia, vel=360):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    angulo = (distancia * 3398)/124
    while left_motor.angle() < angulo or right_motor.angle() < angulo:
        andar_reto(vel)
    motors.stop()
    print(left_motor.angle(), right_motor.angle())
    brake_motors()
    
def move_backward(distancia, vel=360):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    angulo = (distancia * -1496)/55
    while left_motor.angle() > angulo or right_motor.angle() > angulo:
        andar_reto(-vel)
    motors.stop()
    print(left_motor.angle(), right_motor.angle())
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
    # print(left_motor.angle(), right_motor.angle())
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
    # print(left_motor.angle(), right_motor.angle())
    brake_motors()
    wait(200)
            
def turn_left_pid(x):  
    kp = 1.0
    ki = 0.0156
    setpoint = 1224 * (x / 360)
      
    setpoint = round(setpoint)
    
    wait(200)
    brake_motors()
    
    while not (abs(calculate_error_right(setpoint)) < 177):
        current_angle = right_motor.angle()
        current_angle += calcule(current_angle, setpoint, kp, ki)
        left_motor.run_angle(200, -current_angle, wait = False)
        right_motor.run_angle(200, current_angle, wait = True)
        
        # print(left_motor.angle(), right_motor.angle())
        
        print(calculate_error_right(setpoint))
        
        # if(abs(calculate_error_right(setpoint)) < 1.5):
        # wait(200)
        # break
    
    brake_motors()
    # move_forward(500)
    
def turn_right_pid(x):  
    kp = 1.0
    ki = 0.0156
    setpoint = 1224 * (x / 360)
    
    setpoint = round(setpoint)
      
    wait(200)
    brake_motors()
      
    while not abs(calculate_error(setpoint)) < 176:
        current_angle = left_motor.angle()
        current_angle += calcule(current_angle, setpoint, kp, ki)
        left_motor.run_angle(200, current_angle, wait = False)
        right_motor.run_angle(200, -current_angle, wait = True)
        
        # print(left_motor.angle(), right_motor.angle())
        
        print(calculate_error(setpoint))
        
        # if(abs(calculate_error(setpoint)) < 1.5):
        # wait(200)
        # break
    # move_forward(500)
    
    brake_motors()
    
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
    brake_motors()
    wait(250)
    move_backward(1)
    
# ---------------------------------------------------------------------------------------- 
    if cor_vista == "BLACK":
            
        while (red_left() not in get_treshold_left_black() ) and (red_right() not in get_treshold_right_black() ):
    
            while red_left() not in (get_treshold_left_black()) :
                
                while red_left() > (max(get_treshold_left_black())) : #white
                    left_motor.run_angle(40, 1, wait = False)
                    right_motor.run_angle(-10, 1, wait = False)
                   
                
                while red_left() < min(get_treshold_left_black()) : #black
                    left_motor.run_angle(-40, 1, wait = False)
                    right_motor.run_angle(10, 1, wait = False)
                   

            while red_right() not in (get_treshold_right_black()) :
                
                while red_right() > (max(get_treshold_right_black())) : #white
                    right_motor.run_angle(40, 1, wait = False)
                    left_motor.run_angle(-10, 1, wait = False)
                    
                    
                while red_right() < (min(get_treshold_right_black())) : #black
                    right_motor.run_angle(-40, 1, wait = False)
                    left_motor.run_angle(10, 1, wait = False)


# ----------------------------------------------------------------------------------------
    if cor_vista == "RED":
        
        
        while (blue_left() not in get_treshold_left_red() ) and (blue_right() not in get_treshold_right_red() ):
           
            while blue_left() not in get_treshold_left_red() :
                
                while blue_left() > max(get_treshold_left_red()) : #white
                    left_motor.run_angle(40, 1, wait = False)
                    right_motor.run_angle(-10, 1, wait = False)
                   
                
                while blue_left() < min(get_treshold_left_red()) : #black
                    left_motor.run_angle(-40, 1, wait = False)
                    right_motor.run_angle(10, 1, wait = False)
                   

            while blue_right() not in get_treshold_right_red() :
                
                while blue_right() > max(get_treshold_right_red()) : #white
                    right_motor.run_angle(40, 1, wait = False)
                    left_motor.run_angle(-10, 1, wait = False)
                    
                    
                while blue_right() < min(get_treshold_right_red()) : #black
                    right_motor.run_angle(-40, 1, wait = False)
                    left_motor.run_angle(10, 1, wait = False)

    
# ----------------------------------------------------------------------------------------
    if cor_vista == "YELLOW":
        print(blue_left(), blue_right())
        while (blue_left() not in get_treshold_left_yellow() ) and (blue_right() not in get_treshold_right_yellow()):
            print("Entrei")
            while blue_left() not in get_treshold_left_yellow() :
                
                while blue_left() > max(get_treshold_left_yellow()) : 
                    left_motor.run_angle(40, 1, wait = False)
                    right_motor.run_angle(-10, 1, wait = False)
                
                
                while blue_left() < min(get_treshold_left_yellow()) : 
                    left_motor.run_angle(-40, 1, wait = False)
                    right_motor.run_angle(10, 1, wait = False)
                

            while blue_right() not in get_treshold_right_yellow():
                
                while blue_right() > max(get_treshold_right_yellow()): 
                    right_motor.run_angle(40, 1, wait = False)
                    left_motor.run_angle(-10, 1, wait = False)
                    
                    
                while blue_right() < min(get_treshold_right_yellow()): 
                    right_motor.run_angle(-40, 1, wait = False)
                    left_motor.run_angle(10, 1, wait = False)         

        
    print("Cor ajustada!")   
    alined_to_wall()          
    brake_motors()
    wait(500)
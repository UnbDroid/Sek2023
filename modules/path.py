from modules.motors import *
from modules.colors import *
from modules.detect import *
from pybricks.tools import StopWatch

pointed_to = 1
cardinal_points = ["N", "E", "S", "W"]
cronometer = StopWatch()
size_of_tube = 0
color_of_tube = ""
initial_path = [0, 0, 0, 0]
current_path = [0, 0, 0, 0]

def find_blue_line():
    cronometer.reset()
    while not is_blue_left() and not is_blue_right() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right():
        motors.drive(100,0)
    motors.stop()
    time_forward = cronometer.time()
    ajust_color()
    if not is_blue() and not is_red() and not is_black() and not is_yellow():
        while not is_blue_left() and not is_blue_right() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right():
            motors.drive(-40,0)
        motors.stop()
    if is_red():
        print("Achou vermelho")
        move_backward(2.5)
        turn_left()
        while not is_blue() and not is_black():
            motors.drive(100,0)
        if is_black():
            print("Achou parede")
            turn_right()
            turn_right()
            while not is_blue():
                motors.drive(100,0)
        motors.stop()
    elif is_black() or is_yellow():
        print("Achou parede")
        cronometer.reset()
        print("Resetou cronometro")
        print("Voltando...")
        while cronometer.time() < time_forward:
            motors.drive(-100,0)
        turn_right()
        find_blue_line()
    print(color_sensor_floor_left.rgb())
        
def align_to_begin_scan():
    move_backward(0.1)
    turn_right()
    motors.stop()
    while not is_red():
        motors.drive(100,0)
    turn_left()
    turn_left()

def scan():
    pointed_to = 0
    while not is_tube_of_15() and not is_tube_of_10():
        motors.drive(100,0)
        
    if is_tube_of_15():
        size_of_tube = 15
    if is_tube_of_10():
        size_of_tube = 10
        
    if is_red_tube():
        color_of_tube = "RED"
    if is_green_tube():
        color_of_tube = "GREEN"
    if is_blue_tube():
        color_of_tube = "BLUE"
    if is_brown_tube():
        color_of_tube = "BROWN"
        
def align_to_begin_deliver():
    pointed_to = 0
    while not is_red():
        motors.drive(100,0)
    move_backward(4)

def set_path():
    if size_of_tube == 15:
        if color_of_tube == "RED": #Farmacia
            initial_path = [0, 0, 0, 0]
        # if color_of_tube == "GREEN": #Prefeitura
            
        # if color_of_tube == "BLUE": #Museu
            
        # if color_of_tube == "BROWN": #Padaria
            
    # else:
    #     if color_of_tube == "GREEN": #Parque
    #         print('oi'')
        # if color_of_tube == "BLUE": #Escola
            
        # if color_of_tube == "BROWN": #Biblioteca
            
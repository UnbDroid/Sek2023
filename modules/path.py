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
    break_motors()
    
    print("procurando")
    while not is_blue() and not is_red() and not is_black() and not is_yellow() and not is_wall():
        andar_reto(40)   
        if is_blue():
            cor_vista = "AZUL"
        elif is_red():
            cor_vista = "VERMELHO"
        elif is_black():
            cor_vista = "PRETO"
        elif is_yellow():
            cor_vista = "AMARELO"
        elif is_wall():
            cor_vista = "PAREDE"
    break_motors()
    
    
    time_forward = cronometer.time()
    ajust_color()
    if not is_blue() and not is_red() and not is_black() and not is_yellow():
        while not is_blue_left() and not is_blue_right() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right():
            andar_reto(-20)
        break_motors()
        
        
    if is_red():
        
        print("Achou vermelho")
        move_backward(3500) #Ajuste para ver como lida com o "andar reto"
        turn_left(90)
        break_motors()
        
        while not is_blue() and not is_black() and not is_yellow() and not is_wall():
            andar_reto(50)
        if is_black() or is_yellow() or is_wall():
            print("Achou parede")
            turn_left(190)
            break_motors()
            
            while not is_blue():
                andar_reto(50)
        break_motors()
        
        
    elif is_black() or is_yellow() or is_wall():
        
        # erro !!!
        # Mudar quando ele está no C olhando para o amarelo, e pensar de um jeito de deixar mais simples quando encontra o vermelho direto. Ele fica em um loop infinito virando 180° 
        # Mudar a condicional de vermelho
        
        print("Achou parede")
        cronometer.reset()
        print("Voltando...")
        while cronometer.time() < time_forward:
            andar_reto(-40)
            
        break_motors()
        turn_right(90)
        
        # while not is_black() and not is_yellow():
        #     andar_reto(-50)
        
        find_blue_line()
    
        
# def align_to_begin_scan():
#     print("Achei o azul")
#     move_backward(0.1)
#     turn_right(90)
#     break_motors()
#     while not is_red():
#         andar_reto(50)
#     turn_left(190)
    

def scan():
    turn_left(90)
    pointed_to = 0
    branco = 68
    azul = 12
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    chegou_no_fim = False
    integral = 0
    prev_error = 0
    while True:  # not is_tube_of_15() and not is_tube_of_10():
        red_reading = red_right()
        delta = red_reading - threshold
        kp = 1.2
        ki = 0.001  # Tune as needed
        kd = 0.01   # Tune as needed
        error = delta * kp
        integral += error
        integral = max(min(integral, 100), -100)  # Anti-windup
        derivative = error - prev_error
        control_output = error * kp + integral * ki + derivative * kd
        prev_error = error
        if chegou_no_fim:
            motors.drive(-vel, -control_output)
        else:
            motors.drive(vel, control_output)
            if is_red_left():
                chegou_no_fim = True
        
    # if is_tube_of_15():
    #     size_of_tube = 15
    # if is_tube_of_10():
    #     size_of_tube = 10
        
    # if is_red_tube():
    #     color_of_tube = "RED"
    # if is_green_tube():
    #     color_of_tube = "GREEN"
    # if is_blue_tube():
    #     color_of_tube = "BLUE"
    # if is_brown_tube():
    #     color_of_tube = "BROWN"
        
def align_to_begin_deliver():
    pointed_to = 0
    while not is_red():
        andar_reto(50)
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
            
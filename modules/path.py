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
    motors.stop()
    
    print("procurando")
    while not is_blue() and not is_red() and not is_black() and not is_yellow():
        andar_reto(50)   
    motors.stop()
    
    time_forward = cronometer.time()
    # ajust_color()
    
    if not is_blue() and not is_red() and not is_black() and not is_yellow():
        while not is_blue_left() and not is_blue_right() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right():
            andar_reto_tras(20)
        motors.stop()
        
        
    if is_red():
        
        print("Achou vermelho")
        move_backward(2.5) #Ajuste para ver como lida com o "andar reto"
        turn_left(90)
        motors.stop()
        
        while not is_blue() and not is_black():
            andar_reto(50)
        if is_black():
            print("Achou parede")
            move_backward(2.5)
            turn_left(90)
            motors.stop()
            
            while not is_blue():
                andar_reto(50)
        motors.stop()
        
        
    elif is_black() or is_yellow() or is_wall():
        
        # erro !!!
        # Mudar quando ele está no C olhando para o amarelo, e pensar de um jeito de deixar mais simples quando encontra o vermelho direto. Ele fica em um loop infinito virando 180° 
        # Mudar a condicional de vermelho
        
        print("Achou parede")
        cronometer.reset()
        print("Voltando...")
        while cronometer.time() < time_forward:
            andar_reto(-50)
            
        motors.stop()
        turn_right(190)
        
        # while not is_black() and not is_yellow():
        #     andar_reto(-50)
        
        find_blue_line()
    
        
def align_to_begin_scan():
    print("Achei o azul")
    move_backward(0.1)
    turn_right(90)
    motors.stop()
    while not is_red():
        andar_reto(50)
    turn_left(190)
    

def scan():
    pointed_to = 0
    while not is_tube_of_15() and not is_tube_of_10():
        andar_reto(50)
        
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
            
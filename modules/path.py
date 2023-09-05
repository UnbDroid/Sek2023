from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.claw import *
from modules.delivery import *
from pybricks.tools import StopWatch

pointed_to = 1
cardinal_points = ["N", "E", "S", "W"]
cronometer = StopWatch()
size_of_tube = 0
color_of_tube = ""
initial_path = [0, 0, 0, 0]
current_path = [0, 0, 0, 0]

# server 
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

def find_blue_line(numero_de_paredes):
    if numero_de_paredes < 4:
        cronometer.reset()
        brake_motors()
        
        cor_vista = ""
        
        print("procurando")
        while not is_blue() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right() and not has_obstacle():
            andar_reto(360)   
            #print("RGB Esquerdo: ", red_left(), green_left(), blue_left(), "RGB Direito: ", red_right(), green_right(), blue_right())
            if is_blue():
                cor_vista = "AZUL"
            elif is_red_left() or is_red_right():
                cor_vista = "VERMELHO"
            elif is_black_left() or is_black_right():
                cor_vista = "PAREDE"
            elif is_yellow_left() or is_yellow_right():
                cor_vista = "PAREDE"
        brake_motors()
        time_forward = cronometer.time()
        ajust_color(cor_vista)
        if not is_blue() and not (is_red_left() or is_red_right()) and not (is_black_left() or is_black_right()) and not (is_yellow_left() or is_yellow_right()) and not has_obstacle():
            while not is_blue_left() and not is_blue_right() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right():
                andar_reto(-360)
            brake_motors()
            
        if (is_red_left() or is_red_right()):
            print("Achou vermelho")
            brake_motors()
            move_backward(3500) 
            turn_left_pid(90)
            brake_motors()
            
            while not is_blue() and not (is_black_left() or is_black_right()) and not (is_yellow_left() or is_yellow_right()) and not is_wall():
                andar_reto(360)
            if (is_black_left() or is_black_right()) or (is_yellow_left() or is_yellow_right()) or is_wall():
                print("Achou parede")
                brake_motors()
                turn_left_pid(180)
                brake_motors()
                
                while not is_blue():
                    andar_reto(360)
            brake_motors()
            
            
        elif (is_black_left() or is_black_right()) or (is_yellow_left() or is_yellow_right()) or is_wall() or has_obstacle():
            print("Achou parede")
            cronometer.reset()
            print("Voltando...")
            while cronometer.time() < time_forward:
                andar_reto(-360)
                
            brake_motors()
            turn_right_pid(90)
            
            find_blue_line(numero_de_paredes + 1)
    else:
        turn_left_pid(90)
        while ultrasound_sensor.distance() > 145 and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right():
            andar_reto(360)
        brake_motors()
        if is_wall():
            move_backward(500)
        turn_left_pid(90)
        find_blue_line(0)
        
def align_to_begin_scan():
    brake_motors()
    print("Achei o azul")
    move_backward(100)
    turn_right_pid(90)
        
    branco = 80
    azul = 10
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    chegou_no_fim = False
    while not chegou_no_fim:
        
        delta = threshold - red_left()
        kp = 0.8
        erro = delta * kp
        motors.drive(vel, erro)
        
        if is_red_right():
            chegou_no_fim = True
            brake_motors()
            
    turn_left_pid(90)
    move_forward(1400)
    turn_left_pid(90)
    

def scan():
    global color_of_tube
    global size_of_tube
    cronometer.reset()
    print("Procurando tubo...")
    while not tube_is_detected():
        andar_reto(150)
    brake_motors()
    tempo = cronometer.time()
    
    mbox.send('chave')
    mbox.wait()

    size_of_tube = mbox.read()
    size_of_tube = int(size_of_tube)
    
    
    Close()
    
    if is_red_tube():
        color_of_tube = "RED"
    elif is_green_tube():
        color_of_tube = "GREEN"
    elif is_blue_tube():
        color_of_tube = "BLUE"
    else:
        color_of_tube = "BROWN"
        
    print("Tubo encontrado:", size_of_tube, "de cor", color_of_tube)
    
    cronometer.reset()
    
    valor_giro = -3
    metrica = 6000
    while cronometer.time() < tempo:
        andar_reto(-150)
    brake_motors()
    
        
    print("Sai do scan")
        
        
def align_to_begin_deliver():
    turn_right_pid(90)
    move_backward(1200)
    turn_left_pid(90)

def set_path():
    global color_of_tube
    global size_of_tube
    
    print("Entrei")
    if size_of_tube == 15:
        print("Tem 15 cm")#$%¨&*(
        if color_of_tube == "RED": #Farmacia
            tube_drugstore()
        if color_of_tube == "GREEN": #Prefeitura
            tube_city_hall()
        if color_of_tube == "BLUE": #Museu
            tube_museum()
        if color_of_tube == "BROWN": #Padaria
            tube_bakery()
    else:
        print("Entrei no else")#$%¨&*(
        
        if color_of_tube == "GREEN": #Parque
            tube_park()
        if color_of_tube == "BLUE": #Escola
            tube_school()
        if color_of_tube == "BROWN": #Biblioteca
            tube_library()
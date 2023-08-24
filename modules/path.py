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

def find_blue_line():
    cronometer.reset()
    break_motors()
    
    print("procurando")
    while not is_blue() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right():
        andar_reto(50)   
        #print("RGB Esquerdo: ", red_left(), green_left(), blue_left(), "RGB Direito: ", red_right(), green_right(), blue_right())
        if is_blue():
            cor_vista = "AZUL"
        elif is_red_left() or is_red_right():
            cor_vista = "VERMELHO"
        elif is_black_left() or is_black_right():
            cor_vista = "PAREDE"
        elif is_yellow_left() or is_yellow_right():
            cor_vista = "PAREDE"
    break_motors()
    
    
    time_forward = cronometer.time()
    ajust_color()
    if not is_blue() and not (is_red_left() or is_red_right()) and not (is_black_left() or is_black_right()) and not (is_yellow_left() or is_yellow_right()):
        while not is_blue_left() and not is_blue_right() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right():
            andar_reto(-20)
        break_motors()
        
        
    if (is_red_left() or is_red_right()):
        print("Achou vermelho")
        move_backward(3500) 
        turn_left(90)
        break_motors()
        
        while not is_blue() and not (is_black_left() or is_black_right()) and not (is_yellow_left() or is_yellow_right()) and not is_wall():
            andar_reto(50)
        if (is_black_left() or is_black_right()) or (is_yellow_left() or is_yellow_right()) or is_wall():
            print("Achou parede")
            turn_left(190)
            break_motors()
            
            while not is_blue():
                andar_reto(50)
        break_motors()
        
        
    elif (is_black_left() or is_black_right()) or (is_yellow_left() or is_yellow_right()) or is_wall():
        
        print("Achou parede")
        cronometer.reset()
        print("Voltando...")
        while cronometer.time() < time_forward:
            andar_reto(-50)
            
        break_motors()
        turn_right(93)
        
        find_blue_line()
    
        
def align_to_begin_scan():
    break_motors()
    print("Achei o azul")
    if size_of_tube != 10 and color_of_tube != "BROWN":
        while is_blue():
            andar_reto(-50)   
        break_motors()
    if size_of_tube == 10 and color_of_tube == "BROWN":
        turn_right(110)
    else:
        turn_right(90)
        
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
            break_motors()
            move_backward(1500)
    branco = 80
    azul = 10
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    chegou_no_fim = False
    cronometer.reset()
    while cronometer.time() < 1450:
        delta = threshold - red_left()
        kp = 0.8
        erro = delta * kp
        motors.drive(vel, erro)
    break_motors()
    turn_left(90)
    move_forward(1200)
    turn_left(90)
    

def scan():
    global color_of_tube
    global size_of_tube
    cronometer.reset()
    valor_giro = 3
    print("Procurando tubo...")
    metrica = 6000
    while not tube_is_detected():
        andar_reto(30)
        if cronometer.time() > metrica:
            turn_left(valor_giro)
            metrica += 6000
    tempo = cronometer.time()
    
    break_motors()
    mbox.send('chave')
    mbox.wait()

    size_of_tube = mbox.read()
    size_of_tube = int(size_of_tube)
    
    
    Close()
    
    # Após fechar a garra
    

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
        andar_reto(-30)
    break_motors()
    
    
    # if not tube_is_detected():
    #     print("Entrei de novo no scan")
    #     Open()
    #     scan()
        
    print("Sai do scan")
        
        
def align_to_begin_deliver():
    turn_right(90)
    move_backward(1200)
    turn_left(90)

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
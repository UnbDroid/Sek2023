from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.claw import *
from modules.tube import *
from pybricks.tools import StopWatch

pointed_to = 1
cardinal_points = ["N", "E", "S", "W"]
cronometer = StopWatch()
size_of_tube = 0
color_of_tube = ""
initial_path = [0, 0, 0, 0]
current_path = [0, 0, 0, 0]

SERVER = 'ev3dev'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')


def find_blue_line():
    cronometer.reset()
    break_motors()
    
    print("procurando")
    while not is_blue() and not is_red() and not is_black() and not is_yellow() and not is_wall():
        andar_reto(50)   
        #print("RGB Esquerdo: ", red_left(), green_left(), blue_left(), "RGB Direito: ", red_right(), green_right(), blue_right())
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
        move_backward(3500) 
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
        
        print("Achou parede")
        cronometer.reset()
        print("Voltando...")
        while cronometer.time() < time_forward:
            andar_reto(-50)
            
        break_motors()
        turn_right(90)
        
        find_blue_line()
    
        
def align_to_begin_scan():
    break_motors()
    print("Achei o azul")
    turn_right(90)
    break_motors()
    branco = 99
    azul = 22
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
    turn_left(90)
    move_forward(1200)
    turn_left(90)
    

def scan():
    cronometer.reset()
    print("Procurando tubo...")
    
    while not tube_is_detected():
        andar_reto(30)
    tempo = cronometer.time()
    
    break_motors()
    Close()
    
    # Após fechar a garra
    mbox.send('chave')
    mbox.wait()

    size_of_tube = int(mbox.read())
    
    if is_red_tube():
        color_of_tube = "RED"
    elif is_green_tube():
        color_of_tube = "GREEN"
    elif is_blue_tube():
        color_of_tube = "BLUE"
    else:
        color_of_tube = "BROWN"
        
    
    
    #Aqui é o momento que o Brick Auxiliar faz a leitura do tamanho do tubo
    #num primeiro momento, pra testar, todos os tubos vão ser considerados de 10 :)
    
    size_of_tube = 10
    
    # if is_tube_of_15():
    #     size_of_tube = 15
    # if is_tube_of_10():
    #     size_of_tube = 10
    
    cronometer.reset()
    
    while cronometer.time() < tempo:
        andar_reto(-30)
    break_motors()
        
        
def align_to_begin_deliver():
    turn_right(90)
    move_backward(1200)
    turn_left(90)

def set_path():
    if size_of_tube == 15:
        if color_of_tube == "RED": #Farmacia
            tube_pharmacy()
        if color_of_tube == "GREEN": #Prefeitura
            tube_city_hall()
        if color_of_tube == "BLUE": #Museu
            tube_museum()
        if color_of_tube == "BROWN": #Padaria
            tube_bakery()
    else:
        if color_of_tube == "GREEN": #Parque
            tube_park()
        if color_of_tube == "BLUE": #Escola
            tube_school()
        if color_of_tube == "BROWN": #Biblioteca
            tube_library()
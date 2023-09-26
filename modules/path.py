from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.claw import *
from modules.delivery import *
from pybricks.tools import StopWatch

ev3 = EV3Brick()
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

ev3.speaker.beep(444, 1000)
print('waiting for connection...')
server.wait_for_connection()
print('connected!')


# Se alinhando no azul para iniciar o scan ---------------------------------------------------------------------------------
      
def align_to_begin_scan():
    brake_motors()
    print("Achei o azul")
    move_backward(1)
    turn_right_pid(90)
        
    branco = range_white_left()[0] # 80
    azul = range_blue_left()[0] 
    threshold = (branco + azul) / 2  # = 40
    vel = 150
    chegou_no_fim = False
    
    while not chegou_no_fim:
        
        delta = threshold - red_left()
        kp = 0.45
        erro = delta * kp
        motors.drive(vel, erro)
        
        if is_red_right():
            chegou_no_fim = True
            brake_motors_para_drive_base()
    
    
    # Manobra na área de coleta 
    # wait(300)
    move_backward(0.7)
   
    # wait(300) 
    turn_left_pid(90)
    
    # wait(300) 
    move_forward(15)

    # wait(300) 
    turn_left_pid(90)
        
def scan():
    global color_of_tube
    global size_of_tube
    
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    print("Procurando tubo...")
    while not tube_is_detected():
        andar_reto(200)
    angulo_esquerdo = left_motor.angle()
    angulo_direito = right_motor.angle()
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
    
    brake_motors()
    
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    while left_motor.angle() > ((-angulo_esquerdo) + 20) or right_motor.angle() > ((-angulo_direito) + 20):
        andar_reto(-500)
    
    brake_motors()
    
    print("Sai do scan")
       
def set_path():
    global color_of_tube
    global size_of_tube
    
    print("Entrei")
    if size_of_tube == 15:
        
        print("Tem 15 cm")
        if color_of_tube == "RED": #Farmacia
            tube_drugstore()
        if color_of_tube == "GREEN": #Prefeitura
            tube_city_hall()
        if color_of_tube == "BLUE": #Museu
            tube_museum()
        if color_of_tube == "BROWN": #Padaria
            tube_bakery()
    else:
        # print("Tem 10 cm")
        
        if color_of_tube == "GREEN": #Parque
            tube_park()
        if color_of_tube == "BLUE": #Escola
            tube_school()
        if color_of_tube == "BROWN": #Biblioteca
            tube_library()
        if color_of_tube == "RED":
            tube_drugstore()
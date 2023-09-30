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
quanto_andou_pra_frente = [0, 0]

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
    Open()
    branco = range_white_left()[0] 
    azul = range_blue_left()[0] 
    threshold = (branco + azul) / 2 
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
    move_backward(1.5) 
   
    turn_left_pid(90)
    
    move_forward(15)

    turn_left_pid(90)



def align_to_be_ladinho():
    turn_left_pid(90)
    Open()
    move_backward(1)
    
def scan():
    global color_of_tube
    global size_of_tube
    
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    azul = 7
    branco = 52
    threshold = (azul + branco) / 2
    
    print("Procurando tubo...")
    while True:
        erro = (red_aux() - threshold) * 0.45
        mbox.send("tem tubo?")
        mbox.wait()
        tem_tubo = mbox.read()
        if tem_tubo == "tem tubo":
            break
        motors.drive(80, erro)
        
    angulo_esquerdo = left_motor.angle()
    angulo_direito = right_motor.angle()
    brake_motors_para_drive_base()
    brake_motors()
    
    mbox.send('chave')
    mbox.wait()

    size_of_tube = mbox.read()
    size_of_tube = int(size_of_tube)
    
    Close()
    
    mbox.send('cor do tubo')
    mbox.wait()
    
    color_of_tube = mbox.read()
        
    print("Tubo encontrado:", size_of_tube, "de cor", color_of_tube)
    
    brake_motors()

    
    while left_motor.angle() > ((-angulo_esquerdo) + 20) or right_motor.angle() > ((-angulo_direito) + 20):
        andar_reto(-400)
    brake_motors_para_drive_base()
    
    print("Sai do scan")


def scan_de_ladinho_papai():
    global color_of_tube
    global size_of_tube
    global quanto_andou_pra_frente

    branco = range_white_right()[0] 
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2

    while not is_red_left():
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(150, erro)
    brake_motors_para_drive_base()
    move_backward(1.5)
    turn_left_pid(90)
    move_forward(5)
    turn_left_pid(90)

    azul = 7
    branco = 52
    threshold = (azul + branco) / 2

    print("1")
    
    if quanto_andou_pra_frente != [0, 0]:
        while left_motor.angle() < quanto_andou_pra_frente[0] or right_motor.angle() < quanto_andou_pra_frente[1]:
            erro = (red_aux() - threshold) * -0.45
            mbox.send("de_ladinho")
            mbox.wait()
            tem_tubo = mbox.read()
            if tem_tubo == "Vi tubo":
                break
            motors.drive(100, erro)
        brake_motors_para_drive_base() 

    print("2")

    while True:
        erro = (red_aux() - threshold) * -0.45
        mbox.send("de_ladinho")
        mbox.wait()
        tem_tubo = mbox.read()
        if tem_tubo == "Vi tubo":
            break
        else:
            print(tem_tubo)
            motors.drive(40, erro)
    
    quanto_andou_pra_frente[0] += left_motor.angle()
    quanto_andou_pra_frente[1] += right_motor.angle() 
    brake_motors_para_drive_base()
    deu_bom_familia()

    
    # # manobras --- 
    move_forward(3.8, 60)
    turn_left_pid(90)
    Close(esperar=False)
    # wait(200)
    move_forward(11, 360)
    while claw_motor.speed() != 0:
        wait(1)

    #com o tubo

    move_backward(11)
    turn_right_pid(90)
            
    azul = 7
    branco = 52
    threshold = (azul + branco) / 2
    
    vel = 150
    chegou_no_fim = False

    while not chegou_no_fim:
        
        delta = threshold - red_aux()
        kp = 0.45
        erro = delta * kp
        motors.drive(vel, erro)
        
        if is_red_right():
            chegou_no_fim = True
            brake_motors_para_drive_base()


    move_backward(1.5) #0.7

    while left_motor.speed() != 0 or right_motor.speed() != 0:
        wait(1)

    mbox.send('chave')
    mbox.wait()
    size_of_tube = mbox.read()
    size_of_tube = int(size_of_tube)

    mbox.send('cor do tubo')
    mbox.wait()
    
    color_of_tube = mbox.read()
        
    print("Tubo encontrado:", size_of_tube, "de cor", color_of_tube)
    turn_left_pid(90)
    move_forward(7.5)
    turn_left_pid(90)

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

        if color_of_tube == "GREEN": #Parque
            tube_park()
        if color_of_tube == "BLUE": #Escola
            tube_school()
        if color_of_tube == "BROWN": #Biblioteca
            tube_library()
        if color_of_tube == "RED":
            tube_drugstore()
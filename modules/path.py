from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.claw import *
from modules.delivery import *
from pybricks.tools import StopWatch

dar_pra_tras = False

ev3 = EV3Brick()
cronometer = StopWatch()
size_of_tube = 0
color_of_tube = ""
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
      
def align_to_begin_scan(velocidade = 150):
    global dar_pra_tras
    set_dar_pra_tras(True)
    dar_pra_tras = get_dar_pra_tras
    brake_motors()
    print("Achei o azul")
    move_backward(1)
    turn_right_pid(90)
    
    branco = range_white_left()[0] 
    azul = range_blue_left()[0] 
    threshold = (branco + azul) / 2 

    chegou_no_fim = False
    
    while not chegou_no_fim:
        delta = threshold - red_left()
        kp = 0.45
        erro = delta * kp
        motors.drive(velocidade, erro)
        
        if is_red_right() :
            chegou_no_fim = True
            brake_motors_para_drive_base()
            brake_motors()
    
    
    # Manobra na área de coleta 
    move_backward(3) 
   
    turn_left_pid(90)
    
    move_forward(15)

    turn_left_pid(90)



def align_to_be_ladinho(): 
    global dar_pra_tras
    set_dar_pra_tras(False)
    dar_pra_tras = get_dar_pra_tras
    turn_left_pid(90)
    move_backward(1)
  
# Tatica para pegar os tubos, seja de lado ou por dentro ----------------------------------------------------------
  
def scan():
    global color_of_tube
    global size_of_tube
    global quanto_andou_pra_frente
    
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    azul = 12
    branco = 62
    threshold = (azul + branco) / 2
    
    if quanto_andou_pra_frente != [0, 0]:
        while left_motor.angle() < quanto_andou_pra_frente[0] or right_motor.angle() < quanto_andou_pra_frente[1]:
            erro = (red_aux() - threshold) * 0.45
            mbox.send("de_ladinho")
            mbox.wait()
            tem_tubo = mbox.read()
            if tem_tubo == "Vi tubo":
                break
            motors.drive(180, erro)
        brake_motors_para_drive_base()
        brake_motors()
    
    print("Procurando tubo...")
    while True:
        erro = (red_aux() - threshold) * 0.45
        mbox.send("tem tubo?")
        mbox.wait()
        tem_tubo = mbox.read()
        if tem_tubo == "tem tubo":
            break
        motors.drive(80, erro)
        
    quanto_andou_pra_frente[0] += left_motor.angle()
    quanto_andou_pra_frente[1] += right_motor.angle()
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

    
    while left_motor.angle() > (- (quanto_andou_pra_frente[0]) + 30) or right_motor.angle() > (- (quanto_andou_pra_frente[1]) + 30):
        andar_reto(-400)
    brake_motors_para_drive_base()
    brake_motors()
    
    print("Sai do scan")


def scan_de_ladinho_papai(): 
    global color_of_tube
    global size_of_tube
    global quanto_andou_pra_frente

    branco = range_white_right()[0] 
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2

    # while not is_red_left() and red_left() >= 50:
    #     delta = red_right() - threshold
    #     kp = 0.5
    #     erro = delta * kp
    #     motors.drive(150, erro) #! VELOCIDADE ARRUMANDO
        
    chegou_no_fim = False

    while not chegou_no_fim:
        if is_red_left() and red_left() >= range_meio_blue_left()[0]:
            chegou_no_fim = True
            brake_motors_para_drive_base()
            brake_motors()
            break
        
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(150, erro) #! VELOCIDADE ARRUMANDO
        
        if is_red_left() and red_left() >= range_meio_blue_left()[0]:
            chegou_no_fim = True
            brake_motors_para_drive_base()
            brake_motors()
            break


            
    # brake_motors_para_drive_base()
    # brake_motors()

    
    move_backward(5)
    turn_180()

    azul = range_blue_left()[0]
    branco = range_white_left()[0]
    threshold = (azul + branco) / 2

    if quanto_andou_pra_frente != [0, 0]:
        while left_motor.angle() < quanto_andou_pra_frente[0] or right_motor.angle() < quanto_andou_pra_frente[1]:
            erro = (red_left() - threshold) * -0.45
            if tube_is_detected():
                brake_motors_para_drive_base()
                brake_motors()
                break
            motors.drive(180, erro) #! VELOCIDADE ARRUMANDO
        brake_motors_para_drive_base()
        brake_motors()

    while not tube_is_detected():
        erro = (red_left() - threshold) * -0.45
        motors.drive(50, erro)
        
        
    
    quanto_andou_pra_frente[0] += left_motor.angle()
    quanto_andou_pra_frente[1] += right_motor.angle() 
    brake_motors_para_drive_base()
    brake_motors()
    deu_bom_familia()

    
    # manobras -----------------
    #? Teste
    
    while tube_is_detected():
        andar_reto(-40)
    brake_motors()
    move_backward(2)
    #? move_backward(4.5, 60) #Aqui
    Close()
    turn_left_pid(90)
    move_backward(3,100)
    Open()
    #? move_forward(3,100)
    Close(esperar=False, time = 600) #FAZER : Talvez arrumar o tempo

    move_forward(9, 380)
    while claw_motor.speed() != 0:
        wait(1)

    #com o tubo

    move_backward(9)
    turn_right_pid(90)

    azul = range_blue_left()[0]
    branco = range_white_left()[0]
    threshold = (azul + branco) / 2
    
    chegou_no_fim = False

    while not chegou_no_fim:
        
        delta = threshold - red_left()
        kp = 0.5
        erro = delta * kp
        motors.drive(150, erro) #! VELOCIDADE ARRUMANDO
        
        if is_red_right():
            chegou_no_fim = True
            brake_motors_para_drive_base()
            brake_motors()


    move_backward(2) 

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
    
    print("Manobra")
    turn_180()

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
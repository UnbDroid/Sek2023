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
    move_backward(0.2) #0.1
    turn_left_pid(90)
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
    mbox.send('de_ladinho')
    mbox.wait()
    scan_tube=mbox.read()
    
    
    if scan_tube == "Vi tubo":  
        while True:
            mbox.send('de_ladinho')
            mbox.wait()
            scan_tube = mbox.read()
            if scan_tube == "Sem tubo":
                break
            andar_reto(-35)
            
        move_backward(5.35) 
    
            
            
    branco = range_white_right()[0] 
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2  
    vel = 100

    mbox.send('de_ladinho')
    mbox.wait()
    scan_tube=mbox.read()

    
    while scan_tube == 'Sem tubo':
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro) 
        
        # ---- novo  
        if is_red_left():
            brake_motors_para_drive_base()
            turn_180()
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
            
            move_backward(1.5)
            turn_180()
        
        # -------
        mbox.send('de_ladinho')
        mbox.wait()
        scan_tube = mbox.read()

        
    brake_motors_para_drive_base()
    deu_bom_familia()

    
    # # manobras --- 

    move_forward(4)
    turn_right_pid(90, 72)
    Close(False)
    wait(70)
    move_forward(5, 250)
    mbox.send('chave')
    mbox.wait()
        
    

    size_of_tube = mbox.read()
    size_of_tube = int(size_of_tube)
    while claw_motor.speed() != 0:
        wait(1)

    #com o tubo

    move_backward(5)
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


    move_backward(1.5) #0.7

    while left_motor.speed() != 0 or right_motor.speed() != 0:
        wait(1)

    mbox.send('cor do tubo')
    mbox.wait()
    
    color_of_tube = mbox.read()
        
    print("Tubo encontrado:", size_of_tube, "de cor", color_of_tube)
    turn_left_pid(90)
    move_forward(2)
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
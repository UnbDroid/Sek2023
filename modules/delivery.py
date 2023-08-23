from modules.motors import *
from modules.beeps import *
from modules.claw import *

from pybricks.tools import StopWatch

crono = StopWatch()

def go_to_check_point():
    turn_right(90)
    move_backward(1200)
    turn_left(90)

def tube_library():
    
    crono.reset()
    branco = 100 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 600:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)  
    turn_left(90)
    
    crono.reset()
    while not is_yellow_left() and not is_yellow_right():
        andar_reto(50)
    tempo = crono.time()
    break_motors()
    found_door()
    
    move_forward(300) # Indo para a entrega
    Open()
    move_backward(600) # Volta para a área de coleta a msm distância de ir
    
    turn_left(200)
    
    while not is_blue():
        andar_reto(50)
    break_motors()
    
        
    
def tube_city_hall():
    crono.reset()
    branco = 100 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 4000:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    break_motors()
    turn_left(90)
    move_forward(1000) # Está indo em direção ao objeto J
    
    if has_obstacle(): #sensor identificou objeto "J":
        move_backward(1)
        turn_right(90)
        move_forward(3)
        turn_left(90)
        move_forward(2)
        turn_left(90)
        move_forward(2)
        Open()
        #retorna para a área de coleta
        move_backward(2)
        turn_left(90)
        move_forward(3)
    
    else:
        #objeto J não existe
        move_forward(2750)#Distancia pequena 3500
        turn_right(90)
        
        #tentativa de se alinhar
        while not is_yellow_left() and not is_yellow_right():
            andar_reto(50)
        break_motors()
        
        move_forward(1000)
        Open()
        #retorna para a área de coleta
        move_backward(1500)
        turn_right(90)
        
        while not is_blue():
            andar_reto(50)
        break_motors()
        

    
def tube_school():
    
    crono.reset()
    branco = 100 
    azul = 14 #22 
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 10000:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    break_motors()
    turn_left(90)
    move_forward(1000)
    
    if has_obstacle(): #sensor identificou objeto "i":
        move_backward(1)
        turn_left(90)
        move_forward(4)
        turn_right(90)
        move_forward(4)
        turn_right(90)
        #while not is_red():
        #    move_forward(): sugestão, bater no vermelho e dai voltar
        move_forward(6)
        turn_right(90)
        move_forward(2)
        #abre e retorna
        Open()
        move_backward(2)
        turn_right(90)
        move_forward(6)
        turn_left(90)
        move_forward(4)
    else:
        move_forward(2750)#Distancia pequena 3500
        turn_right(90)
        
        #tentativa de se alinhar
        while not is_yellow_left() and not is_yellow_right():
            andar_reto(50)
        break_motors()
        
        move_forward(1000)
        Open()
        #retorna para a área de coleta
        move_backward(1500)
        turn_right(90)
        
        while not is_blue():
            andar_reto(50)
        break_motors()
        
def tube_museum():
    
    crono.reset()
    branco = 100 
    azul = 14 #22
    threshold = (branco + azul) / 2  
    vel = 100
    while crono.time() < 3500: #4000
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    break_motors()
    turn_left(90)
    move_forward(1000) # Está indo em direção ao objeto J
    
    if has_obstacle(): #sensor identificou objeto "j":
        turn_right(90)
        move_forward(4)
        turn_left(90)
        move_forward(4)
        turn_left(90)
        move_forward(2)
        if has_obstacle(): #sensor identificou objeto G:
            move_backward(2)
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(4)
            turn_left(90)
            move_forward(4)
            turn_right(90)
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(4)
            turn_right(90)
            move_forward(4)
            turn_right(90)
            move_forward(8)
        else:
            move_forward(6)
            turn_right(90)
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(2)
            turn_right(90)
            move_forward(4) 
            
    else: # objeto J não existe
        print("Não existe J")
        move_forward(5000)
        turn_left(90)
        move_forward(1000)
    
    if has_obstacle(): #Objeto "H":
        turn_right(90)
        move_forward(2)
        turn_left(90)
        move_forward(2)
        # Abre e retorna
        move_backward(2)
        turn_left(90)
        move_forward(6)
        
    else: #Objeto "H" não existe
        print("Não existe H")
        while not is_red_left() and not is_red_right():
            andar_reto(50)
        break_motors()
        
        print("Achou vermelho")
        cor_vista = "VERMELHO"
        ajust_color()
        
        move_backward(500)
        
        turn_right(90)
        move_forward(1500)
        
        Open()
        
        #retorna para a área de coleta
        move_backward(1500)
        turn_right(90)
        move_forward(2500)
        turn_right(90)
        
        # No futuro, tentar ver a mudança do J
        while not is_blue():
            andar_reto(50)
        break_motors()
        
                
def tube_drugstore():
    
    crono.reset()
    branco = 100 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 4000:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    break_motors()
    turn_left(90)
    
    if has_obstacle(): #Objeto "J":
        turn_right(90)
        move_forward(4)
        turn_left(90)
        move_forward(4)
        turn_left(90)
        
        if has_obstacle(): #Objeto "G":
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(2)
            turn_left(90)
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_left(90)
            move_forward(3)
            turn_right(90)
            move_forward(8)
        else:    
            move_forward(2)
            turn_right(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(3)
            turn_right(90)
            move_forward(4)
    else:
        move_forward(4) # Mesmo valor do museum
        turn_right(90)
    
    if has_obstacle(): #Objeto "G":
        turn_left(90)
        if has_obstacle(): #Objeto "E":
            move_backward(5)
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(9)
            turn_left(90)
            move_forward(3)
            turn_left(90)
            move_forward(2)
            #Abre e solta
            move_backward(2)
            turn_left(90)
            move_forward(3)
            turn_right(90)
            move_forward(9) 
        else:
            move_forward(4)
            turn_right(90)
            move_forward(2)
            turn_right(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(3)
            turn_left(90)
            move_forward(8)
    else:
        move_forward(2000)
        turn_left(90)
        move_forward(1000)
        
        
        Open() #Entregou
        
        move_backward(1000)
        turn_left(90)
        move_forward(2000)
        turn_left(90)
        
        # Voltando para área de coleta
        while not is_blue():
            andar_reto(50)
        break_motors()
        
def tube_bakery():
    crono.reset()
    branco = 100 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 10000:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    break_motors()
    turn_left(90)
    move_forward(1000)
    
    if has_obstacle(): #Objeto "I":
        turn_left(90)
        move_forward(5)
        turn_right(90)
        move_forward(4)
        if has_obstacle(): #objeto "E":
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(2)
            turn_right(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(3)
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(4)
        else:
            move_forward(4)
            turn_right(90)
        
        if has_obstacle(): #OBJETO B"
            turn_right(90)
            move_forward(5)
            turn_left(90)
            move_forward(4)
            turn_left(90)
            move_forward(2)
            turn_right(90)
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(3)
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(4)
        else:
            move_forward(4)
        if has_obstacle(): #objeto "A":
            turn_right(90)
            move_forward(3)
            turn_left(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(2)
            turn_right(90)
            move_forward(5)
            turn_left(90)
            move_forward(4)
        else:
            move_forward(2)
            turn_right(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(6)
            turn_left(90)
            move_forward(8)
    else:
        move_forward(3000)
    
    if has_obstacle(): #Objeto "D":
        turn_left(90)
        move_forward(1)
        if has_obstacle(): #Objeto "G":
            turn_left(90)
            move_forward(4)
            turn_right(90)
            move_forward(4)
            turn_right(90)
            move_forward(8)
            
        
        if has_obstacle(): #objeto "A":
            move_back()
            turn_right(90)
            move_forward()
            turn_left(90)
            move_forward()
            #Abre e retorna
        
        move_backward()
        turn_right(90)
        move_forward()
        turn_left(90)
        move_forward()        
        #Abre e retorna
    else:
        
        move_forward(1000)
        turn_right(90)
        move_forward(1000)
        
        
        Open() #Entregou
        
        move_backward(1000)
        turn_right(90)
        
        while not is_blue():
            andar_reto(50)
        break_motors()
        
    
def tube_park():
    move_forward(3500)
    turn_left(90)
    if has_obstacle(): #objeto "J":
        turn_right(90)
        move_forward(4)
        turn_left(90)
        move_forward(4)
        if has_obstacle(): #objeto "D":
            turn_left(90)
            move_forward(4)
            turn_right(90)
            move_forward(4)
            turn_right(90)
            if has_obstacle(): #objeto "B":
                turn_180()
                move_forward(2)
                turn_right(90)
                move_forward(2)
                #Abre e retorna
                move_backward(2)
                turn_right(90)
                move_forward(4)
                turn_right(90)
                move_forward(4)
                turn_left(90)
                move_forward(4)
                turn_right(90)
                move_forward(2)
            else:
                move_forward(4)
                turn_left(90)
                move_forward(2)
                #Abre e retorna
        else:
            move_forward(4)
            turn_right(90)
            if has_obstacle(): #objeto "A":
                turn_180()
                move_forward(2)
                turn_right(90)
                move_forward(2)
                #Abre e retorna
            else:
                move_forward(2)
                turn_left(90)
                move_forward(2)
                #Abre e retorna
    else:
        move_forward(4750)
        if has_obstacle(): #objeto "E":
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(4)
            turn_right(90)
            if has_obstacle(): #objeto "A":
                turn_180()
                move_forward(2)
                turn_right(90)
                move_forward(2)
                #Abre e retorna
            else:
                move_forward(2)
                turn_left(90)
                move_forward(2)
                #Abre e retorna
        else:
            move_forward(7000)
            turn_right(90)
            if has_obstacle(): #objeto "B":
                turn_180()
                move_forward(2)
                turn_right(90)
                move_forward(2)
                #Abre e retorna
            else:
                move_forward(3500)
                turn_left(90)
                move_forward(1750)
                #Abre e retorna
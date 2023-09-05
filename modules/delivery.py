from modules.motors import *
from modules.beeps import *
from modules.claw import *

from pybricks.tools import StopWatch

crono = StopWatch()

has_object_in = []

def go_to_check_point():
    turn_right_pid(90)
    move_backward(1200)
    turn_left_pid(90)

def tube_library():
    global has_object_in
    crono.reset()
    branco = 88 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 1400: # Tenho que olhar isso
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)
    brake_motors()
    
    move_backward(800)
    turn_left_pid(90)
    move_forward(2000) # Indo para a entrega
    Open()
    move_backward(2000) # Volta para a área de coleta a msm distância de ir
    
    turn_left_pid(180)
    
    while not is_blue():
        andar_reto(360)
    brake_motors()
    
        
    
def tube_city_hall():
    global has_object_in
    crono.reset()
    branco = 88 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 3600: # Tenho que olhar isso
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors()
    turn_left_pid(90)
    move_forward(1000) # Está indo em direção ao objeto J
    
    if has_obstacle(): #sensor identificou objeto "J":
        turn_right_pid(180)
        while not is_blue():
            andar_reto(360)
        brake_motors()
        while is_blue():
            andar_reto(-360)
        brake_motors()
        turn_left_pid(90)
        branco = 88 
        azul = 14 #22
        threshold = (branco + azul) / 2  # = 40
        vel = 100
        crono.reset()
        while crono.time() < 6000: # Tenho que olhar isso
            delta = red_right() - threshold
            kp = 0.5
            erro = delta * kp
            motors.drive(vel, erro)
            
        turn_left_pid(90)
        move_forward(3500)
        turn_left_pid(90)
        move_forward(2000)
        Open()
        #retorna para a área de coleta
        move_backward(2000)
        turn_left_pid(90)
        while not is_blue():
            andar_reto(360)
        brake_motors()
    
    else:
        #objeto J não existe
        move_forward(2500)#Distancia pequena 3500
        turn_right_pid(90)
        
        #tentativa de se alinhar
        while not is_yellow_left() and not is_yellow_right():
            andar_reto(360)
        brake_motors()
        
        move_forward(1000)
        Open()
        #retorna para a área de coleta
        move_backward(1500)
        turn_right_pid(90)
        
        while not is_blue():
            andar_reto(360)
        brake_motors()
        

    
def tube_school():
    
    crono.reset()
    branco = 88
    azul = 14 #22 
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 9500:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors()
    turn_left_pid(90)
    move_forward(1000)
    
    if has_obstacle(): #sensor identificou objeto "i":
        move_backward(1000)
        turn_left_pid(180)
        while not is_blue():
            andar_reto(360)
        brake_motors()
        
        
        while is_blue():
            andar_reto(-360)
        brake_motors()
        turn_right_pid(90)
        branco = 80
        azul = 10
        threshold = (branco + azul) / 2  # = 40
        vel = 100
        crono.reset()
        
        
        while crono.time() < 6000:
            delta = threshold - red_left()
            kp = 0.8
            erro = delta * kp
            motors.drive(vel, erro)
        turn_right_pid(90)
        #De frente para o J
        move_forward(6000)
        
        #G
        turn_right_pid(90)
        move_forward(1000)
        if has_obstacle(): #Objeto "G":
            move_backward(1000)
            turn_left_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(360)
            cor_vista = "PAREDE"
            brake_motors()
            ajust_color(cor_vista)
            move_backward(100)
            turn_right_pid(90)
            
            
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "VERMELHO"
            ajust_color(cor_vista)
            print("Bati no vermelho")
            move_backward(2800)
            turn_right_pid(90)
            move_forward(4900)
            turn_left_pid(90)
            
            
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "VERMELHO"
            ajust_color(cor_vista)
            print("Bati no vermelho 2")
            
            move_backward(700)
            turn_right_pid(90)
            move_forward(1500)
            Open()
            move_backward(1500)
            turn_right_pid(90)
            
            #começa caminho de volta
            
            move_forward(3000)
            turn_right_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "PAREDE"
            ajust_color(cor_vista)
            move_backward(1000)
            turn_left_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "VERMELHO"
            ajust_color(cor_vista)
            print("Bati no vermelho")
            move_backward(3500)
            turn_left_pid(90)
            while not is_blue():
                andar_reto(540)
        else:
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "VERMELHO"
            ajust_color(cor_vista)
            print("Bati no vermelho")
            move_backward(500)
            turn_right_pid(90)
            move_forward(1500)
            #abre e retorna
            Open()
            move_backward(1500)
            turn_right_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "VERMELHO"
            ajust_color(cor_vista)
            move_backward(3500)
            turn_left_pid(90)
            while not is_blue():
                andar_reto(540)
            brake_motors()
    else:
        move_forward(2500)#Distancia pequena 3500
        turn_right_pid(90)
        
        #tentativa de se alinhar
        while not is_yellow_left() and not is_yellow_right():
            andar_reto(360)
        brake_motors()
        
        move_forward(1000)
        Open()
        #retorna para a área de coleta
        move_backward(1500)
        turn_right_pid(90)
        
        while not is_blue():
            andar_reto(360)
        brake_motors()
        
def tube_museum():
    
    crono.reset()
    branco = 88 
    azul = 14 #22
    threshold = (branco + azul) / 2  
    vel = 100
    while crono.time() < 3600: #4000
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors()
    turn_left_pid(90)
    move_forward(1000) # Está indo em direção ao objeto J
    
    if has_obstacle(): #sensor identificou objeto "j":
        move_backward(1000)
        turn_right_pid(180)
        while not is_blue():
            andar_reto(360)
        brake_motors()
        while is_blue():
            andar_reto(-360)
        turn_left_pid(90)
        branco = 88 
        azul = 14 #22
        threshold = (branco + azul) / 2  # = 40
        vel = 100
        crono.reset()
        while crono.time() < 6500: 
            delta = red_right() - threshold
            kp = 0.5
            erro = delta * kp
            motors.drive(vel, erro)
            
        turn_left_pid(90)
        move_forward(6000)
        turn_left_pid(90)
        move_forward(1000)
        if has_obstacle(): #sensor identificou objeto G:
            move_backward(1000)
            turn_right_pid(90)
            while not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "PAREDE"
            ajust_color(cor_vista)
            turn_left_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "VERMELHO"
            ajust_color(cor_vista)
            print("Bati no vermelho")
            move_backward(3500)
            turn_left_pid(90)
            move_forward(4000)
            turn_right_pid(90)
            move_forward(1500)
            #abre e retorna
            Open()
            move_backward(1500)
            turn_right_pid(90)
            while not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "PAREDE"
            ajust_color(cor_vista)
            turn_right_pid(90)
            move_forward(6000)
            turn_right_pid(90)
            while not is_blue():
                andar_reto(540)
            brake_motors()
        else:
            move_forward(6000)
            if has_obstacle(): #sensor identificou objeto H:
                turn_right_pid(90)
                move_forward(2000)
                turn_left_pid(90)
                move_forward(1500)
                #abre e retorna
                Open()
                move_backward(1500)
                turn_left_pid(90)
                move_forward(2000)
                turn_left_pid(90)
                move_forward(6000)
                turn_right_pid(90)
                while not is_blue():
                    andar_reto(540)
                brake_motors()
            else:
                while not is_red_left() and not is_red_right():
                    andar_reto(360)
                brake_motors()
                cor_vista = "VERMELHO"
                ajust_color(cor_vista)
                print("Bati no vermelho")
                move_backward(500)
                turn_right_pid(90)
                move_forward(1500)
                #abre e retorna
                Open()
                move_backward(1500)
                turn_right_pid(90)
                move_forward(8000)
                turn_right_pid(90)
                while not is_blue():
                    andar_reto(540)
                brake_motors()
                
    else: # objeto J não existe
        print("Não existe J")
        move_forward(6000)
        turn_left_pid(90)
        move_forward(800)
    
        if has_obstacle(): #Objeto "H":
            move_backward(1000)
            turn_right_pid(90)
            move_forward(2000)
            turn_left_pid(90)
            move_forward(1500)
            #abre e retorna
            Open()
            move_backward(1500)
            turn_left_pid(90)
            while not is_blue():
                andar_reto(540)
            brake_motors()
            
        else: #Objeto "H" não existe
            print("Não existe H")
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            
            print("Achou vermelho")
            cor_vista = "VERMELHO"
            ajust_color(cor_vista)
            
            move_backward(700)
            
            turn_right_pid(90)
            move_forward(1700)
            
            Open()
            
            #retorna para a área de coleta
            move_backward(1700)
            turn_right_pid(90)
            move_forward(3000)
            turn_right_pid(90)
            while not is_blue():
                andar_reto(360)
            brake_motors()
        
                
def tube_drugstore():
    
    crono.reset()
    branco = 88 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 3600: #3250
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors()
    turn_left_pid(90)
    move_forward(1000)
    
    if has_obstacle(): #Objeto "J":
        turn_right_pid(180)
        while not is_blue():
            andar_reto(360)
        brake_motors()
        
        while is_blue():
            andar_reto(-360)
        brake_motors()
        turn_left_pid(90)
        
        branco = 88 
        azul = 14 #22
        threshold = (branco + azul) / 2  
        vel = 100
        crono.reset()
        while crono.time() < 6500: 
            delta = red_right() - threshold
            kp = 0.5
            erro = delta * kp
            motors.drive(vel, erro)
        brake_motors()
        turn_left_pid(90)
        move_forward(6200)
        turn_left_pid(90)
        move_forward(500)
        
        if has_obstacle(): #Objeto "G":
            move_backward(500)
            turn_right_pid(90)
            
            while not is_black_left() or not is_black_right():
                andar_reto(360)
            brake_motors()
            
            
            cor_vista = "PRETO"
            ajust_color(cor_vista)
            
            move_backward(500)
            
            turn_left_pid(90)
            move_forward(2400)
            turn_left_pid(90)
            move_forward(2200)
            
            Open()
            
            move_backward(2200)
            turn_left_pid(90)
            
            move_forward(2200)
            turn_right_pid(90)
            
            while not is_blue():
                andar_reto(360)
            brake_motors()
    
        else:    
            move_forward(275)
            turn_right_pid(90)
            move_forward(1500)
            
            Open()
            
            move_backward(1500)
            turn_right_pid(90)
            move_forward(2750)
            turn_right_pid(90)
            while not is_blue():
                andar_reto(360)
            brake_motors()
    else:
        move_forward(5700) # Mesmo valor do museum
        turn_right_pid(90)
    
        if has_obstacle(): #Objeto "G":
            turn_left_pid(90)
            if has_obstacle(): #Objeto "E":
                move_backward(5)
                turn_right_pid(90)
                move_forward(4)
                turn_left_pid(90)
                move_forward(9)
                turn_left_pid(90)
                move_forward(3)
                turn_left_pid(90)
                move_forward(2)
                #Abre e solta
                move_backward(2)
                turn_left_pid(90)
                move_forward(3)
                turn_right_pid(90)
                move_forward(9) 
            else:
                move_forward(4)
                turn_right_pid(90)
                move_forward(2)
                turn_right_pid(90)
                move_forward(2)
                #Abre e retorna
                move_backward(2)
                turn_right_pid(90)
                move_forward(3)
                turn_left_pid(90)
                move_forward(8)
        else:
            move_forward(2800)
            turn_left_pid(90)
            move_forward(1700)
            
            
            Open() #Entregou
            
            move_backward(1700)
            turn_left_pid(90)
            move_forward(2000)
            turn_left_pid(90)
            
            # Voltando para área de coleta
            while not is_blue():
                andar_reto(360)
            brake_motors()
        
def tube_bakery():
    crono.reset()
    branco = 88 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 9800:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors()
    turn_left_pid(90)
    move_forward(1000)
    
    if has_obstacle(): #Objeto "I":
        turn_left_pid(90)
        move_forward(5)
        turn_right_pid(90)
        move_forward(4)
        if has_obstacle(): #objeto "E":
            turn_right_pid(90)
            move_forward(4)
            turn_left_pid(90)
            move_forward(2)
            turn_right_pid(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right_pid(90)
            move_forward(3)
            turn_right_pid(90)
            move_forward(4)
            turn_left_pid(90)
            move_forward(4)
        else:
            move_forward(4)
            turn_right_pid(90)
        
        if has_obstacle(): #OBJETO B"
            turn_right_pid(90)
            move_forward(5)
            turn_left_pid(90)
            move_forward(4)
            turn_left_pid(90)
            move_forward(2)
            turn_right_pid(90)
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_right_pid(90)
            move_forward(3)
            turn_right_pid(90)
            move_forward(4)
            turn_left_pid(90)
            move_forward(4)
        else:
            move_forward(4)
        if has_obstacle(): #objeto "A":
            turn_right_pid(90)
            move_forward(3)
            turn_left_pid(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right_pid(90)
            move_forward(2)
            turn_right_pid(90)
            move_forward(5)
            turn_left_pid(90)
            move_forward(4)
        else:
            move_forward(2)
            turn_right_pid(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right_pid(90)
            move_forward(6)
            turn_left_pid(90)
            move_forward(8)
    else:
        move_forward(8700)
    
    if has_obstacle(): #Objeto "D":
        turn_left_pid(90)
        move_forward(1)
        if has_obstacle(): #Objeto "G":
            turn_left_pid(90)
            move_forward(4)
            turn_right_pid(90)
            move_forward(4)
            turn_right_pid(90)
            move_forward(8)
            
        
        if has_obstacle(): #objeto "A":
            move_back()
            turn_right_pid(90)
            move_forward()
            turn_left_pid(90)
            move_forward()
            #Abre e retorna
        
        move_backward()
        turn_right_pid(90)
        move_forward()
        turn_left_pid(90)
        move_forward()        
        #Abre e retorna
    else:
        turn_right_pid(90)
        move_forward(2500)
        
        
        Open() #Entregou
        
        move_backward(2500)
        turn_right_pid(90)
        
        while not is_blue():
            andar_reto(360)
        brake_motors()
        
    
def tube_park():
    crono.reset()
    branco = 88 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 3600: #3250
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors()
    turn_left_pid(90)
    move_forward(1000)
    
    if has_obstacle(): #objeto "J":
        turn_right_pid(90)
        move_forward(4)
        turn_left_pid(90)
        move_forward(4)
        if has_obstacle(): #objeto "D":
            turn_left_pid(90)
            move_forward(4)
            turn_right_pid(90)
            move_forward(4)
            turn_right_pid(90)
            if has_obstacle(): #objeto "B":
                turn_180()
                move_forward(2)
                turn_right_pid(90)
                move_forward(2)
                #Abre e retorna
                move_backward(2)
                turn_right_pid(90)
                move_forward(4)
                turn_right_pid(90)
                move_forward(4)
                turn_left_pid(90)
                move_forward(4)
                turn_right_pid(90)
                move_forward(2)
            else:
                move_forward(4)
                turn_left_pid(90)
                move_forward(2)
                #Abre e retorna
        else:
            move_forward(4)
            turn_right_pid(90)
            if has_obstacle(): #objeto "A":
                turn_180()
                move_forward(2)
                turn_right_pid(90)
                move_forward(2)
                #Abre e retorna
            else:
                move_forward(2)
                turn_left_pid(90)
                move_forward(2)
                #Abre e retorna
    else:
        not_found_wall()
        move_forward(5050)
        
        if has_obstacle(): #objeto "E":
            turn_right_pid(90)
            move_forward(4)
            turn_left_pid(90)
            move_forward(4)
            turn_right_pid(90)
            if has_obstacle(): #objeto "A":
                turn_180()
                move_forward(2)
                turn_right_pid(90)
                move_forward(2)
                #Abre e retorna
            else:
                move_forward(2)
                turn_left_pid(90)
                move_forward(2)
                #Abre e retorna
        else:
            not_found_wall()
            while not is_black_left() and not is_black_right():
                andar_reto(360)
                
            brake_motors()
            cor_vista = "PAREDE"
            ajust_color(cor_vista)
            move_backward(700)
            turn_right_pid(90)
            if has_obstacle(): #objeto "B":
                turn_180()
                move_forward(2)
                turn_right_pid(90)
                move_forward(2)
                #Abre e retorna
            else:
                move_forward(1500)
                turn_left_pid(90)
                move_forward(1750)
                Open()
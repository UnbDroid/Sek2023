from modules.motors import *
from modules.beeps import *
from modules.claw import *
from modules.path import *

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
    
    if has_obstacle() or "J" in has_object_in: #sensor identificou objeto "J":
        has_object_in.append("J")
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
    global has_object_in
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
    
    if has_obstacle() or "I" in has_object_in: #sensor identificou objeto "i":
        has_object_in.append("I")
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
        if has_obstacle() or "G" in has_object_in: #Objeto "G":
            has_object_in.append("G")
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
            find_blue_line(0)
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
        find_blue_line(0)
        
def tube_museum():
    global has_object_in
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
    
    if has_obstacle() or "J" in has_object_in: #sensor identificou objeto "j":
        has_object_in.append("J")
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
        if has_obstacle() or "G" in has_object_in: #sensor identificou objeto G:
            has_object_in.append("G")
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
            find_blue_line(0)
        else:
            move_forward(6000)
            if has_obstacle() or "H" in has_object_in: #sensor identificou objeto H:
                has_object_in.append("H")
                turn_right_pid(90)
                move_forward(2000)
                turn_left_pid(90)
                move_forward(1500)
                #abre e retorna
                Open()
                find_blue_line(0)
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
                find_blue_line(0)
                
    else: # objeto J não existe
        print("Não existe J")
        move_forward(6000)
        turn_left_pid(90)
        move_forward(800)
    
        if has_obstacle() or "H" in has_object_in: #Objeto "H":
            has_object_in.append("H")
            move_backward(1000)
            turn_right_pid(90)
            move_forward(2000)
            turn_left_pid(90)
            move_forward(1500)
            #abre e retorna
            Open()
            find_blue_line(0)
            
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
            
            find_blue_line(0)
        
                
def tube_drugstore():
    global has_object_in
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
    
    if has_obstacle() or "J" in has_object_in: #Objeto "J":
        has_object_in.append("J")
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
        
        if has_obstacle() or "G" in has_object_in: #Objeto "G":
            has_object_in.append("G")
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
            
            find_blue_line(0)
    
        else:    
            move_forward(275)
            turn_right_pid(90)
            move_forward(1500)
            
            Open()
            
            find_blue_line(0)
    else:
        move_forward(5700) # Mesmo valor do museum
        turn_right_pid(90)
    
        if has_obstacle() or "G" in has_object_in: #Objeto "G":
            has_object_in.append("G")
            turn_left_pid(90)
            if has_obstacle() or "E" in has_object_in: #Objeto "E":
                has_object_in.append("E")
                move_backward(5)
                turn_right_pid(90)
                move_forward(4)
                turn_left_pid(90)
                move_forward(9)
                turn_left_pid(90)
                move_forward(3)
                turn_left_pid(90)
                move_forward(2)
                Open()
                #Abre e solta
                find_blue_line(0) 
            else:
                move_forward(4)
                turn_right_pid(90)
                move_forward(2)
                turn_right_pid(90)
                move_forward(2)
                Open()
                #Abre e retorna
                find_blue_line(0)
        else:
            move_forward(2800)
            turn_left_pid(90)
            move_forward(1700)
            
            
            Open() #Entregou
            
            find_blue_line(0)
        
def tube_bakery():
    global has_object_in
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
    
    if has_obstacle() or "I" in has_object_in: #Objeto "I":
        has_object_in.append("I")
        turn_left_pid(90)
        move_forward(5)
        turn_right_pid(90)
        move_forward(4)
        if has_obstacle() or "E" in has_object_in: #objeto "E":
            has_object_in.append("E")
            turn_right_pid(90)
            move_forward(4)
            turn_left_pid(90)
            move_forward(2)
            turn_right_pid(90)
            move_forward(2)
            Open()
            #Abre e retorna
            find_blue_line(0)
        else:
            move_forward(4)
            turn_right_pid(90)
        
        if has_obstacle() or "B" in has_object_in: #OBJETO B"
            has_object_in.append("B")   
            turn_right_pid(90)
            move_forward(5)
            turn_left_pid(90)
            move_forward(4)
            turn_left_pid(90)
            move_forward(2)
            turn_right_pid(90)
            move_forward(2)
            Open()
            #abre e retorna
            find_blue_line(0)
        else:
            move_forward(4)
        if has_obstacle() or "A" in has_object_in: #objeto "A":
            has_object_in.append("A")
            turn_right_pid(90)
            move_forward(3)
            turn_left_pid(90)
            move_forward(2)
            Open()
            #Abre e retorna
            find_blue_line(0)
        else:
            move_forward(2)
            turn_right_pid(90)
            move_forward(2)
            Open()
            #Abre e retorna
            find_blue_line(0)
    else:
        move_forward(8700)
    
    if has_obstacle() or "D" in has_object_in: #Objeto "D":
        has_object_in.append("D")
        turn_left_pid(90)
        move_forward(1)
        if has_obstacle() or "G" in has_object_in: #Objeto "G":
            has_object_in.append("G")
            turn_left_pid(90)
            move_forward(4)
            turn_right_pid(90)
            move_forward(4)
            turn_right_pid(90)
            move_forward(8)
            
        
        if has_obstacle() or "A" in has_object_in: #objeto "A":
            has_object_in.append("A")
            move_back()
            turn_right_pid(90)
            move_forward()
            turn_left_pid(90)
            move_forward()
            Open()
            #Abre e retorna
            find_blue_line(0)
        
        move_backward()
        turn_right_pid(90)
        move_forward()
        turn_left_pid(90)
        move_forward()
        Open() 
        #Abre e retorna
        find_blue_line(0)
    else:
        turn_right_pid(90)
        move_forward(2500)
        
        
        Open() #Entregou
        
        find_blue_line(0)
        
    
def tube_park():
    global has_object_in
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
    
    if has_obstacle() or "J" in has_object_in: #objeto "J":
        has_object_in.append("J")
        turn_right_pid(90)
        move_forward(4)
        turn_left_pid(90)
        move_forward(4)
        if has_obstacle() or "D" in has_object_in: #objeto "D":
            has_object_in.append("D")
            turn_left_pid(90)
            move_forward(4)
            turn_right_pid(90)
            move_forward(4)
            turn_right_pid(90)
            if has_obstacle() or "B" in has_object_in: #objeto "B":
                has_object_in.append("B")
                turn_180()
                move_forward(2)
                turn_right_pid(90)
                move_forward(2)
                Open()
                #Abre e retorna
                find_blue_line(0)
            else:
                move_forward(4)
                turn_left_pid(90)
                move_forward(2)
                Open()
                #Abre e retorna
                find_blue_line(0)
        else:
            move_forward(4)
            turn_right_pid(90)
            if has_obstacle() or "A" in has_object_in: #objeto "A":
                has_object_in.append("A")
                turn_180()
                move_forward(2)
                turn_right_pid(90)
                move_forward(2)
                Open()
                #Abre e retorna
                find_blue_line(0)
            else:
                move_forward(2)
                turn_left_pid(90)
                move_forward(2)
                Open()
                #Abre e retorna
                find_blue_line(0)
    else:
        not_found_wall()
        move_forward(5050)
        
        if has_obstacle() or "E" in has_object_in: #objeto "E":
            has_object_in.append("E")
            turn_right_pid(90)
            move_forward(4)
            turn_left_pid(90)
            move_forward(4)
            turn_right_pid(90)
            if has_obstacle() or "A" in has_object_in: #objeto "A":
                has_object_in.append("A")
                turn_180()
                move_forward(2)
                turn_right_pid(90)
                move_forward(2)
                Open()
                #Abre e retorna
                find_blue_line(0)
            else:
                move_forward(2)
                turn_left_pid(90)
                move_forward(2)
                Open()
                #Abre e retorna
                find_blue_line(0)
        else:
            not_found_wall()
            while not is_black_left() and not is_black_right():
                andar_reto(360)
                
            brake_motors()
            cor_vista = "PAREDE"
            ajust_color(cor_vista)
            move_backward(700)
            turn_right_pid(90)
            if has_obstacle() or "B" in has_object_in: #objeto "B":
                has_object_in.append("B")
                turn_180()
                move_forward(2)
                turn_right_pid(90)
                move_forward(2)
                Open()
                #Abre e retorna
                find_blue_line(0)
            else:
                move_forward(1800)
                turn_left_pid(90)
                move_forward(1750)
                Open()
                find_blue_line(0)
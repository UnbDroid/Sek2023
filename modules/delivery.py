from modules.motors import *
from modules.beeps import *
from modules.claw import *
from modules.variables import *
from modules.path import *
from pybricks.tools import StopWatch

crono = StopWatch()


def go_to_check_point():
    turn_right_pid(90)
    wait(250)
    move_backward(13)
    wait(250)
    turn_left_pid(90)
    wait(250)

def tube_library():
    #global has_object_in
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
    
    move_backward(6)
    turn_left_pid(90)
    move_forward(32) # Indo para a entrega
    Open()
    move_backward(32) # Volta para a área de coleta a msm distância de ir
    
    turn_left_pid(90)
    move_backward(13)
    turn_left_pid(90)
        
    
def tube_city_hall():
    #global has_object_in
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
    move_forward(18) # Está indo em direção ao objeto J
    
    if has_obstacle() :# or "J" in has_object_in 
        # #has_object_in.append("J")
        turn_180()
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
        brake_motors()
        
        
        turn_left_pid(90)
        move_forward(38)
        turn_left_pid(90)
        wait(250)
        move_forward(20)
        Open()
        #retorna para a área de coleta
        move_backward(20)
        turn_left_pid(90)
        while not is_blue():
            andar_reto(360)
        brake_motors()
    
    else:
        #objeto J não existe
        not_found_wall()
        move_forward(17)
        turn_right_pid(90)
        
        move_forward(20)
        Open()
        #retorna para a área de coleta
        move_backward(20)
        turn_right_pid(90)
        
        while not is_blue():
            andar_reto(360)
        brake_motors()
        

    
def tube_school():
    ##global has_object_in
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
    move_forward(18)
    
    if has_obstacle():
        found_wall()
        turn_180()
        while not is_blue():
            andar_reto(360)
        brake_motors()
        
        while is_blue():
            andar_reto(-360)
        brake_motors()
        turn_right_pid(90)
        
        
    
        branco = 90
        azul = 13
        threshold = (branco + azul) / 2  
        vel = 100
        crono.reset()
        while crono.time() < 6000:
            delta = threshold - red_left()
            kp = 0.5 #(0.8)
            erro = delta * kp
            motors.drive(vel, erro)
            
        brake_motors()
        turn_right_pid(90)
        move_forward(66)
        turn_right_pid(90)
        #G
        move_forward(15)
        
        if has_obstacle(): 
            move_backward(1000)
            turn_left_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(360)
            cor_vista = "BLACK"
            brake_motors()
            ajust_color(cor_vista)
            move_backward(100)
            turn_right_pid(90)
            
            
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            print("Bati no RED")
            move_backward(28)
            turn_right_pid(90)
            move_forward(49)
            turn_left_pid(90)
            
            
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            print("Bati no RED 2")
            
            move_backward(7)
            turn_right_pid(90)
            move_forward(15)
            Open()
            move_backward(15)
            turn_right_pid(90)
            
            #começa caminho de volta
            
            move_forward(30)
            turn_right_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(10)
            turn_left_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            print("Bati no RED")
            move_backward(35)
            turn_left_pid(90)
            while not is_blue():
                andar_reto(360)
            brake_motors()
        else:
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            print("Bati no RED")
            move_backward(6)
            turn_right_pid(90)
            move_forward(15)
            #abre e retorna
            Open()
            move_backward(15)
            turn_right_pid(90)
            find_blue_line(0)
    else:
        not_found_wall()
        move_forward(18)
        turn_right_pid(90)
        
        move_forward(20)
        Open()
        move_backward(20)
        turn_right_pid(90)
        
        while not is_blue():
            andar_reto(360)
        brake_motors()
        
def tube_museum():
    #global has_object_in
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
    move_forward(10) # Está indo em direção ao objeto J
    
    if has_obstacle(): # "J" in has_object_in: #sensor identificou objeto "j":
        #has_object_in.append("J")
        move_backward(10)
        turn_180()
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
        brake_motors()
        turn_left_pid(90)
        move_forward(65)
        turn_left_pid(90)
        move_forward(10)
        if has_obstacle(): # "G" in has_object_in: #sensor identificou objeto G:
            #has_object_in.append("G")
            move_backward(10)
            turn_right_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(7)
            turn_left_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            print("Bati no RED")
            move_backward(35)
            turn_left_pid(90)
            move_forward(32.5)
            turn_right_pid(90)
            move_forward(15)
            #abre e retorna
            Open()
            move_backward(15)
            turn_right_pid(90)
            find_blue_line()
        else:
            move_forward(60)
            if has_obstacle(): # "H" in has_object_in: #sensor identificou objeto H:
                #has_object_in.append("H")
                move_backward(10)
                turn_right_pid(90)
                move_forward(30)
                turn_left_pid(90)
                move_forward(15)
                #abre e retorna
                Open()
                move_backward(15)
                turn_right_pid(90)
                find_blue_line()
            else:
                while not is_red_left() and not is_red_right():
                    andar_reto(360)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(5)
                turn_right_pid(90)
                move_forward(15)
                #abre e retorna
                Open()
                move_backward(15)
                turn_right_pid(90)
                find_blue_line()
                
    else: # objeto J não existe
        print("Não existe J")
        move_forward(60)
        turn_left_pid(90)
        move_forward(8)
    
        if has_obstacle(): # "H" in has_object_in: #Objeto "H":
            #has_object_in.append("H")
            move_backward(10)
            turn_right_pid(90)
            move_forward(20)
            turn_left_pid(90)
            move_forward(15)
            #abre e retorna
            Open()
            move_backward(15)
            turn_right_pid(90)
            find_blue_line()
            
        else: #Objeto "H" não existe
            print("Não existe H")
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            
            print("Achou RED")
            cor_vista = "RED"
            ajust_color(cor_vista)
            
            move_backward(7)
            
            turn_right_pid(90)
            move_forward(17)
            
            Open()
            move_backward(17)
            turn_right_pid(90)
            find_blue_line()
        
                
def tube_drugstore():
    #global has_object_in
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
    move_forward(10)
    
    if has_obstacle(): # "J" in has_object_in: #Objeto "J":
        #has_object_in.append("J")
        turn_180()
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
        move_forward(62)
        turn_left_pid(90)
        move_forward(5)
        
        if has_obstacle(): # "G" in has_object_in: #Objeto "G":
            #has_object_in.append("G")
            move_backward(5)
            turn_right_pid(90)
            
            while not is_black_left() or not is_black_right():
                andar_reto(360)
            brake_motors()
            
            
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            
            move_backward(5)
            
            turn_left_pid(90)
            move_forward(24)
            turn_left_pid(90)
            move_forward(22)
            
            Open()
            move_backward(22)
            turn_right_pid(90)
            
            find_blue_line()
    
        else:    
            move_forward(27.5)
            turn_right_pid(90)
            move_forward(15)
            
            Open()
            move_backward(10)
            turn_right_pid(90)
            find_blue_line()
    else:
        move_forward(57) # Mesmo valor do museum
        turn_right_pid(90)
    
        if has_obstacle(): # "G" in has_object_in: #Objeto "G":
            #has_object_in.append("G")
            turn_left_pid(90)
            if has_obstacle(): # "E" in has_object_in: #Objeto "E":
                #has_object_in.append("E")
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
                move_backward(1500)
                turn_right_pid(90)
                find_blue_line() 
            else:
                move_forward(4)
                turn_right_pid(90)
                move_forward(2)
                turn_right_pid(90)
                move_forward(2)
                Open()
                move_backward(15)
                turn_right_pid(90)
                #Abre e retorna
                find_blue_line()
        else:
            move_forward(28)
            turn_left_pid(90)
            move_forward(17)
            
            Open() #Entregou
            move_backward(17)
            turn_right_pid(90)
            find_blue_line()
        
def tube_bakery():
    #global has_object_in
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
    move_forward(10)
    
    if has_obstacle(): # "I" in has_object_in: #Objeto "I":
        #has_object_in.append("I")
        move_backward(10)
        turn_180()
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
        brake_motors()
        turn_right_pid(90)
        #De frente para o J
        move_forward(70)
        turn_right_pid(90)
        move_forward(10)
        if has_obstacle(): # "G" in has_object_in: #objeto "G":
            #has_object_in.append("G")
            move_backward(10)
            turn_left_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(7)
            turn_right_pid(90)
            while not is_red_left() and not is_red_right() and not has_obstacle():
                andar_reto(360)
            brake_motors()
            if is_red_left() or is_red_right():
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(7)
                turn_right_pid(90)
                move_forward(15)
                Open()
                move_backward(15)
                turn_right_pid(90)
                find_blue_line()
            else:
                #has_object_in.append("A")
                while ultrasound_sensor.distance() > 145:
                    andar_reto(360)
                brake_motors()
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-150)
                brake_motors()
                turn_right_pid(90)
                move_forward(15)
                turn_left_pid(90)
                move_forward(15)
                Open()
                move_backward(15)
                turn_right_pid(90)
                find_blue_line()
        else:
            move_forward(45)
            turn_left_pid(90)
            move_forward(10)
            if has_obstacle(): # "D" in has_object_in: 
                #has_object_in.append("D")
                move_backward(10)
                turn_left_pid(90)
                move_forward(55)
                turn_right_pid(90)
                while not is_black_left() and not is_black_right():
                    andar_reto(360)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                while not is_red_left() and not is_red_right():
                    andar_reto(360)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(7)
                turn_right_pid(90)
                move_forward(15)
                Open()
                move_backward(15)
                turn_right_pid(90)
                find_blue_line()
            else:
                move_forward(15)
                turn_right_pid(90)
                move_forward(15)
                Open()
                move_backward(15)
                turn_right_pid(90)
                #Abre e retorna
                find_blue_line()
    else:
        move_forward(55)
        if has_obstacle(): # "D" in has_object_in:
            #has_object_in.append("D")
            turn_left_pid(90)
            move_forward(10)
            if has_obstacle(): # "G" in has_object_in:
                #has_object_in.append("G")
                move_backward(10)
                turn_left_pid(90)
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
                brake_motors()
                turn_right_pid(90)
                while not is_black_left() and not is_black_right():
                    andar_reto(360)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                while not is_red_left() and not is_red_right():
                    andar_reto(360)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(7)
                turn_right_pid(90)
                move_forward(15)
                Open()
                move_backward(15)
                turn_right_pid(90)
                find_blue_line()
            else:
                move_forward(45)
                turn_right_pid(90)
                while not is_black_left() and not is_black_right():
                    andar_reto(360)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                while not is_red_left() and not is_red_right():
                    andar_reto(360)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(7)
                turn_right_pid(90)
                move_forward(15)
                Open()
                move_backward(15)
                turn_right_pid(90)
                find_blue_line()
        else:
            move_forward(30)
            turn_right_pid(90)
            move_forward(15)
            Open()
            move_backward(15)
            turn_right_pid(90)
            #Abre e retorna
            find_blue_line()
    
def tube_park():
    
    #global has_object_in
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
    move_forward(16)
    
    if has_obstacle(): # "J" in has_object_in: #objeto "J":
        print("Tem um objeto no J indo pro Park")
        #has_object_in.append("J")
        turn_180()
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
        while crono.time() < 6000: # reduzir 
            delta = red_right() - threshold
            kp = 0.5
            erro = delta * kp
            motors.drive(vel, erro)
        brake_motors()
        turn_left_pid(90)
        move_forward(64)
        
        if has_obstacle(): # "D" in has_object_in: #objeto "D":
            print("Tem objeto no D")
            #has_object_in.append("D")
            turn_left_pid(90)
            move_forward(57.5)
            turn_right_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(360)
            brake_motors()
            
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(7)
            turn_right_pid(90)
            move_forward(32.5)
            turn_left_pid(90)
            move_forward(15)
            Open()
            move_backward(15)
            turn_right_pid(90)
            find_blue_line()
        else:
            while not is_black_left() and not is_black_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            
            move_backward(7)
            turn_right_pid(90)
            move_forward(5)
            
            if has_obstacle(): # "A" in has_object_in: #objeto "A":
                #has_object_in.append("A")
                turn_180()
                move_forward(37.5)
                turn_right_pid(90)
                move_forward(15)
                Open()
                move_backward(15)
                turn_left_pid(90)
                #Abre e retorna
                find_blue_line()
            else:
                while not is_red_left() and not is_red_right():
                    andar_reto(360)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                
                move_backward(7) # possivelmente eu reduza
                turn_left_pid(90)
                move_forward(15)
                Open()
                move_backward(15)
                turn_right_pid(90)

                find_blue_line()
                
    else:
        move_forward(65)
        
        if has_obstacle(): # "E" in has_object_in: #objeto "E":
            #has_object_in.append("E")
            move_backward(4)
            turn_right_pid(90)
            move_forward(5)
            
            
            if has_obstacle(): # "G" in has_object_in: #objeto "G":
                move_backward(5)
                turn_right_pid(90)
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
                while not is_black_left() and not is_black_right():
                    andar_reto(360)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                move_forward(32.5)
                turn_left_pid(90)
                move_forward(15)
                Open()
                move_backward(15)
                turn_right_pid(90)
                find_blue_line()
                
            else:
                
                move_forward(47)
                turn_left_pid(90)
                
                while not is_black_left() and not is_black_right():
                    andar_reto(360)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                
                move_backward(7)
                turn_right_pid(90)
                move_forward(5)
                
                if has_obstacle(): # "A" in has_object_in: #objeto "A":
                    #has_object_in.append("A")
                    turn_180()
                    move_forward(32.5)
                    turn_right_pid(90)
                    move_forward(15)
                    Open()
                    move_backward(15)
                    turn_left_pid(90)
                    #Abre e retorna
                    find_blue_line()
                    
                else:
                    while not is_red_left() and not is_red_right():
                        andar_reto(360)
                    brake_motors()
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(5)
                    
                    turn_left_pid(90)
                    move_forward(15)
                    Open()
                    move_backward(15)
                    turn_right_pid(90)
                    
                    find_blue_line()
        else:
            move_forward(15)
            while not is_black_left() and not is_black_right():
                andar_reto(360)   
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(8)
            turn_right_pid(90)
            move_forward(5)
            if has_obstacle(): # "B" in has_object_in: #objeto "B":
                #has_object_in.append("B")
                move_backward(5)
                turn_180()
                move_forward(27.5)
                turn_right_pid(90)
                move_forward(15)
                Open()
                move_backward(15)
                turn_left_pid(90)
                #Abre e retorna
                find_blue_line()
            else:
                move_forward(18)
                turn_left_pid(90)
                move_forward(15.5)
                Open()
                move_backward(15.5)
                turn_right_pid(90)
                find_blue_line()
from modules.motors import *
from modules.beeps import *
from modules.claw import *
from modules.variables import *
from modules.path import *
from pybricks.tools import StopWatch

crono = StopWatch()
 
#! Mudar isso na competição :D


#! ESSA POHA AQUI #FALSE é pro ALIGN
# TO BE ladinho e TRUE para entrar

dar_pra_tras = False 

#! Localizações ----------------------------------------------------

#* Essas funções são sobre, ir do checkpoint e caminhar até o obstáculo

def go_to_i(velocidade = 150):
    branco = range_white_right()[0] 
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2 
    while left_motor.angle() < 2550 or right_motor.angle() < 2550:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(velocidade, erro)

def go_to_j(velocidade = 150):
    branco = range_white_right()[0] 
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2  
    while left_motor.angle() < 940 or right_motor.angle() < 940:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        
        motors.drive(velocidade, erro)

#* Teve obstáculo essa função faz voltar na linha azul até a área de encontro



def j_to_i(velocidade = 150):
    branco = range_white_right()[0] 
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2  
    
    while left_motor.angle() < 1588 or right_motor.angle() < 1580:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(velocidade, erro)
    
def i_to_j(velocidade = 150):
    branco = range_white_left()[0]
    azul = range_blue_left()[0]
    threshold = (branco + azul) / 2  
    
    while left_motor.angle() < 1580 or right_motor.angle() < 1588:
        delta = threshold - red_left()
        kp = 0.5
        erro = delta * kp
        motors.drive(velocidade, erro)

#* Funções para avançar até o obstáculo

def move_to_i_or_j(distancia = 19): # Colado no azul indo pro obstáculo
    brake_motors_para_drive_base()#!
    brake_motors()#!
    turn_left_pid(90)
    move_forward(distancia) 
    
def move_to_e_or_d(distancia = 62): # Colado no azul até o "D" ou o "E"
    move_forward(distancia)

def move_to_middle(distancia = 72): # Colado no azul até o meio da arena "F", "G" e "H"
    move_forward(distancia)

def i_or_j_to_middle(distancia = 53): # De frente com o I ou o J até o meio
    move_forward(distancia)
    
def middle_to_obstacle(distancia = 10): #!          No meio da arena para andar até o obstáculo
    move_forward(distancia)

#! -------------------------------------------------------------------------------------------------------


# Função recursiva para achar a linha azul (ida ou volta) ----------------------------------------

def find_blue_line(numero_de_paredes):
    esquerda_direita = ["ESQUERDA", 1]
    if numero_de_paredes < 4:
        brake_motors()
        
        cor_vista = ""
        
        print("procurando")
        while not is_meio_left() and not is_meio_right() and not is_blue_left() and not is_blue_right() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right() and not has_obstacle():
            andar_reto(500)   
            
        time_forward = [left_motor.angle(), right_motor.angle()]
        brake_motors()
        if is_red_left() or is_red_right():
            cor_vista = "RED"
        elif is_black_left() or is_black_right():
            cor_vista = "BLACK"
        elif is_yellow_left() or is_yellow_right():
            cor_vista = "YELLOW"
        if not is_blue() and not (is_red_left() or is_red_right()) and not (is_black_left() or is_black_right()) and not (is_yellow_left() or is_yellow_right()) and not has_obstacle():
            while not is_blue_left() and not is_blue_right() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right():
                andar_reto(-500)
            brake_motors()
            
        if (is_red_left() or is_red_right()):
            ajust_color(cor_vista) 
            print("Achou vermelho")
            brake_motors()
            move_backward(36)
            turn_left_pid(90)
            brake_motors()
            while not is_meio_left() and not is_meio_right() and not is_blue_left() and not is_blue_right():
                andar_reto(500)
                if (is_black_left() or is_black_right()) or (is_yellow_left() or is_yellow_right()) or is_wall():
                    brake_motors()
                    cor_vista = "BLACK"
                    ajust_color(cor_vista)
                    turn_180()
                elif has_obstacle():
                    found_wall()
                    brake_motors()
                    while ultrasound_sensor.distance() < 145:
                        andar_reto(-500)
                    while ultrasound_sensor.distance() > 145:
                        andar_reto(150)
                    brake_motors()
                    if esquerda_direita[0] == "ESQUERDA":
                        turn_left_pid(90)
                        if esquerda_direita[1] == 2:
                            esquerda_direita = ["DIREITA", 1]
                        elif esquerda_direita[1] == 1:
                            esquerda_direita[1] += 1
                    else:
                        turn_right_pid(90)
                        if esquerda_direita[1] == 2:
                            esquerda_direita = ["ESQUERDA", 1]
                        elif esquerda_direita[1] == 1:
                            esquerda_direita[1] += 1
                    cronometer.reset()
                    while not is_red_left() and not is_red_right() and not has_obstacle():
                        andar_reto(500)
                    brake_motors()
                    if cronometer.time() < 3000 or has_obstacle():
                        if not has_obstacle():
                            ajust_color("RED")
                            move_backward(7)
                            turn_180()
                        while ultrasound_sensor.distance() > 145 and not is_red_left() and not is_red_right() and not is_black_left() and not is_black_right():
                            andar_reto(500)
                        brake_motors()
                        if is_red_left() or is_red_right():
                            if (is_red_left() and not is_red_right()) or (not is_red_left() and is_red_right()):
                                cor_vista = "RED"
                                ajust_color(cor_vista)
                            move_backward(36)
                            if esquerda_direita[0] == "ESQUERDA":
                                turn_left_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["DIREITA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                            else:
                                turn_right_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["ESQUERDA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                        elif is_black_left() or is_black_right():
                            cor_vista = "BLACK"
                            ajust_color(cor_vista)
                            move_backward(7)
                            if esquerda_direita[0] == "ESQUERDA":
                                turn_left_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["DIREITA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                            else:
                                turn_right_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["ESQUERDA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                            find_blue_line(0)
                        elif ultrasound_sensor.distance() < 145:
                            brake_motors()
                            while ultrasound_sensor.distance() < 145:
                                andar_reto(-500)
                            while ultrasound_sensor.distance() > 145:
                                andar_reto(150)
                            brake_motors()
                            if esquerda_direita[0] == "ESQUERDA":
                                turn_left_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["DIREITA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                            else:
                                turn_right_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["ESQUERDA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                            while not is_meio_left() and not is_meio_right() and not is_blue_left() and not is_blue_right():
                                andar_reto(500)
                                if (is_black_left() or is_black_right()) or (is_yellow_left() or is_yellow_right()) or is_wall():
                                    brake_motors()
                                    cor_vista = "BLACK"
                                    ajust_color(cor_vista)
                                    move_backward(7)
                                    if esquerda_direita[0] == "ESQUERDA":
                                        turn_left_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["DIREITA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
                                    else:
                                        turn_right_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["ESQUERDA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
                                elif has_obstacle():
                                    found_wall()
                                    brake_motors()
                                    while ultrasound_sensor.distance() < 145:
                                        andar_reto(-500)
                                    brake_motors()
                                    if esquerda_direita[0] == "ESQUERDA":
                                        turn_left_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["DIREITA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
                                    else:
                                        turn_right_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["ESQUERDA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
                                elif is_red_left() or is_red_right():
                                    brake_motors()
                                    cor_vista = "RED"
                                    ajust_color(cor_vista)
                                    move_backward(36)
                                    if esquerda_direita[0] == "ESQUERDA":
                                        turn_left_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["DIREITA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
                                    else:
                                        turn_right_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["ESQUERDA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
                    else:
                        cor_vista = "RED"
                        ajust_color(cor_vista)
                        move_backward(36)
                        if (esquerda_direita[0] == "ESQUERDA" and esquerda_direita[1] == 1) or (esquerda_direita[0] == "DIREITA" and esquerda_direita[1] == 2):
                            turn_left_pid(90)
                        else:
                            turn_right_pid(90)
                        while not is_meio_left() and not is_meio_right() and not is_blue_left() and not is_blue_right() and not is_red_left() and not is_red_right() and not has_obstacle() and not is_black_left() and not is_black_right():
                            andar_reto(500)
                        brake_motors()
                        if is_red_left() or is_red_right():
                            if (is_red_left() and not is_red_right()) or (not is_red_left() and is_red_right()):
                                cor_vista = "RED"
                                ajust_color(cor_vista)
                            move_backward(36)
                            if esquerda_direita[0] == "ESQUERDA":
                                turn_left_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["DIREITA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                            else:
                                turn_right_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["ESQUERDA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                        elif is_black_left() or is_black_right():
                            cor_vista = "BLACK"
                            ajust_color(cor_vista)
                            move_backward(7)
                            if esquerda_direita[0] == "ESQUERDA":
                                turn_left_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["DIREITA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                            else:
                                turn_right_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["ESQUERDA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                            find_blue_line(0)
                        elif ultrasound_sensor.distance() < 145:
                            brake_motors()
                            while ultrasound_sensor.distance() < 145:
                                andar_reto(-500)
                            while ultrasound_sensor.distance() > 145:
                                andar_reto(150)
                            brake_motors()
                            if esquerda_direita[0] == "ESQUERDA":
                                turn_left_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["DIREITA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                            else:
                                turn_right_pid(90)
                                if esquerda_direita[1] == 2:
                                    esquerda_direita = ["ESQUERDA", 1]
                                elif esquerda_direita[1] == 1:
                                    esquerda_direita[1] += 1
                            while not is_meio_left() and not is_meio_right() and not is_blue_left() and not is_blue_right():
                                andar_reto(500)
                                if (is_black_left() or is_black_right()) or (is_yellow_left() or is_yellow_right()) or is_wall():
                                    brake_motors()
                                    cor_vista = "BLACK"
                                    ajust_color(cor_vista)
                                    move_backward(7)
                                    if esquerda_direita[0] == "ESQUERDA":
                                        turn_left_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["DIREITA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
                                    else:
                                        turn_right_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["ESQUERDA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
                                elif has_obstacle():
                                    found_wall()
                                    brake_motors()
                                    while ultrasound_sensor.distance() < 145:
                                        andar_reto(-500)
                                    brake_motors()
                                    if esquerda_direita[0] == "ESQUERDA":
                                        turn_left_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["DIREITA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
                                    else:
                                        turn_right_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["ESQUERDA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
                                elif is_red_left() or is_red_right():
                                    brake_motors()
                                    cor_vista = "RED"
                                    ajust_color(cor_vista)
                                    move_backward(36)
                                    if esquerda_direita[0] == "ESQUERDA":
                                        turn_left_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["DIREITA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
                                    else:
                                        turn_right_pid(90)
                                        if esquerda_direita[1] == 2:
                                            esquerda_direita = ["ESQUERDA", 1]
                                        elif esquerda_direita[1] == 1:
                                            esquerda_direita[1] += 1
            brake_motors()
            
        elif (is_black_left() or is_black_right()) or (is_yellow_left() or is_yellow_right()) or is_wall() or has_obstacle():
            if cor_vista != "" and (((is_red_left() or is_black_left() or is_yellow_left()) and (not is_red_right() and not is_black_right() and not is_yellow_right())) or ((not is_red_left() and not is_black_left() and not is_yellow_left()) and (is_red_right() or is_black_right() or is_yellow_right()))):
                ajust_color(cor_vista) 
            print("Achou parede")
            print("Voltando...")
            if is_black_left() or is_black_right() or is_yellow_left() or is_yellow_right():
                brake_motors()
                while left_motor.angle() > (-time_forward[0] + 10) or right_motor.angle() > (-time_forward[1] + 10):
                    andar_reto(-500)
                brake_motors()
            elif has_obstacle():
                found_wall()
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-500)
                while ultrasound_sensor.distance() > 145:
                    andar_reto(150)
                brake_motors()
            turn_right_pid(90)
            print("Vai somar mais um no numero_de_paredes")
            print(numero_de_paredes)
            find_blue_line(numero_de_paredes + 1)
    else:
        if cor_vista != "" and (((is_red_left() or is_black_left() or is_yellow_left()) and (not is_red_right() and not is_black_right() and not is_yellow_right())) or ((not is_red_left() and not is_black_left() and not is_yellow_left()) and (is_red_right() or is_black_right() or is_yellow_right()))):
            ajust_color(cor_vista) 
        turn_right_pid(90)
        while ultrasound_sensor.distance() > 145 and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right():
            andar_reto(500)
        brake_motors()
        if is_black_left() or is_black_right() or is_yellow_left() or is_yellow_right():
            if is_black_left() or is_black_right():
                cor_vista = "BLACK"
            elif is_yellow_left() or is_yellow_right():
                cor_vista = "YELLOW"
            ajust_color(cor_vista)
            move_backward(7)
        find_blue_line(0)



def go_to_check_point():
    turn_right_pid(90)

    move_backward(14) 
    
    turn_left_pid(90)

def tube_library(): 
    global dar_pra_tras
    
    branco = range_white_right()[0] 
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2  
    while left_motor.angle() < 462 or right_motor.angle() < 467: 
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        
        motors.drive(150, erro)
        
    brake_motors_para_drive_base()
    brake_motors()
    
    move_backward(15)
    turn_left_pid(90)
    move_backward(3)
    wait(500)
    move_forward(3)
    
    move_forward(20)
    move_forward(12, 200) 
    
    Open(time = 500)
    move_backward(32)
    
    

    if dar_pra_tras == True:
        turn_left_pid(90)
        move_backward(13)
        turn_left_pid(90)
        
    if dar_pra_tras == False:
        turn_180()
        
        
    
def tube_city_hall():
    go_to_j()
    
    move_to_i_or_j()
    
    if has_obstacle(): 
        found_wall()
        turn_180()
        while not is_blue_left() and not is_blue_right():
            andar_reto(250) 
        brake_motors()
        while is_blue():
            andar_reto(-500)
        brake_motors()
        turn_left_pid(90)
        
        
        j_to_i()
        
        
        brake_motors_para_drive_base()
        brake_motors()
        turn_left_pid(90)
        move_forward(40)
        turn_left_pid(90)
        move_backward(3)
        wait(500)
        move_forward(3)
        move_forward(20, 200)
        Open(time=500)

        move_backward(20)
        turn_left_pid(90)
        find_blue_line(0)
        brake_motors()
    
    else:
        not_found_wall()
        move_forward(20)
        turn_right_pid(90)
        move_backward(3)
        wait(500)
        move_forward(3)
        move_forward(20,200)
        Open(time=500)
        
        move_backward(20)
        turn_right_pid(90)
        
        find_blue_line(0)
        brake_motors()
        

    
def tube_school():
    
    go_to_i()

    move_to_i_or_j()
    
    if has_obstacle(): 
        found_wall()
        turn_180()
        while not is_blue_left() and not is_blue_right():
            andar_reto(300)
        brake_motors()
        while is_blue():
            andar_reto(-500)
        brake_motors()
        turn_right_pid(90)
            
        i_to_j()
            
        brake_motors_para_drive_base()
        brake_motors()
        turn_right_pid(90)
        
        move_to_middle()
        
        turn_right_pid(90)
    
        move_forward(12)
        
        if has_obstacle(): #"G"
            found_wall()
            move_backward(12)
            turn_left_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(7)
            turn_right_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            print("Bati no RED")
            move_backward(36)
            turn_right_pid(90)
            while not has_obstacle():
                andar_reto(500)
            brake_motors()
            while ultrasound_sensor.distance() < 145:
                andar_reto(-500)
            brake_motors()
            while ultrasound_sensor.distance() > 145:
                andar_reto(150)
            brake_motors()
            turn_left_pid(90)
            
            
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            print("Bati no RED 2")
            
            move_backward(7)
            turn_right_pid(90)
            move_backward(3)
            wait(500)
            move_forward(3)
            move_forward(15, 200)
            Open(time=500)
            move_backward(15)
            turn_right_pid(90)
            
            
            
            while ultrasound_sensor.distance() > 145:
                andar_reto(500)
            brake_motors()
            turn_right_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(7)
            turn_left_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            print("Bati no RED")
            move_backward(36)
            turn_left_pid(90)
            find_blue_line(0)
            brake_motors()
        else:
            not_found_wall()
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            print("Bati no RED")
            move_backward(7)
            turn_right_pid(90)
            move_backward(3)
            wait(500)
            move_forward(3)
            move_forward(15,200)
            
            
            Open(time=500)
            move_backward(15)
            turn_right_pid(90)
            while not is_red_left() and not is_red_right() and ultrasound_sensor.distance() > 145:
                andar_reto(500)
            brake_motors()
            if ultrasound_sensor.distance() < 145:
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-500)
                while ultrasound_sensor.distance() > 145:
                    andar_reto(150)
                brake_motors()
                turn_left_pid(90)
                find_blue_line(0)
            else:
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(36)
                turn_left_pid(90)
                find_blue_line(0)
                brake_motors()
    else:
        not_found_wall()
        move_forward(21)
        turn_right_pid(90)
        move_backward(3)
        wait(500)
        move_forward(3)
        move_forward(20,200)
        Open(time=500)
        move_backward(20)
        turn_right_pid(90)
        find_blue_line(0)
        
def tube_museum():
    
    go_to_j()

    move_to_i_or_j() 
    
    
    if has_obstacle(): 
        found_wall()
        move_backward(7) #middle_to_obstacle()
        turn_180()
        while not is_blue_left() and not is_blue_right():
            andar_reto(300)
        brake_motors()
        while is_blue():
            andar_reto(-500)
        turn_left_pid(90)
        
        j_to_i()
        
        brake_motors_para_drive_base()
        brake_motors()
        turn_left_pid(90)
        
        move_to_middle()
        
        turn_left_pid(90)
        middle_to_obstacle()
        
        if has_obstacle():

            found_wall()
            move_backward(7) #middle_to_obstacle()
            turn_right_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(7)
            turn_left_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            print("Bati no RED")
            move_backward(36)
            turn_left_pid(90)
            move_forward(32.5)
            turn_right_pid(90)
            move_backward(3)
            wait(500)
            move_forward(3)
            move_forward(15,200)
            
            Open(time=500)
            move_backward(15)
            turn_right_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(7)
            turn_right_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            print("Bati no RED")
            move_backward(36)
            turn_right_pid(90)
            find_blue_line(0)
            brake_motors()
        else:
            not_found_wall()
            while not has_obstacle() and not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            if has_obstacle():
                found_wall()
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-500)
                brake_motors()
                while ultrasound_sensor.distance() > 145:
                    andar_reto(150)
                brake_motors()
                
                turn_right_pid(90)
                move_forward(30)
                turn_left_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(15,200)
                
                Open(time=500)
                move_backward(15)
                turn_left_pid(90)
                while ultrasound_sensor.distance() > 145:
                    andar_reto(500)
                brake_motors()
                turn_left_pid(90)
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(36)
                turn_right_pid(90)
                find_blue_line(0)
                brake_motors()
            else:
                not_found_wall()
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(7) #middle_to_obstacle()
                turn_right_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(20,200)
                
                Open(time=500)
                move_backward(20)
                turn_right_pid(90)
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    found_wall()
                    while ultrasound_sensor.distance() < 145:
                        andar_reto(-500)
                    brake_motors()
                    turn_right_pid()
                    find_blue_line(0)
                else:
                    not_found_wall()
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(36)
                    turn_right_pid(90)
                    find_blue_line(0)
                    brake_motors()
    else: 
        print("Não existe J")
        not_found_wall()
        
        i_or_j_to_middle()
        
        turn_left_pid(90)
        
        middle_to_obstacle()
    
        if has_obstacle(): 
            found_wall()
            move_backward(7) #middle_to_obstacle()
            turn_right_pid(90)
            move_forward(30)
            turn_left_pid(90)
            move_backward(3)
            wait(500)
            move_forward(3)
            move_forward(20,200)
            #abre e retorna
            Open(time=500)
            move_backward(20)
            turn_left_pid(90)
            find_blue_line(0)
            
        else: #Objeto "H" não existe
            print("Não existe H")
            not_found_wall()
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            
            print("Achou RED")
            cor_vista = "RED"
            ajust_color(cor_vista)
            
            move_backward(7)
            
            turn_right_pid(90)
            move_backward(3)
            wait(500)
            move_forward(3)
            move_forward(17,200)
            
            Open(time = 500)
            move_backward(17)
            turn_right_pid(90)
            move_forward(29)
            turn_right_pid(90)
            find_blue_line(0)
                
def tube_drugstore():
    
    go_to_j()

    move_to_i_or_j()
    
    if has_obstacle(): 
        found_wall()
        turn_180()
        while not is_blue_left() and not is_blue_right():
            andar_reto(300)
        brake_motors()
        
        while is_blue():
            andar_reto(-500)
        brake_motors()
        turn_left_pid(90)
        
        j_to_i()
        
        brake_motors_para_drive_base()
        brake_motors()
        turn_left_pid(90)
        move_to_middle()
        turn_left_pid(90)
        middle_to_obstacle()
        
        if has_obstacle(): 
            found_wall()
            move_backward(7) #middle_to_obstacle()
            turn_right_pid(90)
            
            while not is_black_left() or not is_black_right():
                andar_reto(500)
            brake_motors()
            
            
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            
            move_backward(7)
            
            turn_left_pid(90)
            move_forward(28)
            turn_left_pid(90)
            move_backward(3)
            wait(500)
            move_forward(3)
            move_forward(22,200)
            
            Open(time=500)
            move_backward(22)
            turn_left_pid(90)
            while not is_red_left() or not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            move_backward(36)
            turn_right_pid(90)
            find_blue_line(0)
            brake_motors()
        else:    
            not_found_wall()
            move_forward(27.5)
            turn_right_pid(90)
            move_backward(3)
            wait(500)
            move_forward(3)
            move_forward(15,200)
            
            Open(time=500)
            move_backward(10)
            turn_right_pid(90)
            while not has_obstacle() and not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            if has_obstacle():
                found_wall()
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-500)
                brake_motors()
                turn_right_pid(90)
                find_blue_line(0)
            else:
                not_found_wall()
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(36)
                turn_right_pid(90)
                find_blue_line(0)
                brake_motors()
    else:
        not_found_wall()
        i_or_j_to_middle() 
        turn_right_pid(90)
        middle_to_obstacle()
        if has_obstacle(): 
            found_wall()
            move_backward(7) #middle_to_obstacle()
            turn_left_pid(90)
            middle_to_obstacle()
            if has_obstacle(): 

                found_wall()
                move_backward(7) #middle_to_obstacle()
                turn_180()
                while not is_blue_left() and not is_blue_right():
                    andar_reto(300)
                brake_motors()
                while is_blue():
                    andar_reto(-500)
                brake_motors()
                turn_left_pid(90)
                
                j_to_i()
                
                brake_motors_para_drive_base()
                brake_motors()
                turn_left_pid(90)
                while not is_black_left() and not is_black_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                turn_left_pid(90)
                move_forward(28)
                turn_left_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(20,200)
                Open(time=500)
                
                move_backward(20)
                turn_left_pid(90)
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(36)
                turn_right_pid(90)
                find_blue_line(0)
                brake_motors() 
            else:
                not_found_wall()
                while not is_black_left() and not is_black_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                move_forward(36)
                turn_right_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(20,200)
                Open(time=500)
                move_backward(20)
                turn_right_pid(90)
                
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    found_wall()
                    while ultrasound_sensor.distance() < 145:
                        andar_reto(-500)
                    brake_motors()
                    turn_left_pid(90)
                    find_blue_line(0)
                else:
                    not_found_wall()
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(36)
                    turn_left_pid(90)
                    find_blue_line(0)
        else:
            not_found_wall()
            move_forward(23)
            turn_left_pid(90)
            move_backward(3)
            wait(500)
            move_forward(3)
            move_forward(20,200)
            
            Open(time=500) 
            move_backward(20)
            turn_right_pid(90)
            while not has_obstacle() and not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            if has_obstacle():
                found_wall()
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-500)
                brake_motors()
                turn_right_pid(90)
                find_blue_line(0)
            else:
                not_found_wall()
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(36)
                turn_right_pid(90)
                find_blue_line(0)
        
def tube_bakery():
    
    go_to_i()

    move_to_i_or_j()
    
    if has_obstacle(): 
        
        found_wall()
        move_backward(10)
        turn_180()
        while not is_blue_left() and not is_blue_right():
            andar_reto(300)
        brake_motors()
        
        
        while is_blue():
            andar_reto(-500)
        brake_motors()
        turn_right_pid(90)
        
        
        i_to_j()
        
        
        
        
        brake_motors_para_drive_base()
        brake_motors()
        turn_right_pid(90)
        
        move_to_middle()
        
        turn_right_pid(90)
        
        middle_to_obstacle()
        
        if has_obstacle():
            found_wall()
            move_backward(7) #middle_to_obstacle()
            turn_left_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(7)
            turn_right_pid(90)
            while not is_red_left() and not is_red_right() and not has_obstacle():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            print("Bati no RED")
            move_backward(7)
            turn_right_pid(90)
            move_backward(3)
            wait(500)
            move_forward(3)
            move_forward(20,200)
            Open(time=500)
            move_backward(20)
            turn_right_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            move_backward(36)
            turn_left_pid(90)
            find_blue_line(0)
            brake_motors()
        else:
            not_found_wall()
            while not is_red_left() and not is_red_right() and not has_obstacle():
                andar_reto(500)
            brake_motors()
            if has_obstacle():
                found_wall()
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-500)
                brake_motors()
                while ultrasound_sensor.distance() > 145:
                    andar_reto(150)
                brake_motors()
            else:
                not_found_wall()
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(36)
            turn_left_pid(90)
            middle_to_obstacle() # de frente pro D
            
            if has_obstacle(): 
                found_wall()
                move_backward(7) #middle_to_obstacle()
                turn_left_pid(90)
                move_forward(55)
                turn_right_pid(90)
                while not is_black_left() and not is_black_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(7)
                turn_right_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(20,200)
                Open(time=500)
                move_backward(20)
                turn_right_pid(90)
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(36)
                turn_left_pid(90)
                find_blue_line(0)
                brake_motors()
            else:
                not_found_wall()
                move_forward(20)
                turn_right_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(15,200)
                Open(time=500)
                move_backward(15)
                turn_right_pid(90)
                while ultrasound_sensor.distance() > 145:
                    andar_reto(500)
                brake_motors()
                turn_right_pid(90)
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    found_wall()
                    while ultrasound_sensor.distance() < 145:
                        andar_reto(-500)
                    brake_motors()
                    turn_left_pid(90)
                    find_blue_line(0)
                else:
                    not_found_wall()
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(36)
                    turn_left_pid(90)
                    find_blue_line(0)
    else:
        not_found_wall()
        move_forward(53)
        middle_to_obstacle()
        
        if has_obstacle():
            found_wall()
            while ultrasound_sensor.distance() < 145:
                andar_reto(-500)
            brake_motors()
            
            while ultrasound_sensor.distance() > 145:
                andar_reto(150)
            brake_motors()
                
            turn_left_pid(90)
            middle_to_obstacle()
            if has_obstacle():
                found_wall()
                move_backward(10)
                turn_left_pid(90)
                while not is_blue_left() and not is_blue_right():
                    andar_reto(300)
                brake_motors()
                while is_blue():
                    andar_reto(-500)
                brake_motors()
                turn_right_pid(90)
                
                i_to_j()
                
                brake_motors_para_drive_base()
                brake_motors()
                turn_right_pid(90)
                while not is_black_left() and not is_black_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(7)
                turn_right_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(15,200)
                Open(time=500)
                move_backward(15)
                turn_right_pid(90)
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(36)
                turn_left_pid(90)
                find_blue_line(0)
                brake_motors()
            else:
                not_found_wall()
                move_forward(45)
                turn_right_pid(90)
                while not is_black_left() and not is_black_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(7)
                turn_right_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(15,200)
                Open(time=500)
                move_backward(15)
                turn_right_pid(90)
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    found_wall()
                    while ultrasound_sensor.distance() < 145:
                        andar_reto(-500)
                    brake_motors()
                    turn_left_pid(90)
                    find_blue_line(0)
                else:
                    not_found_wall()
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(36)
                    turn_left_pid(90)
                    find_blue_line(0)
        else:
            not_found_wall()
            move_forward(20) 
            turn_right_pid(90)
            move_backward(3)
            wait(500)
            move_forward(3)
            move_forward(20,200)
            Open(time=500)
            move_backward(20)
            turn_right_pid(90)
            find_blue_line(0)
    
def tube_park():
    
    go_to_j()
    
    move_to_i_or_j()
    
    if has_obstacle(): 
        found_wall()
        print("Tem um objeto no J indo pro Park")
        
        turn_180()
        while not is_blue_left() and not is_blue_right():
            andar_reto(300)
        brake_motors()
        
        while is_blue():
            andar_reto(-500)
        brake_motors()
        turn_left_pid(90)
        
        j_to_i()
            
        brake_motors_para_drive_base()
        brake_motors()
        turn_left_pid(90)
        move_to_middle()
        middle_to_obstacle()
        
        if has_obstacle(): 
            print("Tem objeto no D")
            found_wall()
            while ultrasound_sensor.distance() < 145:
                andar_reto(-500)
            brake_motors()
            while ultrasound_sensor.distance() > 145:
                andar_reto(150)
            brake_motors()
            turn_left_pid(90)
            
            # Distancia até o meio e virar pro Obstáculo E
            move_forward(53)
            
            turn_right_pid(90)
            while not is_black_left() and not is_black_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            
            

            move_backward(7)
            turn_right_pid(90)
            move_forward(32.5)
            turn_left_pid(90)
            move_backward(3)
            wait(500)
            move_forward(3)
            move_forward(15,200)
            Open(time = 500)
            move_backward(15)
            turn_left_pid(90)
            
            # Voltando agora
            
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            move_backward(36)
            
            
            turn_left_pid(90) 
            
            
            while ultrasound_sensor.distance() > 145:
                andar_reto(500)
            brake_motors()
            while ultrasound_sensor.distance() < 145:
                andar_reto(-150)
            brake_motors()
            
            turn_left_pid(90)
            
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            
            move_backward(36)
            turn_right_pid(90)
            find_blue_line(0)
            brake_motors()
            
        else:
            print("Não tem objeto no D")
            not_found_wall()
            while not is_black_left() and not is_black_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            
            move_backward(7)
            turn_right_pid(90)
            middle_to_obstacle()
            
            if has_obstacle(): 
                found_wall()
                move_backward(7) #middle_to_obstacle()
                turn_180()
                move_forward(28)
                turn_right_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(15,200)
                Open(time=500)
                move_backward(15)
                turn_right_pid(90)
                while ultrasound_sensor.distance() > 145:
                    andar_reto(500)
                brake_motors()
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-200)
                brake_motors()
                turn_right_pid(90)
                find_blue_line(0)
                brake_motors()
            else:
                not_found_wall()
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                
                move_backward(7) 
                turn_left_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(15,200)
                Open(time=500)
                
                
                move_backward(15)
                turn_left_pid(90)
                move_forward(29) 
                
                turn_left_pid(90)
                find_blue_line(0)
    else:
        not_found_wall()
        i_or_j_to_middle()
        wait(1000)
        middle_to_obstacle()
        
        if has_obstacle(): 
            found_wall()
            move_backward(7) #middle_to_obstacle()
            turn_right_pid(90)
            middle_to_obstacle()
            
            if has_obstacle(): 
                found_wall()
                move_backward(7) #middle_to_obstacle()
                turn_right_pid(90)
                while not is_blue_left() and not is_blue_right():
                    andar_reto(300)
                brake_motors()
                while is_blue():
                    andar_reto(-500)
                brake_motors()
                turn_left_pid(90)
                
                j_to_i()
                
                brake_motors_para_drive_base()
                brake_motors()
                turn_left_pid(90)
                while not is_black_left() and not is_black_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(7)
                turn_left_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(15,200)
                Open(time=500)
                move_backward(15)
                turn_right_pid(90)
                move_backward(29)
                turn_right_pid(90)
                find_blue_line(0)
                brake_motors()
            else:
                not_found_wall()
                move_forward(53)
                turn_left_pid(90)
                while not is_black_left() and not is_black_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                
                move_backward(7)
                turn_right_pid(90)
                
                middle_to_obstacle()
                
                if has_obstacle():
                    found_wall()
                    move_backward(7) #middle_to_obstacle()
                    turn_180()
                    move_forward(28)
                    turn_right_pid(90)
                    move_backward(3)
                    wait(500)
                    move_forward(3)
                    move_forward(15,200)
                    Open(time=500)
                    move_backward(15)
                    turn_right_pid(90)
                    while ultrasound_sensor.distance() > 145:
                        andar_reto(500)
                    brake_motors()
                    turn_right_pid(90)
                    find_blue_line(0)
                    brake_motors()
                else:
                    not_found_wall()
                    while not is_red_left() and not is_red_right():
                        andar_reto(500)
                    brake_motors()
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(7)
                    
                    turn_left_pid(90)
                    move_backward(3)
                    wait(500)
                    move_forward(3)
                    move_forward(15,200)
                    Open(time=500)
                    move_backward(15)
                    turn_right_pid(90)
                    move_backward(29)
                    turn_right_pid(90)
                    while not has_obstacle() and not is_blue():
                        andar_reto(500)
                    brake_motors()
                    if has_obstacle():
                        found_wall()
                        while ultrasound_sensor.distance() < 145:
                            andar_reto(-500)
                        brake_motors()
                        turn_right_pid(90)
                        find_blue_line(0)
                    
        else:
            not_found_wall()
            while not is_black_left() and not is_black_right():
                andar_reto(500)   
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(7)
            turn_right_pid(90)
            middle_to_obstacle()
            if has_obstacle():
                found_wall() 
                move_backward(7) #middle_to_obstacle()
                turn_180()
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(15,200)
                Open(time=500)
                move_backward(15)
                turn_left_pid(90)
                move_backward(29)
                turn_left_pid(90)
                
                find_blue_line(0)
            else:
                not_found_wall()
                move_forward(20)
                turn_left_pid(90)
                move_backward(3)
                wait(500)
                move_forward(3)
                move_forward(15.5,200)
                Open(time=500)
                move_backward(15.5)
                turn_left_pid(90)
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    found_wall()
                    while ultrasound_sensor.distance() < 145:
                        andar_reto(-500)
                    brake_motors()
                    turn_left_pid(90)
                    find_blue_line(0)
                else:
                    not_found_wall()
                    not_found_wall()
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(36)
                    turn_left_pid(90)
                    find_blue_line(0)
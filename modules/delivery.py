from modules.motors import *
from modules.beeps import *
from modules.claw import *
from modules.variables import *
from modules.path import *
from pybricks.tools import StopWatch

crono = StopWatch()

# Função recursiva para achar a linha azul (ida ou volta) ----------------------------------------

def find_blue_line(numero_de_paredes):
    esquerda_direita = ["ESQUERDA", 1]
    
    if claw_motor.angle() < 10 and claw_motor.angle() > -10:
        print("Entrei aqui papai")
        Close(time=500)
    if numero_de_paredes < 4:
        brake_motors()
        
        cor_vista = ""
        
        print("procurando")
        while not is_blue() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right() and not has_obstacle():
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
            while not is_blue():
                andar_reto(500)
                if (is_black_left() or is_black_right()) or (is_yellow_left() or is_yellow_right()) or is_wall():
                    brake_motors()
                    cor_vista = "BLACK"
                    ajust_color(cor_vista)
                    turn_180()
                elif has_obstacle():
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
                            while not is_blue():
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
                        while not is_blue() and not is_red_left() and not is_red_right() and not has_obstacle() and not is_black_left() and not is_black_right():
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
                            while not is_blue():
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

    move_backward(13)
    
    turn_left_pid(90)

def tube_library():
    crono.reset()
    branco = range_white_right()[0] 
    azul = range_blue_right()[0] #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 1400: 
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)
    brake_motors_para_drive_base()
    brake_motors()
    
    move_backward(6)
    turn_left_pid(90)
    move_forward(32) 
    Open(time = 500)
    move_backward(32) 
    Close(time = 500)
    turn_left_pid(90)
    move_backward(13) 
    turn_left_pid(90)
        
    
def tube_city_hall():
    

    crono.reset()
    branco = range_white_right()[0]
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2  
    vel = 100
    while crono.time() < 3600: 
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors_para_drive_base()
    brake_motors()
    turn_left_pid(90)
    move_forward(18) 
    
    if has_obstacle() :
        turn_180()
        while not is_blue():
            andar_reto(500)
        brake_motors()
        while is_blue():
            andar_reto(-500)
        brake_motors()
        turn_left_pid(90)
        
        
        branco = range_white_right()[0] 
        azul = range_blue_right()[0] #22
        threshold = (branco + azul) / 2  # = 40
        vel = 100
        crono.reset()
        while crono.time() < 6000:
            delta = red_right() - threshold
            kp = 0.5
            erro = delta * kp
            motors.drive(vel, erro)
        brake_motors_para_drive_base()
        brake_motors()
        turn_left_pid(90)
        move_forward(40)
        turn_left_pid(90)
    
        move_forward(20)
        Open(time=500)

        move_backward(20)
        turn_left_pid(90)
        find_blue_line(0)
        brake_motors()
    
    else:
        
        not_found_wall()
        move_forward(20)
        turn_right_pid(90)
        
        move_forward(20)
        Open(time=500)
        
        move_backward(20)
        turn_right_pid(90)
        
        find_blue_line(0)
        brake_motors()
        

    
def tube_school():
    
    crono.reset()
    branco = range_white_right()[0]
    azul = range_blue_right()[0]  
    threshold = (branco + azul) / 2  
    vel = 100
    while crono.time() < 9500:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors_para_drive_base()
    brake_motors()
    turn_left_pid(90)
    move_forward(18)
    if has_obstacle(): 
        found_wall()
        turn_180()
        while not is_blue():
            andar_reto(500)
        brake_motors()
        while is_blue():
            andar_reto(-500)
        brake_motors()
        turn_right_pid(90)
        branco = range_white_left()[0]
        azul = range_blue_left()[0]
        threshold = (branco + azul) / 2  
        vel = 100
        crono.reset()
        while crono.time() < 6000:
            delta = threshold - red_left()
            kp = 0.5 
            erro = delta * kp
            motors.drive(vel, erro)
            
        brake_motors_para_drive_base()
        brake_motors()
        turn_right_pid(90)
        move_forward(68)
        turn_right_pid(90)
        #G
        move_forward(12)
        
        if has_obstacle(): #"G"
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
            move_forward(15)
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
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            print("Bati no RED")
            move_backward(7)
            turn_right_pid(90)
            move_forward(15)
            
            
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
        
        move_forward(20)
        Open(time=500)
        move_backward(20)
        turn_right_pid(90)
        find_blue_line(0)
        
def tube_museum():
    
    crono.reset()
    branco = range_white_right()[0] 
    azul = range_blue_right()[0] #22
    threshold = (branco + azul) / 2  
    vel = 100
    while crono.time() < 3600: #4000
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors_para_drive_base()
    brake_motors()
    turn_left_pid(90)
    move_forward(15) 
    
    if has_obstacle(): 
        found_wall()
        move_backward(10)
        turn_180()
        while not is_blue():
            andar_reto(500)
        brake_motors()
        while is_blue():
            andar_reto(-500)
        turn_left_pid(90)
        branco = range_white_right()[0] 
        azul = range_blue_right()[0] 
        threshold = (branco + azul) / 2  
        vel = 100
        crono.reset()
        while crono.time() < 6500: 
            delta = red_right() - threshold
            kp = 0.5
            erro = delta * kp
            motors.drive(vel, erro)
        brake_motors_para_drive_base()
        brake_motors()
        turn_left_pid(90)
        move_forward(65)
        turn_left_pid(90)
        move_forward(10)
        if has_obstacle():

            found_wall()
            move_backward(10)
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
            move_forward(15)
            
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
            move_forward(60)
            if has_obstacle(): 

                move_backward(10)
                turn_right_pid(90)
                move_forward(30)
                turn_left_pid(90)
                move_forward(15)
                
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
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                print("Bati no RED")
                move_backward(5)
                turn_right_pid(90)
                move_forward(15)
                
                Open(time=500)
                move_backward(15)
                turn_right_pid(90)
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    while ultrasound_sensor.distance() < 145:
                        andar_reto(-500)
                    brake_motors()
                    turn_right_pid()
                    find_blue_line(0)
                else:
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(36)
                    turn_right_pid(90)
                    find_blue_line(0)
                    brake_motors()
    else: 
        print("Não existe J")
        not_found_wall()
        move_forward(55)
        turn_left_pid(90)
        move_forward(8)
    
        if has_obstacle(): 
            found_wall()
            move_backward(8)
            turn_right_pid(90)
            move_forward(20)
            turn_left_pid(90)
            move_forward(20)
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
            move_forward(17)
            
            Open(time = 500)
            move_backward(17)
            turn_right_pid(90)
            move_forward(29)
            turn_right_pid(90)
            find_blue_line(0)
                
def tube_drugstore():
    
    crono.reset()
    branco = range_white_right()[0] 
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2  
    vel = 100
    while crono.time() < 3600: 
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors_para_drive_base()
    brake_motors()
    turn_left_pid(90)
    move_forward(18)
    
    if has_obstacle(): 
        found_wall()
        turn_180()
        while not is_blue():
            andar_reto(500)
        brake_motors()
        
        while is_blue():
            andar_reto(-500)
        brake_motors()
        turn_left_pid(90)
        
        branco = range_white_right()[0] 
        azul = range_blue_right()[0] #22
        threshold = (branco + azul) / 2  
        vel = 100
        crono.reset()
        while crono.time() < 6500: 
            delta = red_right() - threshold
            kp = 0.5
            erro = delta * kp
            motors.drive(vel, erro)
        brake_motors_para_drive_base()
        brake_motors()
        turn_left_pid(90)
        move_forward(68)
        turn_left_pid(90)
        move_forward(8)
        
        if has_obstacle(): 
            found_wall()
            move_backward(5)
            turn_right_pid(90)
            
            while not is_black_left() or not is_black_right():
                andar_reto(500)
            brake_motors()
            
            
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            
            move_backward(5)
            
            turn_left_pid(90)
            move_forward(24)
            turn_left_pid(90)
            move_forward(22)
            
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
            move_forward(15)
            
            Open(time=500)
            move_backward(10)
            turn_right_pid(90)
            while not has_obstacle() and not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            if has_obstacle():
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-500)
                brake_motors()
                turn_right_pid(90)
                find_blue_line(0)
            else:
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(36)
                turn_right_pid(90)
                find_blue_line(0)
                brake_motors()
    else:
        not_found_wall()
        move_forward(52) 
        turn_right_pid(90)
        move_forward(10)
        if has_obstacle(): 
            found_wall()
            move_backward(10)
            turn_left_pid(90)
            move_forward(10)
            if has_obstacle(): 

                found_wall()
                move_backward(10)
                turn_180()
                while not is_blue():
                    andar_reto(500)
                brake_motors()
                while is_blue():
                    andar_reto(-500)
                brake_motors()
                turn_left_pid(90)
                
                branco = range_white_right()[0] 
                azul = range_blue_right()[0] 
                threshold = (branco + azul) / 2  
                vel = 100
                crono.reset()
                while crono.time() < 6500: 
                    delta = red_right() - threshold
                    kp = 0.5
                    erro = delta * kp
                    motors.drive(vel, erro)
                brake_motors_para_drive_base()
                brake_motors()
                turn_left_pid(90)
                while not is_black_left() and not is_black_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                turn_left_pid(90)
                move_forward(22)
                turn_left_pid(90)
                move_forward(20)
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
                move_forward(20)
                Open(time=500)
                move_backward(20)
                turn_right_pid(90)
                
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    while ultrasound_sensor.distance() < 145:
                        andar_reto(-500)
                    brake_motors()
                    turn_left_pid(90)
                    find_blue_line(0)
                else:
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(36)
                    turn_left_pid(90)
                    find_blue_line(0)
        else:
            not_found_wall()
            move_forward(22)
            turn_left_pid(90)
            move_forward(20)
            
            Open(time=500) 
            move_backward(20)
            turn_right_pid(90)
            while not has_obstacle() and not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            if has_obstacle():
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-500)
                brake_motors()
                turn_right_pid(90)
                find_blue_line(0)
            else:
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(36)
                turn_right_pid(90)
                find_blue_line(0)
        
def tube_bakery():
    
    crono.reset()
    branco = range_white_right()[0]
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2  
    vel = 100
    while crono.time() < 9500:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors_para_drive_base()
    brake_motors()
    turn_left_pid(90)
    move_forward(15)
    
    if has_obstacle(): 
        
        found_wall()
        move_backward(10)
        turn_180()
        while not is_blue():
            andar_reto(500)
        brake_motors()
        
        
        while is_blue():
            andar_reto(-500)
        brake_motors()
        turn_right_pid(90)
        branco = range_white_left()[0]
        azul = range_blue_left()[0]
        threshold = (branco + azul) / 2  
        vel = 100
        crono.reset()
        
        
        while crono.time() < 6000:
            delta = threshold - red_left()
            kp = 0.5
            erro = delta * kp
            motors.drive(vel, erro)
        brake_motors_para_drive_base()
        brake_motors()
        turn_right_pid(90)
        
        move_forward(70)
        turn_right_pid(90)
        move_forward(10)
        if has_obstacle():
            found_wall()
            move_backward(10)
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
            move_forward(20)
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
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-500)
                brake_motors()
                while ultrasound_sensor.distance() > 145:
                    andar_reto(150)
                brake_motors()
            else:
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(36)
            turn_left_pid(90)
            move_forward(7)##
            if has_obstacle(): 
                found_wall()
                move_backward(13)
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
                move_forward(20)
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
                move_forward(18)
                turn_right_pid(90)
                move_forward(15)
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
                    while ultrasound_sensor.distance() < 145:
                        andar_reto(-500)
                    brake_motors()
                    turn_left_pid(90)
                    find_blue_line(0)
                else:
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(36)
                    turn_left_pid(90)
                    find_blue_line(0)
    else:
        not_found_wall()
        move_forward(60)
        if has_obstacle():
            found_wall()
            turn_left_pid(90)
            move_forward(10)
            if has_obstacle():
                found_wall()
                move_backward(10)
                turn_left_pid(90)
                while not is_blue():
                    andar_reto(500)
                brake_motors()
                while is_blue():
                    andar_reto(-500)
                brake_motors()
                turn_right_pid(90)
                branco = range_white_left()[0]
                azul = range_blue_left()[0]
                threshold = (branco + azul) / 2  
                vel = 100
                crono.reset()
                while crono.time() < 6000:
                    delta = threshold - red_left()
                    kp = 0.5
                    erro = delta * kp
                    motors.drive(vel, erro)
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
                move_forward(15)
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
                move_forward(15)
                Open(time=500)
                move_backward(15)
                turn_right_pid(90)
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    while ultrasound_sensor.distance() < 145:
                        andar_reto(-500)
                    brake_motors()
                    turn_left_pid(90)
                    find_blue_line(0)
                else:
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(36)
                    turn_left_pid(90)
                    find_blue_line(0)
        else:
            not_found_wall()
            move_forward(30)
            turn_right_pid(90)
            move_forward(20)
            Open(time=500)
            move_backward(20)
            turn_right_pid(90)
            Close(time=500)
            
            while not has_obstacle() and not is_blue():
                andar_reto(500)
            brake_motors()
            if has_obstacle():
                while ultrasound_sensor.distance() < 145:
                    andar_reto(-500)
                brake_motors()
                turn_right_pid(90)
                find_blue_line(0)
    
def tube_park():
    
    
    crono.reset()
    branco = range_white_right()[0] 
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2  
    vel = 100
    while crono.time() < 3600: 
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors_para_drive_base()
    brake_motors()
    turn_left_pid(90)
    move_forward(16)
    
    if has_obstacle(): 
        print("Tem um objeto no J indo pro Park")
        
        turn_180()
        while not is_blue():
            andar_reto(500)
        brake_motors()
        
        while is_blue():
            andar_reto(-500)
        brake_motors()
        turn_left_pid(90)
        
        branco = range_white_right()[0] 
        azul = range_blue_right()[0] #22
        threshold = (branco + azul) / 2  
        vel = 100
        crono.reset()
        while crono.time() < 6000: 
            delta = red_right() - threshold
            kp = 0.5
            erro = delta * kp
            motors.drive(vel, erro)
        brake_motors_para_drive_base()
        brake_motors()
        turn_left_pid(90)
        move_forward(64)
        
        if has_obstacle(): 
            print("Tem objeto no D")
            
            turn_left_pid(90)
            move_forward(57.5)
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
            move_forward(15)
            Open(time=500)
            move_backward(15)
            turn_left_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            move_backward(36)
            turn_right_pid(90)
            while ultrasound_sensor.distance() > 145:
                andar_reto(500)
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
            while not is_black_left() and not is_black_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            
            move_backward(7)
            turn_right_pid(90)
            move_forward(5)
            
            if has_obstacle(): 
                
                turn_180()
                move_forward(37.5)
                turn_right_pid(90)
                move_forward(15)
                Open(time=500)
                move_backward(15)
                turn_right_pid(90)
                while ultrasound.distance() > 145:
                    andar_reto(500)
                brake_motors()
                while ultrasound.distance() < 145:
                    andar_reto(-200)
                brake_motors()
                turn_right_pid(90)
                find_blue_line(0)
                brake_motors()
            else:
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                
                move_backward(7) 
                turn_left_pid(90)
                move_forward(15)
                Open(time=500)
                move_backward(15)
                turn_left_pid(90)
                move_forward(29)
                turn_left_pid(90)
                Close(False)
                while not is_blue() and not has_obstacle():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    while ultrasound.distance() < 145:
                        andar_reto(-500)
                    brake_motors()
                    turn_right_pid(90)
                    find_blue_line(0)
    else:
        move_forward(65)
        
        if has_obstacle(): 
            
            move_backward(4)
            turn_right_pid(90)
            move_forward(5)
            
            
            if has_obstacle(): 
                move_backward(5)
                turn_right_pid(90)
                while not is_blue():
                    andar_reto(500)
                brake_motors()
                while is_blue():
                    andar_reto(-500)
                brake_motors()
                turn_left_pid(90)
                branco = range_white_right()[0] 
                azul = range_blue_right()[0] 
                threshold = (branco + azul) / 2  
                vel = 100
                crono.reset()
                while crono.time() < 6500: 
                    delta = red_right() - threshold
                    kp = 0.5
                    erro = delta * kp
                    motors.drive(vel, erro)
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
                move_forward(15)
                Open(time=500)
                move_backward(15)
                turn_right_pid(90)
                move_backward(29)
                turn_right_pid(90)
                find_blue_line(0)
                brake_motors()
            else:
                
                move_forward(47)
                turn_left_pid(90)
                
                while not is_black_left() and not is_black_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "BLACK"
                ajust_color(cor_vista)
                
                move_backward(7)
                turn_right_pid(90)
                move_forward(5)
                
                if has_obstacle():
                    turn_180()
                    move_forward(32.5)
                    turn_right_pid(90)
                    move_forward(15)
                    Open(time=500)
                    move_backward(15)
                    turn_right_pid(90)
                    while ultrasound.distance() > 145:
                        andar_reto(500)
                    brake_motors()
                    turn_right_pid(90)
                    find_blue_line(0)
                    brake_motors()
                else:
                    while not is_red_left() and not is_red_right():
                        andar_reto(500)
                    brake_motors()
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(7)
                    
                    turn_left_pid(90)
                    move_forward(15)
                    Open(time=500)
                    move_backward(15)
                    turn_right_pid(90)
                    move_backward(29)
                    turn_right_pid(90)
                    while not has_obstacle() and not is_blue():
                        andar_reto(500)
                    brake_motors()
                    if has_obstacle():
                        while ultrasound.distance() < 145:
                            andar_reto(-500)
                        brake_motors()
                        turn_right_pid(90)
                        find_blue_line(0)
                    
        else:
            move_forward(15)
            while not is_black_left() and not is_black_right():
                andar_reto(500)   
            brake_motors()
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            move_backward(7)
            turn_right_pid(90)
            move_forward(5)
            if has_obstacle(): 
                move_backward(5)
                turn_180()
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                move_forward(15)
                Open(time=500)
                move_backward(15)
                turn_left_pid(90)
                move_backward(29)
                turn_left_pid(90)
                
                find_blue_line(0)
            else:
                move_forward(23)
                turn_left_pid(90)
                move_forward(15.5)
                Open(time=500)
                move_backward(15.5)
                turn_left_pid(90)
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    while ultrasound.distance() < 145:
                        andar_reto(-500)
                    brake_motors()
                    turn_left_pid(90)
                    find_blue_line(0)
                else:
                    cor_vista = "RED"
                    ajust_color(cor_vista)
                    move_backward(36)
                    turn_left_pid(90)
                    find_blue_line(0)
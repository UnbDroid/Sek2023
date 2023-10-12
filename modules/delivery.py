from modules.motors import *
from modules.beeps import *
from modules.claw import *
from modules.variables import *
from modules.path import *
from pybricks.tools import StopWatch

crono = StopWatch()

obstaculos_lidos = []
 
#! Mudar isso na competição :D

#! ESSA POHA AQUI #FALSE é pro ALIGN
# TO BE ladinho e TRUE para entrar

dar_pra_tras = False 

#!------------------------------------------------------------------

#! EQUAÇÂO PARA CALCULO DAS DISTANCIAS EM GRAUS 

def cm_to_angle(distancia_em_cm):
    return ((distancia_em_cm * 3398)/124)

#! -----------------------------------------------------------------

def alinhar_com_obstaculo():
    valores_lidos = []
    while len(valores_lidos) < 10:
        valores_lidos.append(ultrasound_sensor.distance())
    while (sum(valores_lidos)/len(valores_lidos)) < 135:
        andar_reto(-500)
        valores_lidos.pop(0)
        valores_lidos.append(ultrasound_sensor.distance())
    brake_motors()
    
    valores_lidos = []
    while len(valores_lidos) < 10:
        valores_lidos.append(ultrasound_sensor.distance())
    while (sum(valores_lidos)/len(valores_lidos)) < 135:
        andar_reto(150)
        valores_lidos.pop(0)
        valores_lidos.append(ultrasound_sensor.distance())
    brake_motors()
    
def entregar_tubos():
    while not is_yellow():
        andar_reto(200)
        if (is_black_left() and is_yellow_right()) or (is_yellow_right() and is_black_left()):
            brake_motors()
            move_backward(6,800)
            print("vou virar")
            turn_left_pid(90,360) #! Ajustar o valor
            print("Virei")
            move_backward(3,800)
            turn_right_pid(90,360)
        elif (is_black_right() and is_yellow_left()) or (is_yellow_left() and is_black_right()):
            brake_motors()
            move_backward(6,800)
            turn_right_pid(90,360)
            move_backward(3,800)
            turn_left_pid(90,360)
        
    print("Teste 2")
    brake_motors()
    Open()
    move_forward(5,80)
    # Volta
    while not is_yellow_left() and not is_yellow_right():
        andar_reto(-300)
    brake_motors()
    ajust_color("YELLOW")    
    
    move_backward(5)

# ! teste de entregar tubos HILARIO E BIANCA (INSPIRED BY MEXICANS)

def reposition():
    brake_motors()
    left = True
    right = True
    count_l = 0
    count_r = 0

    while is_black_left() or is_black_right() or is_yellow_left() or is_yellow_right():
        move_backward(1)
        
    brake_motors()
    while not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right():
        #print("COUNT LL ", count_l, "    COUNT RRR   ", count_r)
        if left and not right :
            count_l += 1
        if right and not left :
            count_r += 1
        if (not is_white_left()) and left:
            while is_white_right():
                left_motor.hold()
                left_motor.stop()
                right_motor.run(60)
                left_motor.run(-3)
            left = False
            brake_motors()
            break
        if (not is_white_right()) and right:
            while is_white_left():
                right_motor.hold()
                right_motor.stop()
                left_motor.run(60)
                right_motor.run(-3)
            right = False
            brake_motors()
            break

        if right and left:
            andar_reto(100)
        if not right and not left:
            brake_motors()
            #print("PORRAAAAAA")
            
            return 0
        




def entregar_tubos2():
    while not is_yellow():
        andar_reto(200)
        if is_black_left() and is_yellow_right():
            brake_motors()
            move_backward(6,800)
            print("vou virar")
            motors.turn(20)
            brake_motors_para_drive_base()#! Ajustar o valor
            print("Virei")
            while not is_black_left() and not is_yellow_left():
                andar_reto(100)
            brake_motors()
            reposition()
        elif is_black_right() and is_yellow_left():
            brake_motors()
            move_backward(6,800)
            motors.turn(-20)
            brake_motors_para_drive_base()
            print("Virei")
            while not is_black_right() and not is_yellow_right():
                andar_reto(100)
            brake_motors()
            reposition()
    print("Teste 2")
    brake_motors()
    # Open()
    move_forward(5,80)
    # Volta
    while not is_yellow_left() and not is_yellow_right():
        andar_reto(-300)
    brake_motors()
    ajust_color("YELLOW")  
    
    move_backward(5)   

    
#! Localizações ----------------------------------------------------

#* Essas funções são sobre, ir do checkpoint e caminhar até o obstáculo

def go_to_i(angulo_que_ja_andou, velocidade = 200): #! 35 CM
    move_forward(7,250) #FAZER
    branco = range_white_left()[0] 
    azul = range_blue_left()[0] 
    threshold = (branco + azul) / 2
    if (cm_to_angle(35) - angulo_que_ja_andou) < 400 and (cm_to_angle(35) - angulo_que_ja_andou) > -400:
        move_backward(13)
        angulo_que_ja_andou -= cm_to_angle(13)
    if (cm_to_angle(35) - angulo_que_ja_andou) > 0:
        while left_motor.angle() < (cm_to_angle(35) - angulo_que_ja_andou) and right_motor.angle() < (cm_to_angle(35) - angulo_que_ja_andou):
            delta = red_left() - threshold
            kp = -0.75
            erro = delta * kp
            if (cm_to_angle(35) - angulo_que_ja_andou) < 400 and (cm_to_angle(35) - angulo_que_ja_andou) > -400:
                velocidade = 100
            motors.drive(velocidade, erro)
        brake_motors_para_drive_base()
        brake_motors()#!
        turn_right_pid(90)
    else:
        turn_180()
        while left_motor.angle() < -(cm_to_angle(35) - angulo_que_ja_andou) and right_motor.angle() < -(cm_to_angle(35) - angulo_que_ja_andou):
            delta = threshold - red_right()
            kp = -0.75
            erro = delta * kp
            if (cm_to_angle(35) - angulo_que_ja_andou) < 400 and (cm_to_angle(35) - angulo_que_ja_andou) > -400:
                velocidade = 100
            motors.drive(velocidade, erro)
        brake_motors_para_drive_base()
        brake_motors()#!
        turn_left_pid(90)

def go_to_j(angulo_que_ja_andou, velocidade = 200): #! 95 CM
    move_forward(7,250) #FAZER
    branco = range_white_left()[0] 
    azul = range_blue_left()[0] 
    threshold = (branco + azul) / 2 
    if (cm_to_angle(95) - angulo_que_ja_andou) < 400 and (cm_to_angle(95) - angulo_que_ja_andou) > -400:
        move_backward(13)
        angulo_que_ja_andou -= cm_to_angle(13)
    if (cm_to_angle(95) - angulo_que_ja_andou) > 0:
        while left_motor.angle() < (cm_to_angle(95) - angulo_que_ja_andou) and right_motor.angle() < (cm_to_angle(95) - angulo_que_ja_andou):
            delta = red_left() - threshold
            kp = -0.75
            erro = delta * kp
            if (cm_to_angle(95) - angulo_que_ja_andou) < 400 and (cm_to_angle(95) - angulo_que_ja_andou) > -400:
                velocidade = 100
            motors.drive(velocidade, erro)
        brake_motors_para_drive_base()#!
        turn_right_pid(90)
    else:
        turn_180()
        while left_motor.angle() < -(cm_to_angle(95) - angulo_que_ja_andou) and right_motor.angle() < -(cm_to_angle(95) - angulo_que_ja_andou):
            delta = red_right() - threshold
            kp = 0.75
            erro = delta * kp
            if (cm_to_angle(95) - angulo_que_ja_andou) < 400 and (cm_to_angle(95) - angulo_que_ja_andou) > -400:
                velocidade = 100
            motors.drive(velocidade, erro)
        brake_motors_para_drive_base()#!
        turn_left_pid(90)

#* Teve obstáculo essa função faz voltar na linha azul até a área de encontro

def j_to_i(velocidade = 150):
    branco = range_white_right()[0] 
    azul = range_blue_right()[0] 
    threshold = (branco + azul) / 2  
    
    while left_motor.angle() < 1640 or right_motor.angle() < 1640:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(velocidade, erro)
    
def i_to_j(velocidade = 150):
    branco = range_white_left()[0]
    azul = range_blue_left()[0]
    threshold = (branco + azul) / 2  
    
    while left_motor.angle() < 1640 or right_motor.angle() < 1640:
        delta = threshold - red_left()
        kp = 0.5
        erro = delta * kp
        motors.drive(velocidade, erro)

#* Funções para avançar até o obstáculo

def move_to_i_or_j(distancia = 20): # Colado no azul indo pro obstáculo
    while left_motor.angle() < cm_to_angle(distancia) and right_motor.angle() < cm_to_angle(distancia) and not has_obstacle():
        andar_reto(500)
    brake_motors()
    
def move_to_e_or_d(distancia = 62): # Colado no azul até o "D" ou o "E"
    while left_motor.angle() < cm_to_angle(distancia) and right_motor.angle() < cm_to_angle(distancia) and not has_obstacle():
        andar_reto(500)
    brake_motors()

def move_to_middle(distancia = 72): # Colado no azul até o meio da arena "F", "G" e "H"
    while left_motor.angle() < cm_to_angle(distancia) and right_motor.angle() < cm_to_angle(distancia) and not has_obstacle():
        andar_reto(500)
    brake_motors()

def i_or_j_to_middle(distancia = 53): # De frente com o I ou o J até o meio
    while left_motor.angle() < cm_to_angle(distancia) and right_motor.angle() < cm_to_angle(distancia) and not has_obstacle():
        andar_reto(500)
    brake_motors()
    
def middle_to_obstacle(distancia = 10): #!          No meio da arena para andar até o obstáculo
    while left_motor.angle() < cm_to_angle(distancia) and right_motor.angle() < cm_to_angle(distancia) and not has_obstacle():
        andar_reto(500)
    brake_motors()

#! -------------------------------------------------------------------------------------------------------


# Função recursiva para achar a linha azul (ida ou volta) ----------------------------------------

def find_blue_line(numero_de_paredes):
    esquerda_direita = ["ESQUERDA", 1]
    if numero_de_paredes == 0:
        se_alinhou = False
        vai_se_alinhar = False
    if numero_de_paredes < 4:
        brake_motors()
        
        cor_vista = ""
        
        print("procurando")
        while not is_blue_left() and not is_blue_right() and not is_black_left() and not is_black_right() and not is_yellow_left() and not is_yellow_right() and not is_red_left() and not is_red_right() and not has_obstacle():
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
            while not is_blue_left() and not is_blue_right():
                andar_reto(500)
                if (is_black_left() or is_black_right()) or (is_yellow_left() or is_yellow_right()) or is_wall():
                    brake_motors()
                    cor_vista = "BLACK"
                    ajust_color(cor_vista)
                    turn_180()
                elif has_obstacle():
                    found_wall()
                    brake_motors()
                    alinhar_com_obstaculo()
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
                            alinhar_com_obstaculo()
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
                            while not is_blue_left() and not is_blue_right():
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
                                    alinhar_com_obstaculo()
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
                        while not is_blue_left() and not is_blue_right() and not is_red_left() and not is_red_right() and not has_obstacle() and not is_black_left() and not is_black_right():
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
                            alinhar_com_obstaculo()
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
                            while not is_blue_left() and not is_blue_right():
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
                                    alinhar_com_obstaculo()
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
            move_forward(1,100)
            if is_black_left() or is_black_right() or is_yellow_left() or is_yellow_right():
                brake_motors()
                if ((is_black_left() or is_yellow_left()) and is_white_right()) or (is_white_left() and (is_black_right() or is_yellow_right())):
                    vai_se_alinhar = True
                move_backward(1,100)
                while left_motor.angle() > (-time_forward[0] + 10) or right_motor.angle() > (-time_forward[1] + 10):
                    andar_reto(-500)
                brake_motors()
                if se_alinhou == False and vai_se_alinhar == True:
                    turn_left_pid(45)
                se_alinhou = True
            elif has_obstacle():
                found_wall()
                alinhar_com_obstaculo()
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
    while True: 
        delta = threshold - red_left()
        kp = 0.5
        erro = delta * kp
        motors.drive(150, erro)
        if is_red_right():
            brake_motors_para_drive_base()
            break
        
    brake_motors_para_drive_base()
    brake_motors()
    
    move_backward(8)
    turn_right_pid(90)
    
    move_forward(5)
    entregar_tubos()
    
    

    if dar_pra_tras == True:
        turn_left_pid(90)
        move_backward(13)
        turn_left_pid(90)
        find_blue_line(0)
        
    if dar_pra_tras == False:
        turn_180()
        find_blue_line(0)
        
    
def tube_city_hall():
    global obstaculos_lidos
    
    move_to_i_or_j()
    
    if has_obstacle() or "J" in obstaculos_lidos:
        if "J" not in obstaculos_lidos:
            obstaculos_lidos.append("J") 
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
        else:
            move_forward(20)
        turn_left_pid(90)
        move_backward(3)
        
        
        entregar_tubos()
        turn_left_pid(90)
        find_blue_line(0)
        brake_motors()
    
    else:
        not_found_wall()
        move_forward(20)
        turn_right_pid(90)
        move_backward(3)
        # wait(500)
        # move_forward(3)
        
        entregar_tubos()
        
        turn_right_pid(90)
        
        find_blue_line(0)
        brake_motors()
        

    
def tube_school():
    global obstaculos_lidos

    move_to_i_or_j()
    
    if has_obstacle() or "I" in obstaculos_lidos: 
        if "I" not in obstaculos_lidos:
            obstaculos_lidos.append("I")
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
        else:
            i_or_j_to_middle()
            
        if "G" not in obstaculos_lidos:
            turn_right_pid(90)
        
            while left_motor.angle() < cm_to_angle(12) and right_motor.angle() < cm_to_angle(12) and not has_obstacle():
                andar_reto(500)
            brake_motors()
        
        if has_obstacle() or "G" in obstaculos_lidos: #"G"
            if "G" not in obstaculos_lidos:
                obstaculos_lidos.append("G")
                found_wall()
                alinhar_com_obstaculo()
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
            alinhar_com_obstaculo()
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

            entregar_tubos()
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
            
            entregar_tubos()
            
            
            turn_right_pid(90)
            while not is_red_left() and not is_red_right() and ultrasound_sensor.distance() > 145:
                andar_reto(500)
            brake_motors()
            if ultrasound_sensor.distance() < 145:
                alinhar_com_obstaculo()
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

        
        entregar_tubos()
        turn_right_pid(90)
        find_blue_line(0)
        
def tube_museum():
    global obstaculos_lidos
    

    move_to_i_or_j() 
    
    
    if has_obstacle() or "J" in obstaculos_lidos: 
        if "J" not in obstaculos_lidos:
            obstaculos_lidos.append("J")
            found_wall()
            alinhar_com_obstaculo()
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
        else:
            i_or_j_to_middle()
        
        if "G" not in obstaculos_lidos:
            turn_left_pid(90)
            middle_to_obstacle()
        
        if has_obstacle() or "G" in obstaculos_lidos: #"G"
            if "G" not in obstaculos_lidos:
                obstaculos_lidos.append("G")
                found_wall()
                alinhar_com_obstaculo()
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

            
            entregar_tubos()
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
                alinhar_com_obstaculo()
                
                turn_right_pid(90)
                move_forward(30)
                turn_left_pid(90)
                move_backward(3)
                #wait(500)
                #move_forward(3)
                
                entregar_tubos()
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
                move_backward(5) #middle_to_obstacle()
                turn_right_pid(90)
                move_backward(3)
                #wait(500)
                #move_forward(3)
                
                entregar_tubos()
                turn_right_pid(90)
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    found_wall()
                    alinhar_com_obstaculo()
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
            alinhar_com_obstaculo()
            turn_right_pid(90)
            move_forward(30)
            turn_left_pid(90)
            move_backward(3)

            
            entregar_tubos()
            #abre e retorna
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
           
            
            entregar_tubos()
            turn_left_pid(90)
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            move_backward(35)
            turn_left_pid(90)
            find_blue_line(0)
                
def tube_drugstore():
    global obstaculos_lidos
    

    move_to_i_or_j()
    
    if has_obstacle() or "J" in obstaculos_lidos or ("G" in obstaculos_lidos and "E" in obstaculos_lidos): 
        if "J" not in obstaculos_lidos and ("G" not in obstaculos_lidos or "E" not in obstaculos_lidos):
            obstaculos_lidos.append("J")
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
        else:
            i_or_j_to_middle()
        if "G" not in obstaculos_lidos:
            turn_left_pid(90)
            middle_to_obstacle()
        
        if has_obstacle() or "G" in obstaculos_lidos: #"G"
            if "G" not in obstaculos_lidos:
                obstaculos_lidos.append("G")
                found_wall()
                alinhar_com_obstaculo()
                turn_right_pid(90)
            
            while not is_black_left() or not is_black_right():
                andar_reto(500)
            brake_motors()
            
            
            cor_vista = "BLACK"
            ajust_color(cor_vista)
            
            move_backward(7)
            
            turn_left_pid(90)
            move_forward(35)
            turn_left_pid(90)
            move_backward(3)
            
            entregar_tubos()
            
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
            move_forward(18)
            turn_right_pid(90)
            move_backward(3)

            
            entregar_tubos()
            
            turn_right_pid(90)
            while not has_obstacle() and not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            if has_obstacle():
                found_wall()
                alinhar_com_obstaculo()
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
        if "G" not in obstaculos_lidos:
            turn_right_pid(90)
            middle_to_obstacle()
        if has_obstacle() or "G" in obstaculos_lidos: #"G" 
            if "G" not in obstaculos_lidos:
                obstaculos_lidos.append("G")
                found_wall()
                alinhar_com_obstaculo()
                turn_left_pid(90)
            middle_to_obstacle()
            if has_obstacle() or "E" in obstaculos_lidos: #"E"
                if "E" not in obstaculos_lidos:
                    obstaculos_lidos.append("E")
                found_wall()
                alinhar_com_obstaculo()
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
                move_backward(7)
                turn_left_pid(90)
                move_forward(28)
                turn_left_pid(90)
                move_backward(3)                
                entregar_tubos()
                
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
                move_forward(31)
                turn_right_pid(90)
                
                

                entregar_tubos()#!
                # move_backward(20)
                turn_right_pid(90)
                
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    found_wall()
                    alinhar_com_obstaculo()
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
            turn_left_pid(90)
            move_backward(3)

            
            entregar_tubos()
            
            # Open() 
            turn_right_pid(90)
            while not has_obstacle() and not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            if has_obstacle():
                found_wall()
                alinhar_com_obstaculo()
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
    global obstaculos_lidos
    
    move_to_i_or_j()
    
    if has_obstacle() or "I" in obstaculos_lidos or ("G" in obstaculos_lidos and "D" in obstaculos_lidos): 
        if "I" not in obstaculos_lidos:
            obstaculos_lidos.append("I")
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
        else:
            i_or_j_to_middle()
        
        if "G" not in obstaculos_lidos:
            turn_right_pid(90)
            
            middle_to_obstacle()
        
        if has_obstacle() or "G" in obstaculos_lidos: #"G"
            found_wall()
            alinhar_com_obstaculo()
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

            entregar_tubos()
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
                alinhar_com_obstaculo()
            else:
                not_found_wall()
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(36)
            if "D" not in obstaculos_lidos:
                turn_left_pid(90)
                middle_to_obstacle() # de frente pro D
            
            if has_obstacle() or "D" in obstaculos_lidos: #"D"
                if "D" not in obstaculos_lidos:
                    obstaculos_lidos.append("D")
                    found_wall()
                    alinhar_com_obstaculo()
                    turn_left_pid(90)
                else:
                    turn_180()
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
                #wait(500)
                #move_forward(3)
                
                entregar_tubos()
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
                #wait(500)
                #move_forward(3)
                
                entregar_tubos()
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
                    alinhar_com_obstaculo()
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
        if "D" not in obstaculos_lidos:
            middle_to_obstacle()
        
        if has_obstacle() or "D" in obstaculos_lidos: #"D"
            if "D" not in obstaculos_lidos:
                obstaculos_lidos.append("D")
                found_wall()
                alinhar_com_obstaculo()
                
            turn_left_pid(90)
            middle_to_obstacle()
            if has_obstacle():
                if "G" not in obstaculos_lidos:
                    obstaculos_lidos.append("G")
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
                #wait(500)
                #move_forward(3)
                
                entregar_tubos()
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
                #wait(500)
                #move_forward(3)
                
                entregar_tubos()
                turn_right_pid(90)
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    found_wall()
                    alinhar_com_obstaculo()
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

            
            entregar_tubos()
            turn_right_pid(90)
            find_blue_line(0)
    
def tube_park():
    global obstaculos_lidos
    
    
    move_to_i_or_j()
    
    if has_obstacle() or "J" in obstaculos_lidos: 
        if "J" not in obstaculos_lidos:
            obstaculos_lidos.append("J")
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
        else:
            i_or_j_to_middle()
        
        if "D" not in obstaculos_lidos:
            middle_to_obstacle()
        
        if has_obstacle() or "D" in obstaculos_lidos:
            if "D" not in obstaculos_lidos:
                obstaculos_lidos.append("D") 
                print("Tem objeto no D")
                found_wall()
                alinhar_com_obstaculo()
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

            
            entregar_tubos()
            move_backward(13)
            turn_left_pid(90)
            
            # Voltando agora
            
            while not is_red_left() and not is_red_right():
                andar_reto(500)
            brake_motors()
            cor_vista = "RED"
            ajust_color(cor_vista)
            move_backward(36)
            
            
            turn_left_pid(90) 
            
            
            alinhar_com_obstaculo()
            
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
                alinhar_com_obstaculo()
                turn_180()
                move_forward(28)
                turn_right_pid(90)
                move_backward(3)
                #wait(500)
                #move_forward(3)
                
                entregar_tubos()
                turn_right_pid(90)
                while ultrasound_sensor.distance() > 145:
                    andar_reto(500)
                brake_motors()
                alinhar_com_obstaculo()
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
                #wait(500)
                #move_forward(3)
                
                entregar_tubos()
                turn_left_pid(90)
                move_forward(29) 
                
                turn_left_pid(90)
                find_blue_line(0)
    else:
        not_found_wall()
        i_or_j_to_middle()
        wait(1000)
        if "E" not in obstaculos_lidos:
            middle_to_obstacle()
        
        if has_obstacle() or "E" in obstaculos_lidos:
            if "E" in obstaculos_lidos: 
                found_wall()
                alinhar_com_obstaculo()
            turn_right_pid(90)
            if "G" not in obstaculos_lidos:
                middle_to_obstacle()
            
            if has_obstacle():
                if "G" not in obstaculos_lidos: 
                    obstaculos_lidos.append("G")
                found_wall()
                alinhar_com_obstaculo()
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
                #wait(500)
                #move_forward(3)
                
                entregar_tubos()
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
                    alinhar_com_obstaculo()
                    turn_180()
                    move_forward(28)
                    turn_right_pid(90)
                    move_backward(3)
                    wait(500)
                    move_forward(3)
                    
                    entregar_tubos()
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
                   
                    
                    entregar_tubos()
                    turn_right_pid(90)
                    move_backward(29)
                    turn_right_pid(90)
                    while not has_obstacle() and not is_blue():
                        andar_reto(500)
                    brake_motors()
                    if has_obstacle():
                        found_wall()
                        alinhar_com_obstaculo()
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
                alinhar_com_obstaculo()
                turn_180()
                while not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                cor_vista = "RED"
                ajust_color(cor_vista)
                move_backward(7)
                turn_right_pid(90)
                move_backward(3)
                #wait(500)
                #move_forward(3)
                
                entregar_tubos()
                turn_left_pid(90)
                move_backward(29)
                turn_left_pid(90)
                
                find_blue_line(0)
            else:
                not_found_wall()
                move_forward(20)
                turn_left_pid(90)
                move_backward(3)
                #wait(500)
                #move_forward(3)
                
                entregar_tubos()
                turn_left_pid(90)
                while not has_obstacle() and not is_red_left() and not is_red_right():
                    andar_reto(500)
                brake_motors()
                if has_obstacle():
                    found_wall()
                    alinhar_com_obstaculo()
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
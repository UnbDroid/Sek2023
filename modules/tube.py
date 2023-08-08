def go_to_check_point():
     #Descendo pro SUL até a linha vermelha
    while not is_red():
        move_forward(1) # Ajustar!
        
    #Manobra
    turn_right()
    turn_right()

def tube_library():
    go_to_check_point()
    
    move_forward(1)    
    turn_left()
    move_forward(1)
    #Abre garra
    # retorna para a área de coleta
    
def tube_city_hall():
    
    go_to_check_point()
    
    move_forward(3)
    turn_left()
    move_forward(1) # Está indo em direção ao objeto J
    
    if has_obstacle(): #sensor identificou objeto "J":
        move_backward(1)
        turn_right()
        move_forward(3)
        turn_left()
        move_forward(2)
        turn_left()
        move_forward(2)
        #Abre a garra
        #retorna para a área de coleta
        move_backward(2)
        turn_left()
        move_forward(3)
    
    else:
        move_forward(2)#Distancia pequena
        turn_right()
        move_forward(2)
        #Abre a garra
        #retorna para a área de coleta
        move_backward(2)
        turn_right()
        move_forward(3)
        

    
def tube_school():
    go_to_check_point()
    
    move_forward(8)
    turn_left()
    move_forward(1)
    
    if has_obstacle(): #sensor identificou objeto "i":
        move_backward(1)
        turn_left()
        move_forward(4)
        turn_right()
        move_forward(4)
        turn_right()
        #while not is_red():
        #    move_forward(): sugestão, bater no vermelho e dai voltar
        move_forward(6)
        turn_right()
        move_forward(2)
        #abre e retorna
        move_backward(2)
        turn_right()
        move_forward(6)
        turn_left()
        move_forward(4)
    else:
        move_forward(1)
        move_right()
        move_forward(2)
        #abre e retorna
        move_backward(2)
        turn_right()
        move_forward(2)
        
def tube_museum():
    go_to_check_point()
    
    move_forward(4)
    turn_left()
    
    if has_obstacle(): #sensor identificou objeto "j":
        turn_right()
        move_forward(4)
        turn_left()
        move_forward(4)
        turn_left()
        move_forward(2)
        if has_obstacle(): #sensor identificou objeto G:
            move_backward(2)
            turn_right()
            move_forward(4)
            turn_left()
            move_forward(4)
            turn_left()
            move_forward(4)
            turn_right()
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_right()
            move_forward(4)
            turn_right()
            move_forward(4)
            turn_right()
            move_forward(8)
        else:
            move_forward(6)
            turn_right()
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_right()
            move_forward(2)
            turn_right()
            move_forward(4) 
    else:
        move_forward(4)
        turn_left()
    
    if has_obstacle(): #Objeto "H":
        turn_right()
        move_forward(2)
        turn_left()
        move_forward(2)
        # Abre e retorna
        move_backward(2)
        turn_left()
        move_forward(6)
    else:
        move_forward(2)
        turn_right()
        move_forward(2)
        # abre e retorna
        move_backward(2)
        turn_right()
        move_forward(2)
        turn_right()
        move_forward(6)
                
def tube_drugstore():
    go_to_check_point()
    
    move_forward(3)
    turn_left()
    
    if has_obstacle(): #Objeto "J":
        turn_right()
        move_forward(4)
        turn_left()
        move_forward(4)
        turn_left()
        
        if has_obstacle(): #Objeto "G":
            turn_right()
            move_forward(4)
            turn_left()
            move_forward(2)
            turn_left()
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_left()
            move_forward(3)
            turn_right()
            move_forward(8)
        else:    
            move_forward(2)
            turn_right()
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right()
            move_forward(3)
            turn_right()
            move_forward(4)
    else:
        move_forward(4)
        turn_right()
    
    if has_obstacle(): #Objeto "G":
        turn_left()
        if has_obstacle(): #Objeto "E":
            move_backward(5)
            turn_right()
            move_forward(4)
            turn_left()
            move_forward(9)
            turn_left()
            move_forward(3)
            turn_left()
            move_forward(2)
            #Abre e solta
            move_backward(2)
            turn_left()
            move_forward(3)
            turn_right()
            move_forward(9) 
        else:
            move_forward(4)
            turn_right()
            move_forward(2)
            turn_right()
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right()
            move_forward(3)
            turn_left()
            move_forward(8)
    else:
        move_forward(2)
        turn_left()
        move_forward(2)
        # Abre e retorna
        move_backward(2)
        turn_left()
        move_forward(2)
        turn_left()
        move_forward(5)
    

def tube_bakery()
    go_to_check_point()
    
    move_forward(7)
    turn_left()
    
    if has_obstacle(): #Objeto "I":
        turn_left()
        move_forward(5)
        turn_right()
        move_forward(4)
        if has_obstacle(): #objeto "E":
            turn_right()
            move_forward(4)
            turn_left()
            move_forward(2)
            turn_right()
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right()
            move_forward(3)
            turn_right()
            move_forward(4)
            turn_left()
            move_forward(4)
        else:
            move_forward(4)
            turn_right()
        
        if has_obstacle(): #OBJETO B"
            turn_right()
            move_forward(5)
            turn_left()
            move_forward(4)
            turn_left()
            move_forward(2)
            turn_right()
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_right()
            move_forward(3)
            turn_right()
            move_forward(4)
            turn_left()
            move_forward(4)
        else:
            move_forward(4)
        if has_obstacle(): #objeto "A":
            turn_right()
            move_forward(3)
            turn_left()
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right()
            move_forward(2)
            turn_right()
            move_forward(5)
            turn_left()
            move_forward(4)
        else:
            move_forward(2)
            turn_right()
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right()
            move_forward(6)
            turn_left()
            move_forward(8)
    else:
        move_forward(4)
    
    if has_obstacle(): #Objeto "D":
        turn_left()
        move_forward(1)
        if has_obstacle(): #Objeto "G":
            turn_left()
            move_forward(4)
            turn_right()
            move_forward(4)
            turn_right()
            move_forward(8)
            
        
        if has_obstacle(): #objeto "A":
            move_back()
            turn_right()
            move_forward()
            turn_left()
            move_forward()
            #Abre e retorna
        
        move_backward()
        turn_right()
        move_forward()
        turn_left()
        move_forward()        
        #Abre e retorna
    
    move_forward()
    turn_right()
    move_forward()
    #Abre e retorna
    
def tube_park():
    go_to_check_point()
    
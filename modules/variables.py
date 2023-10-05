from modules.colors import *

#! MUDE APENAS ISSO PRA COMPETIÇÃO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#! Range das cores 
def range_black_left():
    return [8, 9, 5]

def range_black_right():
    return [11, 10, 36]

def range_yellow_left():
    return [67, 70, 20]

def range_yellow_right():
    return [85, 82, 49]

def range_blue_left():
    return [8, 22, 42]

def range_blue_right():
    return [13, 30, 100]

def range_red_left():
    return [65, 10, 9]

def range_red_right():
    return [86, 22, 35]

def range_white_left():#
    return [69, 82, 90]

def range_white_right():
    return [91, 97, 100]

def get_dar_pra_tras(value):
    return value

def set_dar_pra_tras(value):
    return value





# ----------------------------------------------------------------------------------------------------------------------

def get_treshold_left_blue():
    return get_treshold_left("red", range_blue_left())

def get_treshold_right_blue():
    return get_treshold_right("red", range_blue_right())


#-----------------------------------------------------

def get_treshold_left_black():
    return get_treshold_left("red",range_black_left())

def get_treshold_right_black():
    return get_treshold_left("red",range_black_right())


def get_treshold_left_yellow():
    return get_treshold_left("blue",range_yellow_left())
def get_treshold_right_yellow():
    return get_treshold_left("blue",range_yellow_right())


def get_treshold_left_red():
    return get_treshold_left("green",range_red_left())

def get_treshold_right_red():
    return get_treshold_right("green",range_red_right())


def get_range_colors(lista,fator = 'max'):
    if fator == "max":
        for i in range(len(lista)):
            lista[i] += 15
    
    elif fator == "min":
        for i in range(len(lista)):
            lista[i] -= 15
            
    return lista

def get_treshold_left(pos,color,white = range_white_left()):
    if pos == "red":
        
        color_white_formula = white[0]
        color_formula = color[0]

        treshold = (color_formula + color_white_formula)//2
        return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
    
    elif pos == "green":
        
        color_white_formula = white[1]
        color_formula = color[1]
        
        treshold = ( color_formula + color_white_formula )//2
        return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
    
    elif pos == "blue":
        
        color_white_formula = white[2]
        color_formula = color[2]
        
        treshold = ( color_formula + color_white_formula )//2
        return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
    

def get_treshold_right(pos,color,white = range_white_right()):
    if pos == "red":
        
        color_white_formula = white[0]
        color_formula = color[0]

        treshold = (color_formula + color_white_formula)//2
        return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
    
    elif pos == "green":
        
        color_white_formula = white[1]
        color_formula = color[1]
        
        treshold = ( color_formula + color_white_formula )//2
        return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
    
    elif pos == "blue":
        
        color_white_formula = white[2]
        color_formula = color[2]
        
        treshold = ( color_formula + color_white_formula )//2
        return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
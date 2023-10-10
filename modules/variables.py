from modules.colors import *

#! MUDE APENAS ISSO PRA COMPETIÇÃO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#! Range das cores 
def range_black_left():
    # return [8, 9, 5] #! RANGES DA ARENA OFICIAL
    return [7, 9, 9]

def range_black_right():
    # return [11, 10, 36] #! RANGES DA ARENA OFICIAL
    return [13, 14, 33]

def range_yellow_left():
    # return [56, 66, 17] #! RANGES DA ARENA OFICIAL
    return [54, 65, 14]

def range_yellow_right():
    # return [72, 75, 45] #! RANGES DA ARENA OFICIAL
    return [81, 81, 55]

def range_blue_left():
    # return [13, 17, 40] #! RANGES DA ARENA OFICIAL
    return [9, 15, 36]

def range_blue_right():
    # return [20, 22, 100] #! RANGES DA ARENA OFICIAL
    return [17, 22, 100]

def range_meio_blue_left():
    return [(range_white_left()[0] + range_blue_left()[0])//2, (range_white_left()[1] + range_blue_left()[1])//2, (range_white_left()[2] + range_blue_left()[2])//2]

def range_meio_blue_right():
    return [(range_white_right()[0] + range_blue_right()[0])//2, (range_white_right()[1] + range_blue_right()[1])//2, (range_white_right()[2] + range_blue_right()[2])//2]

def range_red_left():
    # return [69, 9, 11] #! RANGES DA ARENA OFICIAL
    return [65, 8, 9]

def range_red_right():
    # return [87, 16, 47] #! RANGES DA ARENA OFICIAL
    return [92, 18, 45]

def range_white_left():
    # return [68, 83, 100] #! RANGES DA ARENA OFICIAL
    return [67, 82, 98]

def range_white_right():
    # return [82, 89, 100] #! RANGES DA ARENA OFICIAL
    return [92, 97, 100]

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
        return [treshold-6,treshold-6,treshold-5,treshold-4,treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3,treshold+4,treshold+5,treshold+6,treshold+6]
    
    elif pos == "green":
        
        color_white_formula = white[1]
        color_formula = color[1]
        
        treshold = ( color_formula + color_white_formula )//2
        return [treshold-6,treshold-5,treshold-4,treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3,treshold+4,treshold+5,treshold+6]
    
    elif pos == "blue":
        
        color_white_formula = white[2]
        color_formula = color[2]
        
        treshold = ( color_formula + color_white_formula )//2
        return [treshold-6,treshold-5,treshold-4,treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3,treshold+4,treshold+5,treshold+6]
    

def get_treshold_right(pos,color,white = range_white_right()):
    if pos == "red":
        
        color_white_formula = white[0]
        color_formula = color[0]

        treshold = (color_formula + color_white_formula)//2
        return [treshold-6,treshold-5,treshold-4,treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3,treshold+4,treshold+5,treshold+6]
    
    elif pos == "green":
        
        color_white_formula = white[1]
        color_formula = color[1]
        
        treshold = ( color_formula + color_white_formula )//2
        return [treshold-6,treshold-5,treshold-4,treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3,treshold+4,treshold+5,treshold+6]
    
    elif pos == "blue":
        
        color_white_formula = white[2]
        color_formula = color[2]
        
        treshold = ( color_formula + color_white_formula )//2
        return [treshold-6,treshold-5,treshold-4,treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3,treshold+4,treshold+5,treshold+6]
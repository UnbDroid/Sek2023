from modules.colors import *

# MUDE APENAS ISSO PRA COMPETIÇÃO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def range_black_left():
    return [8, 9, 5]

def range_black_right():
    return [11, 10, 36]

def range_yellow_left():
    return [67, 70, 20]

def range_yellow_right():
    return [85, 82, 49]

def range_blue_left():
    return [8, 22, 44]

def range_blue_right():
    return [12, 29, 100]

def range_red_left():
    return [65, 10, 9]

def range_red_right():
    return [86, 22, 35]

def range_white_left():
    return [69, 82, 90]

def range_white_right():
    return [91, 97, 100]




# ----------------------------------------------------------------------------------------------------------------------




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
    
    
'''
class Treshold():
        
    def __init__(self, white_left = [97, 95, 100], white_right = [93, 96, 100]):
        self.white_left = white_left
        self.white_right = white_right
        
    def get_treshold_left(self, color,pos):
    
        if pos == "red":
            treshold = ( color[0] + self.white_left[0] )//2
            return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
            
        elif pos == "green":
            treshold = ( color[1] + self.white_left[1] )//2
            return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
            
        elif pos == "blue":
            treshold = ( color[2] + self.white_left[2] )//2
            return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
        
    def get_treshold_right(self, color,pos):
        
        if pos == "red":
            treshold = ( color[0] + self.white_right[0] )//2
            return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
        
        elif pos == "green":
            treshold = ( color[1] + self.white_right[1] )//2
            return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
        
        elif pos == "blue":
            treshold = ( color[2] + self.white_right[2] )//2
            return [treshold-3,treshold-2,treshold-1,treshold,treshold+1,treshold+2,treshold+3]
            
    
treshold = Treshold()
vermelho_left = treshold.get_treshold_left([92, 19, 22],"green")
print("isso é um teste do pedro",vermelho_left)
'''


     
        
        
          
          
      

# teste
# def get_treshold_colors(color, white, pos):
#     treshold = [0,0,0]
#     for i in range(len(color)):
#         treshold[i] += ((color[i]+white[i]) // 2 )
    
    
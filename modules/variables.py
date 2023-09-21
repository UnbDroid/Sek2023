# Variaveis de motors para o ajust color!
#Tresholds para as cores | Diferença entra a cor e o branco, mas
 

def get_treshold_left_black():
    return [51,52,53]
def get_treshold_right_black():
    return [49,50,51]


def get_treshold_left_yellow():
    return [68,69,70]
def get_treshold_right_yellow():
    return [68,69,70]

# Esquerda:  (92, 19, 22) Direita:  (88, 22, 34)
# Esquerda:  (97, 95, 100) Direita:  (93, 96, 100)
def get_treshold_left_red():
    return [54,55,56]
def get_treshold_right_red():
    return [58,59,60]


def get_range_colors(lista,fator='max'):
    if fator == "max":
        for i in range(len(lista)):
            lista[i] += 15
    
    elif fator == "min":
        for i in range(len(lista)):
            lista[i] -= 15
            
    return lista

# teste
# def get_treshold_colors(color, white, pos):
#     treshold = [0,0,0]
#     for i in range(len(color)):
#         treshold[i] += ((color[i]+white[i]) // 2 )
    
    
# Variaveis de motors para o ajust color!
#Tresholds para as cores | Diferença entra a cor e o branco, mas
 

def get_treshold_left_black():
    return [49,50,51,52,53,54,55]
def get_treshold_right_black():
    return [47,48,49,50,51,52,53]


def get_treshold_left_yellow():
    return [66,67,68,69,70,71,72]
def get_treshold_right_yellow():
    return [66,67,68,69,70,71,72]

# Esquerda:  (92, 19, 22) Direita:  (88, 22, 34)
# Esquerda:  (97, 95, 100) Direita:  (93, 96, 100)
def get_treshold_left_red():
    return [52,53,54,55,56,57,58]
def get_treshold_right_red():
    return [56,57,58,59,60,61,62]


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
    
    
from pybricks.ev3devices import ColorSensor                                
from pybricks.parameters import Port, Color


tube_sensor_verification = ColorSensor(Port.S3)
# scan_sensor = ColorSensor(Port.S2)
tube_presence_verificator = ColorSensor(Port.S4)

# Teste de sensor de cor 




def tube():
    verification = tube_sensor_verification.reflection()
    if verification >= 5:
        print("Tube is 15cm high")
        return True
    else:
        print("Tube is 10cm tall")
        return False


def tube_scan():
    verification = scan_sensor.reflection()
    if verification != 1:
        print("Tem um tubo ai rapaz!")
        
    else:
        print("To vendo nada não chefe!")
        
        # (50+72)/2
        
def tube_is_detected():
    if tube_presence_verificator.reflection() >= 8 or (tube_presence_verificator.rgb()[0] >= 2 and tube_presence_verificator.rgb()[1] >=3):
        return True
    else:
        return False
        
def alinhar_azul():
    # print(andar_linha.rgb())
    branco = 67
    azul = 38
    treshold = (branco + azul)//2
    cor = andar_linha.rgb()[0]
    return str(treshold - cor)
    # azul = cor[2]
    # azul = int(azul)
    
    
from pybricks.nxtdevices import ColorSensor                                
from pybricks.parameters import Port, Color
from pybricks.ev3devices import UltrasonicSensor

tube_sensor_verification = ColorSensor(Port.S3)
andar_linha = ColorSensor(Port.S4)

ultrasound = UltrasonicSensor(Port.S2)



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
        print("To vendo nada não chefe!")
        
        # (50+72)/2
        
def alinhar_azul():
    # print(andar_linha.rgb())
    branco = 67
    azul = 38
    treshold = (branco + azul)//2
    cor = andar_linha.rgb()[0]
    return str(treshold - cor)
    # azul = cor[2]
    # azul = int(azul)
    
def scan_de_ladinho():
    if ultrasound.distance() >=25 and  ultrasound.distance() <=75:
        return True
    else:
        return False
    
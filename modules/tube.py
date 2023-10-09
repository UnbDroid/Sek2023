from pybricks.nxtdevices import ColorSensor                                
from pybricks.parameters import Port, Color
from pybricks.ev3devices import UltrasonicSensor

tube_sensor_verification = ColorSensor(Port.S3)
tube_presence_verificator = ColorSensor(Port.S4)

# ultrasound = UltrasonicSensor(Port.S2)



def tube():
    verification = tube_sensor_verification.reflection()
    if verification >= 10:
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
    
# def scan_de_ladinho():
#     if ultrasound.distance() <= 200:
#         return True
#     else:
#         return False
    
def red_tube():
    return [85, 21, 20]

def blue_tube():
    return [55, 68, 76]

def green_tube():
    return [49, 76, 57]
    
def color_tube():
    if tube_presence_verificator.rgb()[0] >= (red_tube()[0] - 15) and tube_presence_verificator.rgb()[0] <= (red_tube()[0] + 15) and tube_presence_verificator.rgb()[1] >= (red_tube()[1] - 15) and tube_presence_verificator.rgb()[1] <= (red_tube()[1] + 15) and tube_presence_verificator.rgb()[2] >= (red_tube()[2] - 15) and tube_presence_verificator.rgb()[2] <= (red_tube()[2] + 15):
        return "RED"
    elif tube_presence_verificator.rgb()[0] >= (green_tube()[0] - 15) and tube_presence_verificator.rgb()[0] <= (green_tube()[0] + 15) and tube_presence_verificator.rgb()[1] >= (green_tube()[1] - 15) and tube_presence_verificator.rgb()[1] <= (green_tube()[1] + 15) and tube_presence_verificator.rgb()[2] >= (green_tube()[2] - 15) and tube_presence_verificator.rgb()[2] <= (green_tube()[2] + 15):
        return "GREEN"
    elif tube_presence_verificator.rgb()[0] >= (blue_tube()[0] - 15) and tube_presence_verificator.rgb()[0] <= (blue_tube()[0] + 15) and tube_presence_verificator.rgb()[1] >= (blue_tube()[1] - 15) and tube_presence_verificator.rgb()[1] <= (blue_tube()[1] + 15) and tube_presence_verificator.rgb()[2] >= (blue_tube()[2] - 15) and tube_presence_verificator.rgb()[2] <= (blue_tube()[2] + 15):
        return "BLUE"
    else:
        color_tube()

def tube_is_detected():
    count = 0
    while count < 5:
        if tube_presence_verificator.reflection() >= 20:
            return True
        count += 1
    return False
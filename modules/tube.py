from pybricks.nxtdevices import ColorSensor                                
from pybricks.parameters import Port, Color


tube_sensor_verification = ColorSensor(Port.S3)
# scan_sensor = ColorSensor(Port.S2)
tube_presence_verificator = ColorSensor(Port.S4)

# Teste de sensor de cor 




def tube_is_15():
    verification = tube_sensor_verification.reflection()
    if verification >= 5:
        print("Tube is 15cm high")
        return True
    else:
        print("Tube is 10cm tall")
        return False
        
        # (50+72)/2
        
def tube_is_detected():
    if tube_presence_verificator.reflection() >= 8 or (tube_presence_verificator.rgb()[0] >= 2 and tube_presence_verificator.rgb()[1] >=3):
        return True
    else:
        return False
    
def color_tube():
    if tube_presence_verificator.rgb()[0] >= (tube_presence_verificator.rgb()[1] + tube_presence_verificator.rgb()[2]):
        return "RED"
    elif tube_presence_verificator.rgb()[1] >= (tube_presence_verificator.rgb()[0] + tube_presence_verificator.rgb()[2]):
        return "GREEN"
    elif tube_presence_verificator.rgb()[2] >= (tube_presence_verificator.rgb()[0] + tube_presence_verificator.rgb()[1]):
        return "BLUE"
    else:
        return "BROWN"
from pybricks.nxtdevices import ColorSensor                                
from pybricks.parameters import Port

tube_sensor_verification = ColorSensor(Port.S2)

def tube():
    tube_sensor_verification.reflection()
    
    if tube_sensor_verification.reflection() >= (50/100):
        print("Tube is hight 15")
        return True
    else:
        print("Tube is low 10")
        return False
    
def hight_tube():
    key = ''
    
    if tube() == True:
        return key = '15'
    
    else:
        return key = '10'
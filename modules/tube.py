from pybricks.nxtdevices import ColorSensor                                
from pybricks.parameters import Port

tube_sensor_verification = ColorSensor(Port.S3)
scan_sensor = ColorSensor(Port.S4) # Teste de sensor de cor 




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
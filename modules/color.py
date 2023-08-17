from pybricks.nxtdevices import ColorSensor                                
from pybricks.parameters import Port

color_verification = ColorSensor(Port.S1)

def tube_color():
    return color_verification.rgb()

# ----------------------------------------------------------------------------------------------------------
range_max_blue = [0,0,0]
range_min_blue = [0,0,0]



def red_tube():
    sensor_r = (range_min_blue[0] < tube_color()[0] < range_max_blue[0])
    sensor_g = (range_min_blue[1] < tube_color()[1] < range_max_blue[1])
    sensor_b = (range_min_blue[2] < tube_color()[2] < range_max_blue[2])
    
    return sensor_r and sensor_g and sensor_b

# ----------------------------------------------------------------------------------------------------------
    


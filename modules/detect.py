from pybricks.ev3devices import ColorSensor
# from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
# from modules.colors import *

tube_verificator = ColorSensor(Port.S4)

# ultrasound_sensor = UltrasonicSensor(Port.S3)

# def has_obstacle():
#     return ultrasound_sensor.distance() < 200

# def is_tube_of_15():
#     return color_sensor_right_lower.reflection() > 1 and color_sensor_right_upper.reflection() > 1

# def is_tube_of_10():
#     return color_sensor_right_lower.reflection() > 1 and color_sensor_right_upper.reflection() < 1

# def is_red_tube():
#     return color_sensor_right_lower.rgb()[0] > 10 and color_sensor_right_lower.rgb()[1] < 10 and color_sensor_right_lower.rgb()[2] < 10

# def is_green_tube():
#     return color_sensor_right_lower.rgb()[0] < 10 and color_sensor_right_lower.rgb()[1] > 10 and color_sensor_right_lower.rgb()[2] < 10

# def is_blue_tube():
#     return color_sensor_right_lower.rgb()[0] < 10 and color_sensor_right_lower.rgb()[1] < 10 and color_sensor_right_lower.rgb()[2] > 10

# def is_brown_tube():
#     return color_sensor_right_lower.rgb()[0] > 10 and color_sensor_right_lower.rgb()[1] > 10 and color_sensor_right_lower.rgb()[2] < 10
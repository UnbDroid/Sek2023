from pybricks.hubs import EV3Brick
ev3 = EV3Brick()

def found_door():
    ev3.speaker.beep(100, 1000)
    
def found_wall():
    ev3.speaker.beep(1000, 1000)
    
def not_found_wall():
    ev3.speaker.beep(100, 1000)
    
def alined_to_wall():
    ev3.speaker.beep(100, 1000)

    
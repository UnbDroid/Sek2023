from pybricks.hubs import EV3Brick
ev3 = EV3Brick()

def found_door():
    ev3.speaker.beep(100, 1000)
    
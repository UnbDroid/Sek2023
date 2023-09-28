#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

print('1')
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
print("2")
from modules.tube import *

SERVER = 'ev3dev'
print("3")
client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')

while True:
    mbox.wait()
    msg = mbox.read()
        
    if msg == "chave":
        wait(50)
        if tube_is_15() == True:
            mbox.send('15')
        else:
            mbox.send('10')

    elif msg == 'tem tubo?':
        if tube_is_detected() == True:
            mbox.send('tem tubo')
        else:
            mbox.send('nao tem tubo')
            
    elif msg == 'cor do tubo':
        mbox.send(color_tube())

# while True:
#     print(tube_presence_verificator.rgb())
    
#RED
#BLUE
#GREEN
#BROWN
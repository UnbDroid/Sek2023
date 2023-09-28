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
    
    if msg == 'alinhar':
        wait(50)
        mbox.send(alinhar_azul())
        
    elif msg == "chave":
        wait(50)
        if tube() == True:
            mbox.send('15')
        else:
            mbox.send('10')
    
    elif msg == "de_ladinho":
        wait(50)
        if scan_de_ladinho() == True:
            mbox.send('Vi tubo')
        else:
            mbox.send('Sem tubo')
        
    elif msg == "tem tubo?":
        wait(50)
        if tube_is_detected():
            mbox.send("tem tubo")
        else:
            mbox.send("nao tem tubo")
         
    elif msg == "scan":
        wait(50)
        tube_scan()

#!/usr/bin/env pybricks-micropython


<<<<<<< HEAD
=======
# The server must be started before the client!
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

>>>>>>> 650fa7e5dd036a27c7e6f25bee8ad96864b45593
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
        if tube() == True:
            mbox.send('15')
        else:
            mbox.send('10')
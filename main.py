#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!
print('1')
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
print("2")
from modules.tube import *

SERVER = 'ev3dev'
print("3")
server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

print('waiting for connection...')
server.wait_for_connection()
print('connected!')

mbox.wait()
msg = mbox.read()
if msg == "chave":
    if tube() == True:
        mbox.send('15')
    else:
        mbox.send('10')
#!/usr/bin/env pybricks-micropython


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
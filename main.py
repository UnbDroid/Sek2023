#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# O nome do servidor deve ser o mesmo que o nome do servidor no programa do servidor.
SERVER = 'ev3dev'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

# Testes para vermos se realmente está conectando.
print('establishing connection...')
client.connect(SERVER)
print('connected!')

# In this program, the client sends the first message and then waits for the
# server to reply.
mbox.send('hello!')
mbox.wait()
print(mbox.read())

send_code = ''

if red_tube() = True:
    send_code = 'red '

if hight_tube() = True:
    send_code = send_code + hight_tube()

print(send_code)
mbox.send('send_code')
mbox.wait()
print(mbox.read())
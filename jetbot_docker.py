import socket
from jetbot import Robot
import time

# take the server name and port name

host = 'ip' #write the ip address of server on which camera is to connect
port = 5000
robot = Robot()
# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port 
# number on local computer.
s.connect((host, port))

# receive message string from
# server, at a time 1024 B
msg = s.recv(1024)

# repeat as long as message
# string are not empty
while msg:
    message = msg.decode()
    print('Received: ' + message)
    if msg == 'left':
        robot.left_motor.value = 0.3
        robot.right_motor.value = 0.6
        time.sleep(1.0)
        robot.left_motor.value = 0.3
        robot.right_motor.value = 0.3
        time.sleep(0.5)
        robot.stop()     
    elif msg == 'right':
        robot.left_motor.value = 0.6
        robot.right_motor.value = 0.3
        time.sleep(1.0)
        robot.left_motor.value = 0.3
        robot.right_motor.value = 0.3
        time.sleep(0.5)
        robot.stop() 
    elif msg == 'spin':
        robot.left_motor.value = 0.6
        robot.right_motor.value = 0
        time.sleep(2.0)
        robot.stop()
    elif msg == 'forward':
        robot.forward(.3)
#         time.sleep(1)
#         robot.stop()
    elif msg == 'backward':
        robot.backward(.3)
    elif msg == 'stop':
        robot.stop()
    elif msg == 'uturn':
        robot.forward(0.3)
        time.sleep(0.5)
        robot.left_motor.value = 0.3
        robot.right_motor.value = 0.6
        time.sleep(1.0)
        robot.left_motor.value = 0.3
        robot.right_motor.value = 0.3
        time.sleep(0.5)
        robot.left_motor.value = 0.3
        robot.right_motor.value = 0.6
        time.sleep(1.0)
        robot.left_motor.value = 0.3
        robot.right_motor.value = 0.3
        time.sleep(0.5)
        robot.stop()
    else:
        robot.stop()
    msg = s.recv(1024)
    

# disconnect the client
s.close()

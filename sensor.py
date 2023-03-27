# Imports go at the top
from microbit import *
from Micro_Carmona import *


robot = Micro_Rover()

while True:
    distancia = robot.get_distance()
    if distancia<=10:
        robot.motor(-255,-255)
        sleep(1000)
        robot.motor(0,255)
    else:
        robot.motor(255,255)

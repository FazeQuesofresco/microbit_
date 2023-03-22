# Imports go at the top
from microbit import *
from MicroPedro import *

robot=Micro_Rover()
while True:
    sensor = robot.infrared_sensor_value()
    display.show(sensor)

    if sensor == 7:
        robot.motor(0,0)
    else:
        robot.motor(255,255)

from microbit import *
from MicroRover import *

robot = Micro_Rover()

while True:
    sensor = robot.infrared_sensor_value()
    display.show(sensor)
    if sensor == 2:
        robot.motor(255,255)
    elif sensor == 4:
        robot.motor(0,150)
    elif sensor == 6:
        robot.motor(0,50)
    elif sensor == 1:
        robot.motor(150,0)
    elif sensor == 3:
        robot.motor(50,0)
    else:
        robot.motor(255,255)

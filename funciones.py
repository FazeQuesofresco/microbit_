# Imports go at the top
from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        display.show(random.randint(0,10))
        sleep(500)
    else:
        display.show(Image.GHOST)

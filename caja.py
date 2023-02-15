# Imports go at the top
from microbit import *
import music

def encender_y_apagar_led(veces):
    for i in range(veces):
        display.show("X")
        sleep(500)
        music.play("D2:2")
        display.show("O")
        sleep(500)
encender_y_apagar_led(2)

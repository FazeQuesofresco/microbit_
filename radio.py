
# Imports go at the top
from microbit import *
import radio

radio.on()
radio.config(channel=10)

while True:
    if button_a.was_pressed():
        mensaje ="A"
        radio.send(mensaje)
        display.show(mensaje)
        sleep(1000)
    elif button_b.was_pressed():
        mensaje ="B"
        radio.send(mensaje)
        display.show(mensaje)
        sleep(1000)
    else:
        display.show("?")
        sleep(1000)

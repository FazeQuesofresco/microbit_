
# Imports go at the top
from microbit import *
contador = 0

while True:
    if button_a.get_presses():
        contador = contador + 1
    elif button_b.get_presses():
        contador = contador - 1
    elif button_a.is_pressed() and button_b.is_pressed():
        contador = 0
    elif pin_logo.is_touched():
        display.show("Pepe")
    else:
        display.show(contador)

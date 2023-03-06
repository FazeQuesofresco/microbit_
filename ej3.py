# Imports go at the top
from microbit import *
import random
import music

music.play(music.BA_DING)
musica = [music.BA_DING,music.WAWAWAWAA,music.POWER_DOWN,music.POWER_UP]

while True:
    if button_a.was_pressed():
        musica_aleatoria=musica[random.randint(0,len(musica)-1)]
        music.play(musica_aleatoria)
        sleep(500)

    else:
        display.show(Image.SNAKE)

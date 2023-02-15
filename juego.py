#imports go at the top
from microbit import*
import random
import music

vocales =['A','E','I','O','U']
consonantes=['B','C','D','F','G','H','J','K','L','M','N','Ñ','P','Q','R','S','T','V','W','X','Y','Z',]
total_palabras = 9
while total_palabras>0:
    if button_a.was_pressed():
        vocal_aleatoria=vocales[random.randint(0,len(vocales)-1)]
        display.show(vocal_aleatoria)
        total_palabras=total_palabras-1
        sleep(1000)
        
    elif button_b.was_pressed():
        display.show("?")
    if button_b.was_pressed():
        consonante_aleatoria=consonantes[random.randint(0,len(consonantes)-1)]
        display.show(consonante_aleatoria)
        total_palabras=total_palabras-1
        sleep(1000)
    else:
        display.show("?")
   

ltsNotas =['f4:2','g4:2','e4:2','c4:2','D4:3','D4:2','a4:2','g4:3','f4:3','e4:3','e4:2','e4:2','g4:3','f4:2','e4:2','D4:3','D4:2','F4:2','e4:2','F4:2','e4:2','F4:2','D4:3','D4:2']
display.scroll("Fin")
cuenta =30
while cuenta>0:
    cuenta=cuenta-1
    display.scroll(cuenta,delay=30)
    sleep(1000)

music.play(ltsNotas)

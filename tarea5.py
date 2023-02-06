#imports go at the top
from microbit import*


lista_nombres = ["Pepe","Esteban","Daniel","Lucas","María","Nicolás","Abulai","Alicia"] 

i=0

while True:
    if button_a.was_pressed():
        i=i-1
        sleep(500)
    elif button_b.was_pressed():
        i=+1
        sleep(500)
        
    if i>len(lista_nombres)-1:
        i=0
    elif i<0:
        i = len(lista_nombres)-1
    else:
        display.show(i)
        sleep(500)
        display.show(lista_nombres[i])
        sleep(500)
        

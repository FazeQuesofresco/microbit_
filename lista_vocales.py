#imports go at the top
from microbit import*


lista_vocales = ["A","E","I","O","U"] 

index=0

while(index < len(lista_vocales)):
    display.show(lista_vocales[index])
    index = index+1
    sleep(1000)

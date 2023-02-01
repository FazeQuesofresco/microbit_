#imports go at the top
from microbit import*


imagenes= [Image.HEART,Image.HEART_SMALL] 



while True:
    display.show(Image.HEART_SMALL)
    sleep(500)
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)

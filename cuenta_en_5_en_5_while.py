# Imports go at the top
from microbit import *

i=1
while(i<31):
    display.scroll(str(i))
    i = i + 5

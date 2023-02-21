from microbit import*
import music

Bob_Esponja_Parte1 = ["","G4","A4","G4","E4","C4","E4","G4","A4","G4","E4:2"]


while True:
    music.play (Bob_Esponja_Parte1)
    sleep(1000)
    display.show("Bob Esponja")
    sleep(2000)

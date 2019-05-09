# mb1 programozása
# programiranje mb1

from microbit import *
import radio

# A rádió címzésének, csoportjának, és erejének beállítása.
# Podešavanje adrese, grupe i jačine za radio.
radio.config(group=0)
radio.config(power=7)

lepesek = 0
ido = 0
azElkuldottRadioJelMegerkezett = 0

# Reszet, vagy a microbit bekapcsolása után
# Posle uključivanja ili resetovanja mikrobita.

radio.on()

while True:
    fogottJel = radio.receive()
    if fogottJel == "started":
        versenyzoElindult = 1
        display.show(Image.RABBIT)
    else:
        versenyzoElindult = 0
        # Különben mutassa az "MB2" szöveget.
        # Inače treba prikazati neprekidno "MB2" tekst.
        display.scroll("MB2")

while True:
    if versenyzoElindult == 1:
        radio.off()
        ido += 1
        if ido < 10:
            if accelerometer.was_gesture("down"):
                lepesek += 1

lepesek = lepesek * 2

# Ismételgeti a rádióadást, míg nem kap jelet, hogy mb1 vette a jelet.
while True:
    if azElkuldottRadioJelMegerkezett == 0:
        radio.on()
        radio.send(str(lepesek))
        fogottJel = radio.receive()
        if fogottJel == "megjott":
            azElkuldottRadioJelMegerkezett = 1


radio.off()
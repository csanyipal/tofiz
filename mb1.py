# mb1 programozása
# programiranje mb1

from microbit import *
# import radio

# A rádió címzésének, csoportjának, és erejének beállítása.
# Podešavanje adrese, grupe i jačine za radio.
# radio.config(address="tofiz")
# radio.config(group=0)
# radio.config(power=7)

# Reszet, vagy a microbit bekapcsolása után.
# Posle uključivanja ili resetovanja mikrobita.

while True:
    if button_a.was_pressed():
        # Ha az A gomb le lett nyomva legalább egyszer,
        # akkor mutassa a "Go!" szöveget,
        # majd az "A" betűt, s végül a "<-" képet.
        # Ezután indulhat a versenyző!
        # Ako je dugme A pritisnuto bar jedanput,
        # treba prikazati "Go!" tekst,
        # pa "A" slovo i najzad "<-" sliku.
        # Takmičar može krenuti!
        display.scroll("Go!")
        display.show("A")
        sleep(500)
        display.show(Image.ARROW_W)
        sleep(500)
        break
    else:
        # Különben mutassa az "MB1" szöveget,
        # majd az "A" betűt, s végül a "<-" képet.
        # Inače treba prikazati neprekidno "MB1" tekst,
        # pa "A" slovo i najzad "<-" sliku.
        display.scroll("MB1")
        display.show("A")
        sleep(500)
        display.show(Image.ARROW_W)
        sleep(500)

# Ezek után a főbíró - akinél az mb1 van - elszámol háromtól egyig így:
# három, kettő, egy; és e pillanatban megnyomja az mb1 A gombját.
# Sada sudija - kod kojeg je mb1 - treba da odbroji od tri do jedan ovako:
# tri, dva, jedan; i u tom trenutku treba da pritisne dugme A na mb1.
while True:
    if button_a.was_pressed():
        # Jelzi, hogy a rádiójel el lett küldve mb2 -nek, és
        # el is küldi a jelet, ami egy kis s betű,
        # miután az A gomb le lett nyomva az mb1 -en.
        # Prikazuje da je radio signal ( malo slovo s )
        # poslat mb2 mikrobitu posle pritiska dugmeta A na mb1.
        # Takođe šalje taj signal.
        display.show("R")
#        radio.on()
#        radio.send("s")
        break
    else:
        # Jelzi, hogy le kell nyomni az A gombot.
        # Prikazuje A što znači da treba pritisnuti dugme A.
        display.show("A")
        sleep(500)
        display.show(Image.ARROW_W)
        sleep(500)
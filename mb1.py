# mb1 programozása
# programiranje mb1

from microbit import *
# import radio

# Reszet, vagy a microbit bekapcsolása után.
# Posle uključivanja ili resetovanja mikrobita.

while True:
    if button_a.was_pressed():
        # Ha az A gomb le lett nyomva legalább egyszer,
        # akkor mutassa az "S" jelet.
        # Ezután indulhat a versenyző!
        # Ako je dugme A pritisnuto bar jedanput,
        # treba prikazati "S" karakter.
        # Takmičar može krenuti!
        display.show("S")
        break
    else:
        # Különben mutassa az "MB1" jelet.
        # Inače treba prikazati neprekidno "MB1" tekst.
        display.scroll("MB1")

# A bírónak figyelnie kell, hogy az A gomb lenyomása után
# észrevegye az S betűt.
# Sudija treba da obrati svoju pažnju na mikrobit
# da bi zapazio S karakter.
sleep(2000)

# Miután a bíró észrevette az S betűt, jöhet a következő feladata.
# Ezek után a főbíró - akinél az mb1 van - elszámol háromtól egyig így:
# három, kettő, egy; és e pillanatban megnyomja az mb1 A gombját.
# Kad je sudija zapazio znak S, sledi njegov sledeći zadatak.
# Sudija - kod kojeg je mb1 - treba da odbroji unazad od tri do jedan ovako:
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
# mb2 programozása
# programiranje mb2

from microbit import *
import radio
import utime

# A rádió címzésének, csoportjának, és erejének beállítása.
# Podešavanje adrese, grupe i jačine za radio.
radio.config(group=0)
radio.config(power=7)

# Megjelenítendő képek:
# Slike za pokazivanje:
# Znak "?!".
kepKerdFelkialt = Image("99009:"
                        "00909:"
                        "09009:"
                        "00000:"
                        "09009")

# Znak "2".
kep2 = Image("09000:"
             "90900:"
             "00900:"
             "09000:"
             "99900")

# Znak "A".
kepA = Image("09900:"
             "90090:"
             "99990:"
             "90090:"
             "90090:")

# Znak "B".
kepB = Image("09990:"
             "09009:"
             "09990:"
             "09009:"
             "09990:")

# Znak za pešačenje.
kepFutas = Image("00900:"
                 "99999:"
                 "00900:"
                 "09090:"
                 "90009:")

# Znak "->".
kepK = Image("00900:"
             "00090:"
             "55559:"
             "00090:"
             "00900:")

# Znak "<-".
kepNY = Image("00900:"
              "09000:"
              "95550:"
              "09000:"
              "00900:")

# korak
lepes = 0

# Reszet, vagy a microbit bekapcsolása után
# Posle uključivanja ili resetovanja mikrobita.

while True:
    if button_a.was_pressed():
        break
    else:
        # Különben mutassa a "2" szöveget,
        # majd az "<-" nyilat, s végül a "A" képet.
        # Inače treba prikazati neprekidno "2" tekst,
        # pa "<-" i najzad "A".
        display.show(kep2)
        sleep(500)
        display.show(kepNY)
        sleep(500)
        display.show(kepA)
        sleep(500)

radio.on()

while True:
    # fogottJel je dobijeniSignal
    fogottJel = radio.receive()
    if fogottJel is not None:
        # Ha megjött a jel, akkor mutassa a gyaloglás képét.
        # Ako je stigao signal onda treba prikazati sliku pešačenja.
        display.show(kepFutas)
        break
    else:
        # Különben a "?!" jelet mutassa.
        # Inače se prikazuje "?!" znak.
        display.show(kepKerdFelkialt)

radio.off()

# Elkezdi mérni az időt tíz másodpercig.
# Počinje meriti vreme do dest sekundi.
# mostan je sada
mostan = int(utime.ticks_ms() / 1000)
while True:
    if int(utime.ticks_ms() / 1000) > mostan + 10:
        break
    else:
        if accelerometer.was_gesture("3g"):
            # povećava se broj koraka
            lepes += 1

display.show(Image.HAPPY)
sleep(1000)

# Megvannak a lépések, amit mb2 összeszámolt tíz mp alatt.
# mb2 -nek el kell küldenie mb1 számára e lépések számát!
# Sada imamo broj koraka učinjenih za deset sekundi.
# Sada treba mb2 to poslati za mb1!
radio.on()
radio.send(str(lepes))
radio.off()
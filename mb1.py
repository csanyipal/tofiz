# mb1 programozása
# programiranje mb1

from microbit import *
import radio

# A rádió címzésének, csoportjának, és erejének beállítása.
# Podešavanje adrese, grupe i jačine za radio.
radio.config(group=0)
radio.config(power=7)

# Megjelenítendő képek:
# Slike za pokazivanje:
# Znak "1".
kep1 = Image("09000:"
             "99000:"
             "09000:"
             "09000:"
             "09000")

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

# Znak "?!".
kepKerdFelkialt = Image("99009:"
                        "00909:"
                        "09009:"
                        "00000:"
                        "09009")

# Reszet, vagy a microbit bekapcsolása után.
# Posle uključivanja ili resetovanja mikrobita.

while True:
    if button_a.was_pressed():
        # Ha az A gomb le lett nyomva legalább egyszer,
        # akkor kiléphetünk e körből.
        # Ako je dugme A pritisnuto bar jedanput,
        # onda se može izaći iz ovog ciklusa.
        break
    else:
        # Különben mutassa az "1" szöveget,
        # majd "<-" képet, s végül az "A" betűt.
        # Inače treba prikazati neprekidno "1" tekst,
        # pa "<-" sliku i najzad "A" slovo.
        display.show(kep1)
        sleep(500)
        display.show(kepNY)
        sleep(500)
        display.show(kepA)
        sleep(500)

# Ezek után a főbíró - akinél az mb1 van - elszámol háromtól egyig így:
# három, kettő, egy; és e pillanatban megnyomja az mb1 B gombját.
# Sada sudija - kod kojeg je mb1 - treba da odbroji od tri do jedan ovako:
# tri, dva, jedan; i u tom trenutku treba da pritisne dugme B na mb1.
while True:
    if button_b.was_pressed():
        # Elküldi az IdoIndul szöveget,
        # miután a B gomb le lett nyomva az mb1 -en.
        # Šalje "IdoIndul" signal mb2 mikrobitu posle
        # pritiska dugmeta B na mb1.
        # IdoIndul je MerenjeVremenaPocinje
        radio.on()
        radio.send("IdoIndul")
        sleep(100)
        radio.off()
        break
    else:
        # Jelzi, hogy le kell nyomni a B gombot.
        # Prikazuje B što znači da treba pritisnuti dugme B.
        display.show(kepB)

# Most már a versenyző elindult,
# az "IdoIndul" rádióüzenet el lett küldve mb2 -nek.
# Sad je takmičar već krenuo, radio signal je već poslato na mb2.
display.show("R")

radio.on()

while True:
    # fogottJel je dobijeniSignal
    fogottJel = radio.receive()
    if fogottJel is not None:
        # Ha megjött a jel, akkor mutassa a futás képét.
        # Ako je stigao signal onda treba prikazati sliku trčanja.
        break
    else:
        # Különben mutassa a "?!" jelet.
        # Inače treba prikazati "?!" znak.
        display.show(kepKerdFelkialt)

# Megkétszerezzük a lépések számát.
# Udvostručava se broj koraka.
lepesek = int(fogottJel) * 2

# Most ki kell számolnunk a sebességet.
# A megtett út egyenlő a lépések megkétszerezett számának,
# és a lépés átlaghosszának szorzatával.
# Sada se izračunava brzina.
# Put je jednako sa proizvodom udvostručenih koraka
# i prosečne dužine koraka.
# atlagLepesHossz je prosecnaDuzinaKoraka
# ut je put
# lepesek je koraci
# sebesseg je brzina
atlagLepesHossz = 0.66355
ut = lepesek * atlagLepesHossz
sebesseg = ut / 10

while True:
    # Megjelenítjük a sebességet m/sec -ben.
    # Prikazuje se brzina u m/sec.
    display.scroll(str(sebesseg))
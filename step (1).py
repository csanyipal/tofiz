from microbit import *
import radio

radio.on()

koraci = 0
vreme = 0

display.show(str(koraci))
vreme = str(vreme)

while True:
    vreme += 1
        
if vreme < 10:
    if accelerometer.was_gesture("shake"):
        steps += 1
        if steps < 10:
            display.show(str(koraci))
        else:
            display.scroll(str(koraci))
        
if vreme > 10:
    steps += 0

if button_a.is_pressed():
    radio.send(koraci)
    incoming = radio.recieve()
    display.show(str(koraci))
    sleep(2500)
    display.clear()
    
if button_b.is_pressed():
    display.show()       # ovde trebaju da se dodaju podaci za izracunavanje brzine :)
    
    
    
    
    
            
    

        
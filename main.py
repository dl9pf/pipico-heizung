from machine import Pin
from time import sleep

epoch=0

# Initialisierung von "LED" als Ausgang
led_onboard = Pin("LED", Pin.OUT)

import ugit
ugit.pull_all()

while True:
    # LED einschalten
    led_onboard.on()
    # 5 Sekunden warten
    sleep(1)
    epoch=epoch+1
    # LED ausschalten
    led_onboard.off()
    # 5 Sekunden warten
    sleep(1)
    epoch=epoch+1


    # daily reboot
    if epoch > 10 :
        machine.reset()

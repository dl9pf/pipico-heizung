from machine import Pin
from time import sleep

# Initialisierung von "LED" als Ausgang
led_onboard = Pin("LED", Pin.OUT)

while True:
    # LED einschalten
    led_onboard.on()
    # 5 Sekunden warten
    sleep(1)

    # LED ausschalten
    led_onboard.off()
    # 5 Sekunden warten
    sleep(1)

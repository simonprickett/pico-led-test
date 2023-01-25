from machine import Pin
from time import sleep

leds = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT),
    Pin(5, Pin.OUT),
    Pin(6, Pin.OUT),
    Pin(7, Pin.OUT),
    Pin(8, Pin.OUT),
    Pin(9, Pin.OUT)
]

while True:
    for led in leds:
        led.value(0)
        sleep(.2)
        led.value(1)

    for led in leds[::-1]:
        led.value(1)
        sleep(.2)
        led.value(0)

    sleep(.5)
    
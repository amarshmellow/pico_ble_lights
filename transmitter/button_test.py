from machine import Pin
import utime

led = Pin("LED", Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)


for i in range(3):
    led.on()
    utime.sleep(0.1)
    led.off()

while True:
    if button.value() == 0:
        led.on()
        print("ON")
    else:
        led.off()
        print("OFF")
    utime.sleep(0.1) 
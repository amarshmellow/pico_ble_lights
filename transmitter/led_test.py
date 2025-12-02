from machine import Pin
import utime

led = Pin("LED", Pin.OUT)


for i in range(3):
    led.on()
    utime.sleep(0.1)
    led.off()
    utime.sleep(0.1)

button = Pin(14, Pin.IN, Pin.PULL_UP)
oled =  Pin(10, Pin.OUT)

while True:
    if button.value() == 0:
        oled.value(1)
    else:
        oled.value(0)
    utime.sleep(0.1)   

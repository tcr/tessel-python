import time
import tessel

while True:
    for led in tessel.led:
        led.write(1)
    time.sleep(.2)
    for led in tessel.led:
        led.write(0)
    time.sleep(.2)

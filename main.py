print("Now inside main.py")

import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

on_time = 0.5
off_time = 0.5
while True:
    led.value(1)
    print("LED ON for : ", str(on_time))
    time.sleep(on_time)
    led.value(0)
    print("LED OFF for : ", str(off_time))
    time.sleep(off_time)
	

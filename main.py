import machine
import time
import random

led = machine.Pin(2, machine.Pin.OUT)

valid_times = [0.25, 0.5, 0.75, 1, 1.5, 2]

while True:
	on_time = random.choice(valid_times)
	off_time = random.choice(valid_times)

    led.value(1)
    print("LED ON for : ", str(on_time))
    time.sleep(on_time)
    led.value(0)
    print("LED OFF for : ", str(off_time))
    time.sleep(off_time)
	

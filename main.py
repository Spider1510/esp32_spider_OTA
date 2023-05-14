import machine
import time
import random
import neopixel

led = machine.Pin(2, machine.Pin.OUT)

valid_times = [0.25, 0.5, 0.75, 1, 1.5, 2]

# while True:
for i in range(0, 1):
	on_time = random.choice(valid_times)
	off_time = random.choice(valid_times)

	led.value(1)
	print("LED ON for : ", str(on_time))
	time.sleep(on_time)
	led.value(0)
	print("LED OFF for : ", str(off_time))
	time.sleep(off_time)

# Code for ws2812b strip
print("Staring ws2812b led strip v2...")
LED_PIN = 4

NUM_LEDS = 12

led_strip = neopixel.NeoPixel(machine.Pin(LED_PIN), NUM_LEDS)

led_strip.fill((255, 0, 0))
led_strip.write()

time.sleep(1)

led_strip.fill((0, 255, 0))
led_strip.write()

time.sleep(1)

led_strip.fill((0, 0, 255))
led_strip.write()

while True:
	for i in range(NUM_LEDS):
		led_strip[i] = (255, 0, 0)
		led_strip.write()
		time.sleep(1)

	led_strip.fill(0, 0, 0)
	led_strip.write()
	time.sleep(2)

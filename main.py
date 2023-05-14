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
print("Staring ws2812b led strip animations v1...")
LED_PIN = 4

NUM_LEDS = 12

led_strip = neopixel.NeoPixel(machine.Pin(LED_PIN), NUM_LEDS)

#
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)
COLOR_YELLOW = (255, 255, 0)

ANIMATION_DELAY = 0.5

def wheel(pos):
	if pos < 85:
		return (pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return (255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return (0, pos * 3, 255 - pos * 3)

def color_wipe(color, wait):
	for i in range(NUM_LEDS):
		led_strip[i] = color
		led_strip.write()
		time.sleep(wait)

def theater_chase(color, wait):
	for j in range(10):
		for q in range(3):
			for i in range(0, NUM_LEDS, 3):
				led_strip[i+q] = color
			led_strip.write()
			time.sleep(wait)
			for i in range(0, NUM_LEDS, 3):
				led_strip[i+q] = (0,0,0)

def rainbow_cycle(wait):
	for j in range(255):
		for i in range(NUM_LEDS):
			rc_index = (i * 256 // NUM_LEDS) + j
			led_strip[i] = wheel(rc_index & 255)
		led_strip.write()
		time.sleep(wait)

#

led_strip.fill((255, 0, 0))
led_strip.write()

time.sleep(1)

# led_strip.fill((0, 255, 0))
# led_strip.write()

# time.sleep(1)

# led_strip.fill((0, 0, 255))
# led_strip.write()

# while True:
# 	for i in range(NUM_LEDS):
#		led_strip[i] = (255, 0, 0)
#		led_strip.write()
#		time.sleep(1)

#	led_strip.fill((0, 0, 0))
#	led_strip.write()
#	time.sleep(2)

while True:
	color_wipe(COLOR_RED, ANIMATION_DELAY)
	color_wipe(COLOR_GREEN, ANIMATION_DELAY)
	color_wipe(COLOR_BLUE, ANIMATION_DELAY)
	theater_chase(COLOR_PURPLE, ANIMATION_DELAY)
	theater_chase(COLOR_YELLOW, ANIMATION_DELAY)
	rainbow_cycle(ANIMATION_DELAY)


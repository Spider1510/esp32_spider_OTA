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
# Define the pin that the LED strip is connected to
LED_PIN = 4

# Define the number of LEDs in the strip
NUM_LEDS = 12

# Create a neopixel object with the LED pin and number of LEDs
led_strip = neopixel.NeoPixel(machine.Pin(LED_PIN), NUM_LEDS)

# Set the color of all LEDs to red
led_strip.fill((255, 0, 0))

# Display the new colors on the LED strip
led_strip.write()

# Wait for 1 second
time.sleep(1)

# Set the color of all LEDs to green
led_strip.fill((0, 255, 0))

# Display the new colors on the LED strip
led_strip.write()

# Wait for 1 second
time.sleep(1)

# Set the color of all LEDs to blue
led_strip.fill((0, 0, 255))

# Display the new colors on the LED strip
led_strip.write()

# Wait for 1 second
# machine.delay(1000)

# Set the color of all LEDs to off (black)
# led_strip.fill((0, 0, 0))

# Display the new colors on the LED strip
# led_strip.write()



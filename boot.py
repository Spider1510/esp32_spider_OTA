import machine
import time
# import ugit

# ugit.wificonnect()
# ugit.backup()
# ugit.pull_all()

led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
    

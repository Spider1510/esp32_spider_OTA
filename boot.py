import machine
import time
import os
import ugit

do_ota = "0"
with open("ota_status.txt", "r") as f:
    do_ota = f.read()
    print("OTA staus : ", do_ota)

if(do_ota == "1"):
    with open("ota_status.txt", "w") as f:
        f.write("0")
    ugit.wificonnect()
    # ugit.backup()
    ugit.pull_all()


with open("ota_status.txt", "w") as f:
    f.write("1")

led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(2)
    led.value(0)
    time.sleep(0.35)

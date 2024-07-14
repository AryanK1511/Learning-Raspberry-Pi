"""
* Started off by connecting the anode to GPIO 25
* Connected the cathode to the ground GPIO
"""

from gpiozero import LED
from time import sleep

led = LED(25)

# Alternate between ON and OFF states every one second
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
